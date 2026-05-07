"""
creator_monitor_quick.py - 快速版本
将 http_get timeout 降为 3 秒，快速失败
"""
import sys, os, json, ssl, time, re, hashlib, xml.etree.ElementTree as ET, urllib.request, urllib.parse
from datetime import datetime, timedelta
from pathlib import Path

# 翻译支持
try:
    from deep_translator import GoogleTranslator
    TRANSLATOR = GoogleTranslator(source='en', target='zh-CN')
    HAS_TRANSLATOR = True
except Exception:
    HAS_TRANSLATOR = False

_trans_cache = {}

SKILL_DIR = Path(r"C:\Users\YF\.workbuddy\skills\ai-news")
CREATORS_FILE = SKILL_DIR / "creators.json"
STATE_FILE = SKILL_DIR / "creator_state.json"
REPORTS_DIR = SKILL_DIR / "reports"
CREATORS_REPORT = SKILL_DIR / "creator-updates.html"
REPORTS_DIR.mkdir(exist_ok=True)

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/rss+xml, application/xml, text/html, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}
BILI_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://www.bilibili.com",
    "Origin": "https://www.bilibili.com",
    "Cookie": "buvid3=DE080968-2D70-5F51-E0C0-759961FB89E013544infoc; b_nut=1759847413; _uuid=F495F455-D10C3-8E64-8914-DCFBE3A4B42D15608infoc; CURRENT_QUALITY=0; rpdid=|(umRkRmJlR|0J'u~lm)R~RuY; buvid_fp=f95190dbe51573f797a43d5e87db1a41; buvid4=C2001806-1EA5-AB0A-BA58-A807D71AA62818785-025100722-pW1elzmXyBcBMDE3AZRexQ%3D%3D; CURRENT_FNVAL=2000; DedeUserID=650476746; DedeUserID__ckMd5=b0d6e6b747fe73ab; theme-tip-show=SHOWED; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i2.hdslb.com; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzU5NTU3NjAsImlhdCI6MTc3NTY5NjUwMCwicGx0IjotMX0.NHWKr4DeoQOZsMdCaA3iXBuxjI6-DDIRW7_07J5uuuM; bili_ticket_expires=1775955700; theme-avatar-tip-show=SHOWED; bili_jct=88e205998a4b5f575e965bc9008d9624; sid=8sz07zp9; home_feed_column=4; browser_resolution=536-768; b_lsid=F0FB31F3_19D6FD6A744",
}

YOUTUBE_CHANNEL_IDS = {
    "ak": "UCXUPKJO5MZQN11PqgIvyuvQ",
    "lex": "UCSHZKyawb77ixDdsGog4iWA",
    "openai-yt": "UCXZCJLdBC09xxGZ6gcdrc6A",
    "3b1b": "UCYO_jab_esuFRV4b17AJtAw",
    "sentdex": "UCfzlCWGWYyIQ0aLC5w48gBQ",
}

# === 快速超时版本 http_get (3秒) ===
def http_get_quick(url, headers=None, timeout=3):
    h = dict(HEADERS)
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    try:
        resp = urllib.request.urlopen(req, timeout=timeout, context=CTX)
        return resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return None

def parse_youtube_rss(xml_text):
    if not xml_text:
        return []
    try:
        root = ET.fromstring(xml_text)
        videos = []
        for entry in root.findall("entry"):
            vid = {}
            vid["title"] = entry.findtext("title", "无标题")
            vid["link"] = entry.findtext("link", "").replace("&", "&amp;")
            vid["published"] = entry.findtext("published", "")
            vid["id"] = entry.findtext("yt:videoId", entry.findtext("id", ""))
            media = entry.find("media:group", {"media": "http://search.yahoo.com/mrss/"})
            if media is not None:
                vid["desc"] = media.findtext("media:description", "")
                thumb = media.find("media:thumbnail", {"media": "http://search.yahoo.com/mrss/"})
                if thumb is not None:
                    vid["thumbnail"] = thumb.get("url", "")
            vid["platform"] = "youtube"
            videos.append(vid)
        return videos
    except Exception:
        return []

