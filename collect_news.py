"""
AI新闻采集与报告生成工具
使用方法: python collect_news.py
"""

import requests
import json
import os
from datetime import datetime

# ============ 新闻源配置 ============
NEWS_SOURCES = {
    "通义千问": {
        "search": "阿里 通义千问 Qwen 发布 2026",
        "urls": [
            ("OSCHINA", "https://www.oschina.net/news/list?catalog=4231"),
            ("AI前线", "https://mp.weixin.qq.com/s?__biz=MzU0NTA0NTgzOA=="),
        ]
    },
    "谷歌AI": {
        "search": "Google AI DeepMind 最新 2026",
        "urls": [
            ("谷歌博客", "https://blog.google/technology/ai/"),
            ("DeepMind", "https://deepmind.google/discover/blog/"),
        ]
    },
    "OpenAI": {
        "search": "OpenAI GPT 发布 2026",
        "urls": [
            ("OpenAI博客", "https://openai.com/blog"),
            ("OpenAI新闻", "https://openai.com/news/"),
        ]
    },
    "Anthropic": {
        "search": "Anthropic Claude 发布 2026",
        "urls": [
            ("Anthropic博客", "https://www.anthropic.com/news"),
            ("Anthropic研究", "https://www.anthropic.com/research"),
        ]
    },
    "国内AI": {
        "search": "DeepSeek 文心一言 通义千问 Kimi 秘塔 智谱 最新 2026",
        "urls": [
            ("量子位", "https://www.qbitai.com/"),
            ("机器之心", "https://jiqizhixin.com/"),
            ("AI前线", "https://mp.weixin.qq.com/s?__biz=MzU0NTA0NTgzOA=="),
        ]
    },
    "开源项目": {
        "search": "GitHub AI 开源 新项目 2026",
        "urls": [
            ("GitHub Trending", "https://github.com/trending"),
            ("Hugging Face", "https://huggingface.co/models"),
        ]
    }
}

# ============ 搜索API配置 ============
# 使用 DuckDuckGo Lite (无需API Key)
DUCKDUCKGO_URL = "https://lite.duckduckgo.com/50x.js"

def search_news(query, max_results=5):
    """使用Google搜索获取新闻"""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        # 使用serpapi或直接搜索
        url = f"https://www.google.com/search?q={query}&tbm=nws&num={max_results}"
        response = requests.get(url, headers=headers, timeout=10)
        
        results = []
        # 简单解析（实际项目中建议使用BeautifulSoup）
        if response.status_code == 200:
            # 返回搜索URL供后续手动访问
            results.append({
                "title": f"Google搜索: {query}",
                "url": url,
                "source": "Google News"
            })
        return results
    except Exception as e:
        print(f"搜索失败: {e}")
        return []

