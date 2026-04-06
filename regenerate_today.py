# -*- coding: utf-8 -*-
"""
独立脚本：重新拉取近3天 Twitter 推文并生成 creator-updates.html
不修改 creator_state.json，不依赖 creator_monitor 模块导入
"""
import json, ssl, time, re, hashlib
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from pathlib import Path

try:
    from deep_translator import GoogleTranslator
    TRANSLATOR = GoogleTranslator(source='en', target='zh-CN')
    HAS_TRANSLATOR = True
except Exception:
    HAS_TRANSLATOR = False

_trans_cache = {}

SKILL_DIR = Path(r"C:\Users\YF\.workbuddy\skills\ai-news")
CREATORS_FILE = SKILL_DIR / "creators.json"
CREATORS_REPORT = SKILL_DIR / "creator-updates.html"

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/rss+xml, application/xml, text/html, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

DATE_STR = datetime.now().strftime("%Y-%m-%d")
CUTOFF = datetime.now() - timedelta(days=3)


def http_get(url, timeout=12):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        resp = urllib.request.urlopen(req, timeout=timeout, context=CTX)
        return resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"    [ERR] {str(e)[:80]}")
        return None


def parse_nitter_rss(xml_text):
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
            desc = item.findtext("description", "")
            desc = re.sub(r'<[^>]+>', '', desc)
            desc = desc.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
            t["desc"] = desc.strip()
            t["thumb"] = ""
            t["duration"] = ""
            t["platform"] = "twitter"
            tweets.append(t)
        return tweets
    except Exception as e:
        print(f"    [XML ERR] {e}")
        return []


def is_foreign_text(text):
    if not text:
        return False
    cjk = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
    return (cjk / max(len(text), 1)) < 0.1


def translate_text(text):
    if not text or not HAS_TRANSLATOR:
        return text
    key = hashlib.md5(text.encode()).hexdigest()[:8]
    if key in _trans_cache:
        return _trans_cache[key]
    try:
        result = TRANSLATOR.translate(text[:500])
        _trans_cache[key] = result
        return result
    except Exception:
        return text


def generate_card(item, creator, lang="cn"):
    platform = item["platform"]
    title = item.get("title", "无标题")
    desc = item.get("desc", "")
    link = item.get("link", "")
    thumb = item.get("thumb", "")

    if lang == "cn" and is_foreign_text(title):
        title_cn = translate_text(title)
        print(f"    [翻译] {title[:40]} => {title_cn[:40]}")
        original_title = title
    else:
        title_cn = title
        original_title = None

    if lang == "cn" and is_foreign_text(desc):
        summary_cn = translate_text(desc[:300])
    else:
        summary_cn = desc[:300] + ("..." if len(desc) > 300 else "")

    pub = item.get("published", "")
    # 标准化发布日期
    pub_date = ""
    if pub:
        try:
            for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S %Z"):
                try:
                    dt = datetime.strptime(pub, fmt)
                    pub_date = dt.strftime("%Y-%m-%d")
                    break
                except:
                    pass
            if not pub_date:
                pub_date = pub[:10]
        except:
            pub_date = pub[:10]

    return {
        "platform": platform,
        "creator_name": creator["name"],
        "creator_handle": creator.get("handle", ""),
        "title": title_cn,
        "original_title": original_title,
        "summary": summary_cn or "点击查看详细内容",
        "link": link,
        "thumb": thumb,
        "published": pub_date,
        "duration": item.get("duration", ""),
        "color": "#1da1f2",
    }