def fetch_bilibili_videos(mid, pn=1, ps=5):
    url = f"https://api.bilibili.com/x/space/arc/search?mid={mid}&pn={pn}&ps={ps}&jsonp=jsonp"
    data = http_get_quick(url, headers=BILI_HEADERS, timeout=5)
    if not data:
        return []
    try:
        j = json.loads(data)
        if j.get("code") != 0:
            return []
        vlist = j.get("data", {}).get("list", {}).get("vlist", [])
        videos = []
        for v in vlist:
            videos.append({
                "title": v.get("title", "无标题"),
                "id": str(v.get("aid", "")),
                "link": f"https://www.bilibili.com/video/{v.get('bvid', '')}",
                "published": datetime.fromtimestamp(v.get("created", 0)).strftime("%Y-%m-%dT%H:%M:%S") if v.get("created") else "",
                "desc": v.get("description", ""),
                "thumbnail": f"https:{v.get('pic', '')}",
                "platform": "bilibili",
            })
        return videos
    except Exception:
        return []

def parse_nitter_rss(xml_text):
    if not xml_text:
        return []
    try:
        root = ET.fromstring(xml_text)
        items = []
        for item in root.findall(".//item"):
            title = item.findtext("title", "")
            link = item.findtext("link", "")
            pub = item.findtext("pubDate", "")
            desc = item.findtext("description", "")
            items.append({
                "title": title,
                "link": link,
                "published": pub,
                "desc": desc,
                "platform": "twitter",
            })
        return items
    except Exception:
        return []

def load_creators():
    with open(CREATORS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"last_check": "", "seen_ids": {}}

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def hash_text(text):
    if not text:
        return ""
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:12]

def check_new_items(creator, items, state):
    if not items:
        return []
    key = creator.get("id", creator.get("name", ""))
    seen = state.setdefault("seen_ids", {}).setdefault(key, [])
    new_items = []
    for item in items:
        item_id = item.get("id", "") or item.get("link", "") or hash_text(item.get("title", ""))
        if item_id and item_id not in seen:
            new_items.append(item)
            seen.append(item_id)
            if len(seen) > 200:
                seen[:] = seen[-200:]
    return new_items

def translate_text(text):
    if not text or not HAS_TRANSLATOR:
        return text
    h = hash_text(text[:100])
    if h in _trans_cache:
        return _trans_cache[h]
    try:
        result = TRANSLATOR.translate(text[:500])
        _trans_cache[h] = result
        return result
    except Exception:
        return text

def generate_interpretation(item, creator, date_str, lang="cn"):
    title = item.get("title", "")
    desc = item.get("desc", "")[:300]
    link = item.get("link", "")
    platform = item.get("platform", "unknown")
    pub = item.get("published", "")[:10]

    platform_icons = {"youtube": "▶️", "bilibili": "📺", "twitter": "🐦"}
    icon = platform_icons.get(platform, "📌")

    summary_cn = ""
    summary_en = desc

    if lang == "cn":
        summary_cn = translate_text(desc) if desc else ""
        content_html = f"""<p>{summary_cn}</p>"""
    else:
        content_html = f"""<p>{desc}</p>"""

    return {
        "icon": icon,
        "platform": platform,
        "title": title,
        "pub": pub,
        "content": content_html,
        "link": link,
        "creator": creator.get("name", "unknown"),
    }

