# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

"""
优质创作者更新监控脚本
监控 B站UP主、YouTube频道、Twitter大V 的最新内容
检测到新内容后生成解读页面

使用方法: python creator_monitor.py [日期]
"""
import json
import os
import ssl
import time
import re
import hashlib
import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
from pathlib import Path

# 翻译支持
try:
    from deep_translator import GoogleTranslator
    TRANSLATOR = GoogleTranslator(source='en', target='zh-CN')
    HAS_TRANSLATOR = True
except Exception:
    HAS_TRANSLATOR = False

# 翻译缓存 {text_hash: translated_text}
_trans_cache = {}

# ============ 路径配置 ============
SKILL_DIR = Path(r"C:\Users\YF\.workbuddy\skills\ai-news")
CREATORS_FILE = SKILL_DIR / "creators.json"
STATE_FILE = SKILL_DIR / "creator_state.json"
REPORTS_DIR = SKILL_DIR / "reports"
CREATORS_REPORT = SKILL_DIR / "creator-updates.html"

REPORTS_DIR.mkdir(exist_ok=True)

# ============ SSL + HTTP 配置 ============
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/rss+xml, application/xml, text/html, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}
BILI_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://www.bilibili.com",
    "Origin": "https://www.bilibili.com",
    "Cookie": "buvid3=DE080968-2D70-5F51-E0C0-759961FB89E013544infoc; b_nut=1759847413; _uuid=F495F455-D10C3-8E64-8914-DCFBE3A4B42D15608infoc; CURRENT_QUALITY=0; rpdid=|(umRkRmJlR|0J'u~lm)R~RuY; buvid_fp=f95190dbe51573f797a43d5e87db1a41; buvid4=C2001806-1EA5-AB0A-BA58-A807D71AA62818785-025100722-pW1elzmXyBcBMDE3AZRexQ%3D%3D; CURRENT_FNVAL=2000; DedeUserID=650476746; DedeUserID__ckMd5=b0d6e6b747fe73ab; theme-tip-show=SHOWED; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i2.hdslb.com; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzU5NTU3NjAsImlhdCI6MTc3NTY5NjUwMCwicGx0IjotMX0.NHWKr4DeoQOZsMdCaA3iXBuxjI6-DDIRW7_07J5uuuM; bili_ticket_expires=1775955700; theme-avatar-tip-show=SHOWED; bili_jct=88e205998a4b5f575e965bc9008d9624; sid=8sz07zp9; home_feed_column=4; browser_resolution=536-768; b_lsid=F0FB31F3_19D6FD6A744",
}

# ============ 已验证的 YouTube Channel ID ============
YOUTUBE_CHANNEL_IDS = {
    "ak": "UCXUPKJO5MZQN11PqgIvyuvQ",
    "lex": "UCSHZKyawb77ixDdsGog4iWA",
    "openai-yt": "UCXZCJLdBC09xxGZ6gcdrc6A",
    "3b1b": "UCYO_jab_esuFRV4b17AJtAw",
    "sentdex": "UCfzlCWGWYyIQ0aLC5w48gBQ",
}


def http_get(url, headers=None, timeout=12):
    h = dict(HEADERS)
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    try:
        resp = urllib.request.urlopen(req, timeout=timeout, context=CTX)
        return resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"    [HTTP ERR] {str(e)[:60]} - {url[:60]}")
        return None


def parse_youtube_rss(xml_text):
    """解析 YouTube RSS，返回视频列表"""
    if not xml_text:
        return []
    try:
        root = ET.fromstring(xml_text)
        ns = {"yt": "http://www.youtube.com/xml/schemas/2015"}
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
                    vid["thumb"] = thumb.get("url", "")
            vid["platform"] = "youtube"
            videos.append(vid)
        return videos
    except Exception as e:
        print(f"    [XML ERR] {e}")
        return []