def render_page(cards, date_str, lang="cn"):
    if not cards:
        return None
    if lang == "cn":
        page_title = f"{date_str} · 创作者动态"
        header_h1 = "👥 创作者动态"
        header_sub = "X大V · YouTube · B站 最新内容追踪（中文版）"
    else:
        page_title = f"{date_str} · Creator Updates"
        header_h1 = "👥 Creator Updates"
        header_sub = "Twitter / X · YouTube · Bilibili"

    platform_labels = {
        "youtube": ("▶️ YouTube", "#ff0000"),
        "bilibili": ("📺 B站", "#00a1d6"),
        "twitter": ("🐦 X(Twitter)", "#1da1f2"),
    }

    cards_html = ""
    for u in cards:
        p = u["platform"]
        label, color = platform_labels.get(p, (p, "#667eea"))
        thumb_html = (f'<img src="{u["thumb"]}" alt="" style="width:100%;height:120px;object-fit:cover;border-radius:8px 8px 0 0;">'
                      if u["thumb"] else "")
        link_text = "🐦 查看原推 →" if p == "twitter" else "→ 查看详情"

        cards_html += f'''
        <div class="card">
            {f'<div style="position:relative;">{thumb_html}</div>' if thumb_html else ""}
            <div style="padding:20px;">
                <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;flex-wrap:wrap;">
                    <span style="background:{color};color:#fff;font-size:12px;padding:3px 10px;border-radius:10px;font-weight:600;">{label}</span>
                    <span style="color:#888;font-size:13px;">{u["creator_name"]}</span>
                    <span style="color:#555;font-size:11px;">{u["creator_handle"]}</span>
                    {f'<span style="background:#4caf50;color:#fff;font-size:11px;padding:2px 8px;border-radius:8px;">译</span>' if u.get("original_title") else ""}
                </div>
                <h3 style="color:#fff;font-size:16px;margin-bottom:8px;line-height:1.5;">{u["title"]}</h3>
                {f'<p style="color:#555;font-size:11px;margin-bottom:10px;">&lt;原文&gt; {u["original_title"]}</p>' if u.get("original_title") else ""}
                <p style="color:#aaa;font-size:13px;line-height:1.7;margin-bottom:14px;">{u["summary"]}</p>
                <div style="display:flex;justify-content:space-between;align-items:center;">
                    <span style="color:#555;font-size:11px;">{u["published"]}</span>
                    <a href="{u["link"]}" target="_blank" style="color:{color};text-decoration:none;font-size:13px;">{link_text}</a>
                </div>
            </div>
        </div>'''

    count = len(cards)
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{page_title}</title>
<style>
  *{{box-sizing:border-box;margin:0;padding:0;}}
  body{{background:#0d1117;color:#e6edf3;font-family:'Segoe UI',sans-serif;min-height:100vh;}}
  .header{{background:linear-gradient(135deg,#1a1f35 0%,#0d1117 100%);padding:40px 20px;text-align:center;border-bottom:1px solid rgba(255,255,255,0.08);}}
  .header h1{{font-size:32px;margin-bottom:8px;}}
  .header p{{color:#8b949e;font-size:14px;}}
  .badge{{background:rgba(29,161,242,0.2);color:#1da1f2;padding:4px 14px;border-radius:12px;font-size:13px;margin-top:12px;display:inline-block;}}
  .container{{max-width:1200px;margin:40px auto;padding:0 20px;}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:20px;}}
  .card{{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:16px;overflow:hidden;transition:transform 0.2s,box-shadow 0.2s;}}
  .card:hover{{transform:translateY(-4px);box-shadow:0 8px 30px rgba(0,0,0,0.4);}}
  .footer{{text-align:center;padding:40px 20px;color:#555;font-size:13px;border-top:1px solid rgba(255,255,255,0.05);margin-top:40px;}}
</style>
</head>
<body>
<div class="header">
  <h1>{header_h1}</h1>
  <p>{header_sub}</p>
  <div class="badge">📅 {date_str} &nbsp;|&nbsp; 共 {count} 条更新</div>
</div>
<div class="container">
  <div class="grid">{cards_html}</div>
</div>
<div class="footer">👤 fly的AI学习 · 每日更新 AI 大模型最新动态</div>
</body>
</html>'''


def log(msg):
    """输出不含 emoji 的日志（避免 GBK 编码错误）"""
    try:
        print(msg)
    except UnicodeEncodeError:
        import unicodedata
        clean = ''.join(c if unicodedata.category(c)[0] != 'S' else '?' for c in msg)
        print(clean)


def main():
    with open(CREATORS_FILE, encoding="utf-8") as f:
        creators_data = json.load(f)

    all_cn = []
    all_en = []

    tw_section = creators_data["platforms"]["twitter"]
    log(f"[Twitter] 拉取 {len(tw_section['creators'])} 个账号 (近3天内容)")
    for creator in tw_section["creators"]:
        handle = creator.get("handle", "").lstrip("@")
        url = f"https://nitter.net/{handle}/rss"
        log(f"  {creator['name']} ...")
        xml = http_get(url)
        tweets = parse_nitter_rss(xml)
        recent = []
        for t in tweets:
            pub = t.get("published", "")
            if pub:
                try:
                    for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S %Z"):
                        try:
                            dt = datetime.strptime(pub, fmt).replace(tzinfo=None)
                            if dt >= CUTOFF:
                                recent.append(t)
                            break
                        except:
                            pass
                    else:
                        recent.append(t)
                except:
                    recent.append(t)
            else:
                recent.append(t)
        log(f"    -> {len(recent)} 条近期推文")
        for t in recent:
            all_cn.append(generate_card(t, creator, "cn"))
            all_en.append(generate_card(t, creator, "en"))
        time.sleep(0.5)

    log(f"\n[合计] {len(all_cn)} 条近期推文")
    if all_cn:
        log("[生成] 中文版 HTML ...")
        html_cn = render_page(all_cn, DATE_STR, "cn")
        if html_cn:
            CREATORS_REPORT.write_text(html_cn, encoding="utf-8")
            log(f"[OK] 已生成: {CREATORS_REPORT}")
        html_en = render_page(all_en, DATE_STR, "en")
        if html_en:
            en_path = SKILL_DIR / "creator-updates-en.html"
            en_path.write_text(html_en, encoding="utf-8")
            log(f"[OK] 已生成: {en_path}")
    else:
        log("[无内容] 没有近期推文，未生成文件")


if __name__ == "__main__":
    main()