def render_updates_page(items, date_str, lang="cn"):
    if not items:
        return ""
    header_h1 = "AI 创作者今日动态" if lang == "cn" else "AI Creator Updates Today"
    header_sub = "优质内容，一网打尽" if lang == "cn" else "Curated AI content from top creators"

    cards_html = ""
    for item in items:
        icon = item.get("icon", "📌")
        title = item.get("title", "")
        creator = item.get("creator", "")
        content = item.get("content", "")
        link = item.get("link", "")
        pub = item.get("pub", "")
        platform = item.get("platform", "")

        platform_badge = {
            "youtube": '<span style="background:#FF0000;color:#fff;padding:2px 8px;border-radius:10px;font-size:11px;margin-left:8px;">YouTube</span>',
            "bilibili": '<span style="background:#00A1D6;color:#fff;padding:2px 8px;border-radius:10px;font-size:11px;margin-left:8px;">B站</span>',
            "twitter": '<span style="background:#1DA1F2;color:#fff;padding:2px 8px;border-radius:10px;font-size:11px;margin-left:8px;">X</span>',
        }.get(platform, "")

        cards_html += f"""
        <div class="update-card">
            <div class="card-header">
                <span class="creator-name">{creator}</span>
                {platform_badge}
            </div>
            <h3 class="card-title"><a href="{link}" target="_blank">{title}</a></h3>
            <div class="card-meta">{pub}</div>
            <div class="card-content">{content}</div>
        </div>"""

    footer_text = "由 AI 日课创作者监控系统生成" if lang == "cn" else "Generated by AI Daily Creator Monitor"
    if lang == "cn":
        footer_link = '<a href="creator-updates-en.html">English Version</a>'
    else:
        footer_link = '<a href="creator-updates.html">中文版</a>'

    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{header_h1} - {date_str}</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#0a0a1a;color:#e0e0f0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;padding:40px 20px}}