def parse_nitter_rss(xml_text):
    """解析 nitter RSS，返回推文列表"""
    if not xml_text:
        return []
    try:
        root = ET.fromstring(xml_text)
        tweets = []
        for item in root.findall("channel/item"):
            t = {}
            t["title"] = item.findtext("title", "")
            t["link"] = item.findtext("link", "")
            t["published"] = item.findtext("pubDate", "")
            t["id"] = item.findtext("guid", "")
            # 清理 HTML 实体
            desc = item.findtext("description", "")
            desc = re.sub(r'<[^>]+>', '', desc)
            desc = desc.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
            t["desc"] = desc.strip()
            t["platform"] = "twitter"
            tweets.append(t)
        return tweets
    except Exception as e:
        print(f"    [XML ERR] {e}")
        return []


def fetch_bilibili_videos(mid, pn=1, ps=5):
    """获取B站用户最新视频"""
    url = f"https://api.bilibili.com/x/space/arc/search?mid={mid}&pn={pn}&ps={ps}&jsonp=jsonp"
    data = http_get(url, headers=BILI_HEADERS, timeout=10)
    if not data:
        return []
    try:
        j = json.loads(data)
        if j.get("code") != 0:
            msg = j.get("message", "未知错误")
            print(f"    [API ERR] code={j.get('code')}, msg={msg}")
            return []
        vlist = j.get("data", {}).get("list", {}).get("vlist", [])
        videos = []
        for v in vlist:
            ts = v.get("created", 0)
            pub_date = datetime.fromtimestamp(ts).isoformat() + "Z" if ts else ""
            videos.append({
                "title": v.get("title", "无标题"),
                "link": f"https://www.bilibili.com/video/{v.get('bvid', '')}",
                "published": pub_date,
                "id": v.get("bvid", ""),
                "desc": v.get("description", ""),
                "thumb": v.get("pic", ""),
                "platform": "bilibili",
                "duration": v.get("length", ""),
            })
        return videos
    except Exception as e:
        print(f"    [B站 ERR] {e}")
        return []


def load_creators():
    with open(CREATORS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"last_seen": {}, "last_check": ""}


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def item_key(item, creator_id, platform):
    """生成唯一标识符"""
    return hashlib.md5(f"{creator_id}:{item.get('id','') or item.get('title','')}".encode()).hexdigest()[:12]


def check_new_items(creator, items, state, days_back=3):
    """过滤出新增内容（最近N天内未看过的）"""
    creator_id = creator["id"]
    seen = set(state.get("last_seen", {}).get(creator_id, []))
    cutoff = datetime.now() - timedelta(days=days_back)
    new_items = []
    for item in items:
        key = item_key(item, creator_id, item["platform"])
        # 检查是否看过
        if key in seen:
            continue
        # 检查时间是否在范围内
        pub_str = item.get("published", "")
        try:
            if pub_str:
                if "T" in pub_str:
                    pub_dt = datetime.fromisoformat(pub_str.replace("Z", "+00:00").split("+")[0])
                else:
                    pub_dt = datetime.fromisoformat(pub_str.split(" +")[0].split(" -")[0])
                if pub_dt < cutoff:
                    seen.add(key)
                    continue
        except Exception:
            pass
        new_items.append(item)
        seen.add(key)
    # 更新状态
    if creator_id not in state["last_seen"]:
        state["last_seen"][creator_id] = []
    state["last_seen"][creator_id] = list(seen)
    return new_items


def is_foreign_text(text):
    """判断文本是否主要是外文（英文等），需要翻译"""
    if not text or len(text.strip()) < 10:
        return False
    # 统计中文字符数量
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text))
    total_chars = len(text.strip())
    if total_chars == 0:
        return False
    # 中文字符占比低于30%判定为外文
    return chinese_chars / total_chars < 0.3


def translate_text(text, cache=_trans_cache):
    """翻译外文文本为中文，带缓存"""
    if not HAS_TRANSLATOR or not text:
        return text
    key = hashlib.md5(text.encode()).hexdigest()[:16]
    if key in cache:
        return cache[key]
    try:
        # 每次最多翻译500字符（Google翻译限制）
        chunk = text[:500].strip()
        result = TRANSLATOR.translate(chunk)
        cache[key] = result
        time.sleep(0.3)  # 避免请求过快
        return result
    except Exception as e:
        print(f"    [翻译 ERR] {str(e)[:60]}")
        return text