def generate_report_template(news_items, date_str):
    """生成HTML报告模板"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{date_str} AI 每日资讯</title>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700;900&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Noto Sans SC', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #16213e 100%);
            min-height: 100vh;
            color: #e0e0e0;
            line-height: 1.8;
        }}
        .container {{ max-width: 1000px; margin: 0 auto; padding: 40px 20px; }}
        .header {{ text-align: center; margin-bottom: 50px; }}
        .header .date {{
            display: inline-block;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white; padding: 8px 24px;
            border-radius: 30px; font-size: 14px; font-weight: 500;
            margin-bottom: 20px;
        }}
        .header h1 {{
            font-size: 42px; font-weight: 900;
            background: linear-gradient(135deg, #fff, #a0a0ff);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            margin-bottom: 15px;
        }}
        .header .subtitle {{ color: #888; font-size: 16px; }}
        .section {{ margin-bottom: 50px; }}
        .section-title {{
            display: flex; align-items: center; gap: 12px;
            font-size: 24px; font-weight: 700; margin-bottom: 25px; color: #fff;
        }}
        .news-card {{
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 20px; padding: 28px; margin-bottom: 20px;
            transition: all 0.3s ease;
        }}
        .news-card:hover {{
            background: rgba(255,255,255,0.06);
            border-color: rgba(102,126,234,0.3);
            transform: translateY(-2px);
        }}
        .news-card h3 {{
            font-size: 20px; font-weight: 700; color: #fff;
            margin-bottom: 12px; display: flex; align-items: flex-start; gap: 10px;
        }}
        .news-card h3 .tag {{
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white; font-size: 11px; padding: 4px 10px;
            border-radius: 12px; font-weight: 500; white-space: nowrap; margin-top: 4px;
        }}
        .news-card p {{ color: #aaa; margin-bottom: 15px; font-size: 15px; }}
        .news-card ul {{
            background: rgba(102,126,234,0.1);
            border-radius: 12px; padding: 16px 20px; margin-bottom: 15px;
            list-style: none;
        }}
        .news-card ul li {{
            color: #d0d0ff; margin-bottom: 8px; padding-left: 20px; position: relative; font-size: 14px;
        }}
        .news-card ul li::before {{ content: "•"; position: absolute; left: 0; color: #667eea; }}
        .news-card ul li:last-child {{ margin-bottom: 0; }}
        .news-card .links {{ display: flex; flex-wrap: wrap; gap: 12px; margin-top: 12px; }}
        .news-card .link {{
            display: inline-flex; align-items: center; gap: 6px;
            color: #667eea; text-decoration: none; font-size: 14px; font-weight: 500;
        }}
        .news-card .link:hover {{ color: #8fa0ff; text-decoration: underline; }}
        .footer {{
            text-align: center; padding: 40px 0; color: #666; font-size: 13px;
        }}
        .footer a {{ color: #667eea; text-decoration: none; }}
        .footer a:hover {{ text-decoration: underline; }}
        .insight-item {{
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 14px; padding: 20px 24px;
            display: flex; align-items: flex-start; gap: 16px; margin-bottom: 16px;
        }}
        .insight-item .num {{
            width: 32px; height: 32px; border-radius: 10px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white; display: flex; align-items: center; justify-content: center;
            font-weight: 700; font-size: 14px; flex-shrink: 0;
        }}
        .insight-item p {{ color: #ccc; font-size: 15px; margin-top: 4px; }}
        .refresh-btn {{
            position: fixed; bottom: 30px; right: 30px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white; border: none; padding: 14px 24px;
            border-radius: 30px; font-size: 14px; font-weight: 500;
            cursor: pointer; box-shadow: 0 4px 20px rgba(102,126,234,0.4);
            transition: all 0.3s ease;
        }}
        .refresh-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 25px rgba(102,126,234,0.5);
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="date">📅 {date_str}</div>
            <h1>📰 AI 每日资讯</h1>
            <p class="subtitle">精选每日 AI / 大模型最新动态 · 所有新闻均带原文链接</p>
        </div>
        
        <div id="news-content">
            <!-- 新闻内容将通过JavaScript动态加载 -->
            <div style="text-align:center;padding:50px;color:#888;">
                正在加载新闻...
            </div>
        </div>
        
        <button class="refresh-btn" onclick="location.reload()">🔄 刷新新闻</button>
    </div>
    
    <script>
        const newsData = {json.dumps(news_items, ensure_ascii=False, indent=2)};
        
        function renderNews() {{
            const container = document.getElementById('news-content');
            
            let html = `
                <div class="section">
                    <h2 class="section-title"><span>🔥</span> 今日重大突破</h2>
            `;
            
            // 渲染新闻卡片
            newsData.breaking_news.forEach(news => {{
                html += `
                    <div class="news-card">
                        <h3>${{news.title}} <span class="tag">${{news.tag}}</span></h3>
                        <ul>
                            ${{news.highlights.map(h => `<li>${{h}}</li>`).join('')}}
                        </ul>
                        <div class="links">
                            ${{news.links.map(l => `<a href="${{l.url}}" target="_blank" class="link">📌 ${{l.source}} →</a>`).join('')}}
                        </div>
                    </div>
                `;
            }});
            
            html += `</div>`;
            
            // 渲染行业动态
            if (newsData.industry_news && newsData.industry_news.length > 0) {{
                html += `
                    <div class="section">
                        <h2 class="section-title"><span>🏆</span> 行业动态</h2>
                        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;">
                `;
                
                newsData.industry_news.forEach(item => {{
                    html += `
                        <div class="news-card">
                            <h3>${{item.company}} <span class="tag">${{item.tag}}</span></h3>
                            <p>${{item.description}}</p>
                            <div class="links">
                                ${{item.links.map(l => `<a href="${{l.url}}" target="_blank" class="link">📌 ${{l.source}}</a>`).join('')}}
                            </div>
                        </div>
                    `;
                }});
                
                html += `</div></div>`;
            }}
            
            // 渲染核心洞察
            if (newsData.insights && newsData.insights.length > 0) {{
                html += `
                    <div class="section">
                        <h2 class="section-title"><span>💡</span> 核心洞察</h2>
                `;
                
                newsData.insights.forEach((insight, i) => {{
                    html += `
                        <div class="insight-item">
                            <div class="num">${{i + 1}}</div>
                            <p>${{insight}}</p>
                        </div>
                    `;
                }});
                
                html += `</div>`;
            }}
            
            // 页脚
            html += `
                <div class="footer">
                    <p>📡 数据来源：${{newsData.sources ? newsData.sources.join(' · ') : '多方采集'}}</p>
                    <p style="margin-top:10px;">🔗 所有链接均可点击访问原文 · 最后更新: ${{newsData.updated}}</p>
                </div>
            `;
            
            container.innerHTML = html;
        }}
        
        renderNews();
    </script>
</body>
</html>'''
    return html

def main():
    print("🤖 AI新闻采集工具")
    print("=" * 50)
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_dir = r"c:\Users\Administrator\Desktop\yf-data\reports"
    
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"\n📅 当前日期: {date_str}")
    print("\n🔍 开始采集新闻...")
    
    # 采集各平台新闻
    all_news = {"breaking_news": [], "industry_news": [], "insights": [], "sources": []}
    
    for source_name, config in NEWS_SOURCES.items():
        print(f"  • 采集 {source_name}...")
        results = search_news(config["search"])
        for r in results:
            if r.get("url"):
                all_news["sources"].append(r.get("source", source_name))
    
    print(f"\n✅ 采集完成，共获取 {len(all_news['sources'])} 个来源")
    
    # 生成报告
    output_file = os.path.join(output_dir, f"{date_str}-with-links.html")
    report_html = generate_report_template(all_news, date_str)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report_html)
    
    print(f"\n📄 报告已生成: {output_file}")
    print("\n💡 请打开文件查看新闻报道")

if __name__ == "__main__":
    main()