.container{{max-width:1200px;margin:0 auto}}
.header{{text-align:center;margin-bottom:50px}}
.date-tag{{display:inline-block;background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;padding:6px 20px;border-radius:20px;font-size:13px;font-weight:500;margin-bottom:16px}}
.header h1{{font-size:38px;font-weight:900;background:linear-gradient(135deg,#fff,#a0a0ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:10px}}
.header .subtitle{{color:#888;font-size:15px}}
.update-count{{text-align:center;margin-bottom:40px}}
.count-badge{{display:inline-block;background:rgba(102,126,234,0.2);border:1px solid rgba(102,126,234,0.3);color:#8fa0ff;padding:8px 24px;border-radius:30px;font-size:14px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:20px}}
.update-card{{background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08);border-radius:16px;padding:24px;transition:all 0.3s}}
.update-card:hover{{background:rgba(255,255,255,0.07);transform:translateY(-2px)}}
.card-header{{margin-bottom:12px}}
.creator-name{{color:#8fa0ff;font-weight:600;font-size:14px}}
.card-title{{font-size:17px;font-weight:700;margin-bottom:8px;line-height:1.4}}
.card-title a{{color:#fff;text-decoration:none}}
.card-title a:hover{{color:#8fa0ff;text-decoration:underline}}
.card-meta{{color:#666;font-size:12px;margin-bottom:12px}}
.card-content{{color:#aaa;font-size:14px;line-height:1.7}}
.card-content p{{margin:0}}
.footer{{text-align:center;padding:50px 0 30px;color:#555;font-size:12px}}
.footer a{{color:#667eea;text-decoration:none}}
</style>
</head>
<body>
<div class="container">
    <div class="header">
        <div class="date-tag">📅 {date_str}</div>
        <h1>{header_h1}</h1>
        <p class="subtitle">{header_sub}</p>
    </div>
    <div class="update-count">
        <span class="count-badge">🔥 今日共 {len(items)} 条更新</span>
    </div>
    <div class="grid">
        {cards_html}
    </div>
    <div class="footer">
        <p>{footer_text} | {footer_link}</p>
    </div>
</div>
</body>
</html>'''
    return html

def main(date_str=None):
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")

    print(f"🤖 创作者更新监控  [{date_str}] (快速模式)")
    print("=" * 50)

    creators_data = load_creators()
    state = load_state()
    state["last_check"] = datetime.now().isoformat()

    all_new_items_cn = []
    all_new_items_en = []
    processed_count = 0
    new_count = 0

    # ── YouTube ──────────────────────────────────────────────
    yt_section = creators_data["platforms"]["youtube"]
    print(f"\n▶️  YouTube ({len(yt_section['creators'])} 个频道) [3s超时]")
    for creator in yt_section["creators"]:
        cid = YOUTUBE_CHANNEL_IDS.get(creator["id"], creator.get("channel_id", ""))
        if not cid:
            print(f"  ⚠️  无 channel_id: {creator['name']}")
            continue
        url = f"https://www.youtube.com/feeds/videos.xml?channel_id={cid}"
        print(f"  • {creator['name']} ...", end=" ")
        sys.stdout.flush()
        xml = http_get_quick(url)
        if xml is None:
            print("超时/失败")
            processed_count += 1
            continue
        videos = parse_youtube_rss(xml)
        new = check_new_items(creator, videos, state)
        if new:
            print(f"🆕 {len(new)}条!")
            new_count += len(new)
            for v in new:
                all_new_items_cn.append(generate_interpretation(v, creator, date_str, "cn"))
                all_new_items_en.append(generate_interpretation(v, creator, date_str, "en"))
        else:
            print(f"无更新")
        processed_count += 1
        time.sleep(0.3)

    # ── Twitter ─────────────────────────────────────────────
    tw_section = creators_data["platforms"]["twitter"]
    print(f"\n🐦 Twitter ({len(tw_section['creators'])} 个账号) [3s超时]")
    for creator in tw_section["creators"]:
        handle = creator.get("handle", creator.get("id", ""))
        if not handle:
            print(f"  ⚠️  无 handle: {creator['name']}")
            continue
        url = f"https://nitter.net/{handle}/rss"
        print(f"  • @{handle} ...", end=" ")
        sys.stdout.flush()
        xml = http_get_quick(url)
        if xml is None:
            print("超时/失败")
            processed_count += 1
            continue
        items = parse_nitter_rss(xml)
        new = check_new_items(creator, items, state)
        if new:
            print(f"🆕 {len(new)}条!")
            new_count += len(new)
            for v in new:
                all_new_items_cn.append(generate_interpretation(v, creator, date_str, "cn"))
                all_new_items_en.append(generate_interpretation(v, creator, date_str, "en"))
        else:
            print(f"无更新")
        processed_count += 1
        time.sleep(0.3)

    # ── Bilibili ────────────────────────────────────────────
    bili_section = creators_data["platforms"]["bilibili"]
    print(f"\n📺 Bilibili ({len(bili_section['creators'])} 个UP主) [5s超时]")
    for creator in bili_section["creators"]:
        uid = creator.get("uid", "")
        if not uid:
            print(f"  ⚠️  无 UID: {creator['name']}")
            continue
        print(f"  • {creator['name']} ...", end=" ")
        sys.stdout.flush()
        videos = fetch_bilibili_videos(uid, ps=5)
        if not videos:
            print("获取失败")
            processed_count += 1
            continue
        new = check_new_items(creator, videos, state)
        if new:
            print(f"🆕 {len(new)}条新视频!")
            new_count += len(new)
            for v in new:
                all_new_items_cn.append(generate_interpretation(v, creator, date_str, "cn"))
                all_new_items_en.append(generate_interpretation(v, creator, date_str, "en"))
        else:
            print(f"无更新")
        processed_count += 1
        time.sleep(0.5)

    # ── 保存状态 ─────────────────────────────────────────────
    save_state(state)

    # ── 生成页面 ─────────────────────────────────────────────
    if all_new_items_cn:
        print(f"\n✅ 检测到 {len(all_new_items_cn)} 条新内容，正在生成页面...")
        html_cn = render_updates_page(all_new_items_cn, date_str, "cn")
        if html_cn:
            with open(CREATORS_REPORT, "w", encoding="utf-8") as f:
                f.write(html_cn)
            print(f"📄 中文版: {CREATORS_REPORT}")
        html_en = render_updates_page(all_new_items_en, date_str, "en")
        if html_en:
            en_path = SKILL_DIR / "creator-updates-en.html"
            with open(en_path, "w", encoding="utf-8") as f:
                f.write(html_en)
            print(f"📄 英文版: {en_path}")
    else:
        print(f"\n😴 今日没有新增内容")

    print(f"\n共处理 {processed_count} 个创作者 | 新增 {new_count} 条 | 状态已更新")
    return len(all_new_items_cn)

if __name__ == "__main__":
    date_arg = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime("%Y-%m-%d")
    main(date_arg)