def generate_interpretation(item, creator, date_str, lang="cn"):
    """生成单条内容的解读摘要
    lang='cn'  自动翻译外文为中文（默认）
    lang='en'  保留英文原文
    """
    platform = item["platform"]
    title = item.get("title", "无标题")
    desc = item.get("desc", "")
    link = item.get("link", "")
    thumb = item.get("thumb", "")

    # B站内容直接使用原文（中文）
    need_translate = platform in ("youtube", "twitter")

    if lang == "en" or not need_translate:
        # 英文原版：不做翻译
        title_cn = title
        summary_cn = desc[:300] + "..." if len(desc) > 300 else desc
        original_title = None
    else:
        # 中文版：翻译外文
        title_cn = title
        if is_foreign_text(title):
            title_cn = translate_text(title)
            print(f"    [翻译] {title[:50]} → {title_cn[:50]}")
        summary_raw = desc[:300] + "..." if len(desc) > 300 else desc
        if is_foreign_text(summary_raw):
            summary_cn = translate_text(summary_raw)
            print(f"    [翻译] {summary_raw[:50]} → {summary_cn[:50]}")
        else:
            summary_cn = summary_raw
        original_title = title if title != title_cn else None

    # 根据平台生成标签颜色
    colors = {
        "youtube": "#ff0000",
        "bilibili": "#00a1d6",
        "twitter": "#1da1f2",
    }
    icons = {
        "youtube": "▶️",
        "bilibili": "📺",
        "twitter": "🐦",
    }
    color = colors.get(platform, "#667eea")
    icon = icons.get(platform, "🔗")

    return {
        "platform": platform,
        "icon": icon,
        "color": color,
        "creator_name": creator["name"],
        "creator_profile": creator.get("profile", ""),
        "creator_handle": creator.get("handle", creator.get("uid", "")),
        "title": title_cn,
        "summary": summary_cn or "点击查看详细内容",
        "link": link,
        "thumb": thumb,
        "published": item.get("published", ""),
        "duration": item.get("duration", ""),
        "date_str": date_str,
        "original_title": title if title != title_cn else None,  # 保留原文（翻译时）
    }


def render_updates_page(all_updates, date_str, lang="cn"):
    """生成 HTML 页面，只显示今日更新
    lang='cn' 生成中文版（已翻译内容）
    lang='en' 生成英文原版
    """
    # 只保留近3天的更新（避免首次运行时历史内容太多；宽限时区差异）
    today = datetime.now()
    today_updates = []
    for u in all_updates:
        pub = u.get("published", "")
        if pub:
            try:
                pub_date = datetime.fromisoformat(pub[:10])
                if (today - pub_date).days <= 3:
                    today_updates.append(u)
            except Exception:
                today_updates.append(u)
        else:
            today_updates.append(u)

    display_updates = today_updates
    update_count = len(display_updates)
    if update_count == 0:
        return None

    # 页面文案
    if lang == "cn":
        page_title = f"{date_str} · 创作者动态"
        header_h1 = "👥 创作者动态"
        header_sub = "优质UP主 · YouTube频道 · X大V 最新内容追踪（中文版）"
        footer_text = "👤 fly的AI学习 · 每日更新 AI 大模型最新动态"
    else:
        page_title = f"{date_str} · Creator Updates"
        header_h1 = "👥 Creator Updates"
        header_sub = "Top AI YouTube Channels · X (Twitter) · B站 Creators"
        footer_text = "👤 fly的AI学习 · Daily AI & LLM Updates"

    platform_labels = {
        "youtube": ("▶️ YouTube", "#ff0000"),
        "bilibili": ("📺 B站", "#00a1d6"),
        "twitter": ("🐦 X(Twitter)", "#1da1f2"),
    }

    cards_html = ""
    for u in display_updates:
        p = u["platform"]
        label, color = platform_labels.get(p, (p, "#667eea"))
        thumb_html = f'<img src="{u["thumb"]}" alt="" style="width:100%;height:120px;object-fit:cover;border-radius:8px 8px 0 0;">' if u["thumb"] else ""
        dur_html = f'<span style="background:rgba(0,0,0,0.7);color:#fff;padding:2px 8px;border-radius:4px;font-size:11px;position:absolute;bottom:8px;right:8px;">{u["duration"]}</span>' if u["duration"] else ""
        link_text = "→ 查看详情"
        if p == "youtube":
            link_text = "▶️ 观看视频"
        elif p == "bilibili":
            link_text = "📺 B站观看"
        elif p == "twitter":
            link_text = "🐦 查看原推"

        card_thumb_wrapper = f'<div style="position:relative;">{thumb_html}{dur_html}</div>' if thumb_html or dur_html else ""

        cards_html += f'''
        <div class="update-card" style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:16px;overflow:hidden;transition:all 0.3s;">
            {card_thumb_wrapper}
            <div style="padding:20px;">
                <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
                    <span style="background:{color};color:#fff;font-size:12px;padding:3px 10px;border-radius:10px;font-weight:600;">{label}</span>
                    <span style="color:#888;font-size:12px;">{u["creator_name"]}</span>
                    <span style="color:#555;font-size:11px;">{u["creator_handle"]}</span>
                    {f'<span style="background:#4caf50;color:#fff;font-size:11px;padding:2px 8px;border-radius:8px;">译</span>' if u.get("original_title") else ""}
                </div>
                <h3 style="color:#fff;font-size:17px;margin-bottom:8px;line-height:1.4;">{u["title"]}</h3>
                {f'<p style="color:#666;font-size:11px;margin-bottom:10px;line-height:1.4;"><原文> {u["original_title"]}</p>' if u.get("original_title") else ""}
                <p style="color:#aaa;font-size:13px;line-height:1.7;margin-bottom:14px;">{u["summary"]}</p>
                <div style="display:flex;justify-content:space-between;align-items:center;">
                    <span style="color:#555;font-size:11px;">{u["published"][:10] if u["published"] else ""}</span>
                    <a href="{u["link"]}" target="_blank" style="color:{color};text-decoration:none;font-size:13px;font-weight:500;">{link_text} →</a>
                </div>
            </div>
        </div>'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{page_title}</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
<style>
* {{ margin:0;padding:0;box-sizing:border-box; }}
body {{
    font-family:'Noto Sans SC',-apple-system,BlinkMacSystemFont,sans-serif;
    background:linear-gradient(135deg,#0a0a1a 0%,#1a1a2e 50%,#16213e 100%);
    min-height:100vh;color:#e0e0e0;line-height:1.7;
}}
.container {{ max-width:1100px;margin:0 auto;padding:50px 24px; }}
.header {{ text-align:center;margin-bottom:50px; }}
.header .date-tag {{
    display:inline-block;background:linear-gradient(135deg,#667eea,#764ba2);
    color:#fff;padding:6px 20px;border-radius:20px;font-size:13px;font-weight:500;margin-bottom:16px;
}}
.header h1 {{
    font-size:38px;font-weight:900;
    background:linear-gradient(135deg,#fff,#a0a0ff);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
    margin-bottom:10px;
}}
.header .subtitle {{ color:#888;font-size:15px; }}
.update-count {{ text-align:center;margin-bottom:40px; }}
.count-badge {{
    display:inline-block;background:rgba(102,126,234,0.2);
    border:1px solid rgba(102,126,234,0.3);
    color:#8fa0ff;padding:8px 24px;border-radius:30px;font-size:14px;
}}
.grid {{ display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:20px; }}
.footer {{ text-align:center;padding:50px 0 30px;color:#555;font-size:12px; }}
.footer a {{ color:#667eea;text-decoration:none; }}
.update-card:hover {{ background:rgba(255,255,255,0.07);transform:translateY(-2px); }}
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
        <span class="count-badge">🔥 今日共 {update_count} 条更新</span>
    </div>
    <div class="grid">
        {cards_html}
    </div>
    <div class="footer">
        <p>{footer_text}</p>
    </div>
</div>
</body>
</html>'''
    return html


def main(date_str=None):
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")

    print(f"🤖 创作者更新监控  [{date_str}]")
    print("=" * 50)

    creators_data = load_creators()
    state = load_state()
    state["last_check"] = datetime.now().isoformat()

    all_new_items_cn = []  # 中文翻译版
    all_new_items_en = []  # 英文原版
    processed_count = 0

    # ── YouTube ──────────────────────────────────────────────
    yt_section = creators_data["platforms"]["youtube"]
    print(f"\n▶️  YouTube ({len(yt_section['creators'])} 个频道)")
    for creator in yt_section["creators"]:
        cid = YOUTUBE_CHANNEL_IDS.get(creator["id"], creator.get("channel_id", ""))
        if not cid:
            print(f"  ⚠️  无 channel_id: {creator['name']}")
            continue
        url = f"https://www.youtube.com/feeds/videos.xml?channel_id={cid}"
        print(f"  • {creator['name']} ...", end=" ")
        xml = http_get(url)
        videos = parse_youtube_rss(xml)
        new = check_new_items(creator, videos, state)
        if new:
            print(f"🆕 {len(new)}条新内容!")
            for v in new:
                all_new_items_cn.append(generate_interpretation(v, creator, date_str, "cn"))
                all_new_items_en.append(generate_interpretation(v, creator, date_str, "en"))
        else:
            print(f"无更新")
        processed_count += 1
        time.sleep(0.5)

    # ── Twitter ─────────────────────────────────────────────
    tw_section = creators_data["platforms"]["twitter"]
    print(f"\n🐦 X(Twitter) ({len(tw_section['creators'])} 个账号)")
    for creator in tw_section["creators"]:
        handle = creator.get("handle", "").lstrip("@")
        url = f"https://nitter.net/{handle}/rss"
        print(f"  • {creator['name']} ...", end=" ")
        xml = http_get(url)
        tweets = parse_nitter_rss(xml)
        new = check_new_items(creator, tweets, state)
        if new:
            print(f"🆕 {len(new)}条新推!")
            for t in new:
                all_new_items_cn.append(generate_interpretation(t, creator, date_str, "cn"))
                all_new_items_en.append(generate_interpretation(t, creator, date_str, "en"))
        else:
            print(f"无更新")
        processed_count += 1
        time.sleep(0.5)

    # ── B站 ─────────────────────────────────────────────────
    bili_section = creators_data["platforms"]["bilibili"]
    print(f"\n📺 B站 ({len(bili_section['creators'])} 个UP主)")
    for creator in bili_section["creators"]:
        uid = creator.get("uid", "")
        if not uid:
            print(f"  ⚠️  无 UID: {creator['name']}")
            continue
        print(f"  • {creator['name']} ...", end=" ")
        videos = fetch_bilibili_videos(uid, ps=5)
        if not videos:
            print("获取失败")
            continue
        new = check_new_items(creator, videos, state)
        if new:
            print(f"🆕 {len(new)}条新视频!")
            for v in new:
                all_new_items_cn.append(generate_interpretation(v, creator, date_str, "cn"))
                all_new_items_en.append(generate_interpretation(v, creator, date_str, "en"))
        else:
            print(f"无更新")
        processed_count += 1
        time.sleep(5)  # B站有频率限制，间隔大一些

    # ── 保存状态 ─────────────────────────────────────────────
    save_state(state)

    # ── 生成页面 ─────────────────────────────────────────────
    if all_new_items_cn:
        print(f"\n✅ 检测到 {len(all_new_items_cn)} 条新内容，正在生成页面...")
        # 中文版（默认）
        html_cn = render_updates_page(all_new_items_cn, date_str, "cn")
        if html_cn:
            cn_path = CREATORS_REPORT  # creator-updates.html
            with open(cn_path, "w", encoding="utf-8") as f:
                f.write(html_cn)
            print(f"📄 中文版: {cn_path}")
        # 英文原版
        html_en = render_updates_page(all_new_items_en, date_str, "en")
        if html_en:
            en_path = SKILL_DIR / "creator-updates-en.html"
            with open(en_path, "w", encoding="utf-8") as f:
                f.write(html_en)
            print(f"📄 英文版: {en_path}")
    else:
        print(f"\n😴 今日没有新增内容")

    print(f"\n共处理 {processed_count} 个创作者 | 状态已更新")
    return len(all_new_items_cn)


if __name__ == "__main__":
    import sys
    date_arg = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime("%Y-%m-%d")
    main(date_arg)
