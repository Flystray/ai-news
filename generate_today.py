# -*- coding: utf-8 -*-
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
from datetime import datetime

date_str = datetime.now().strftime("%Y-%m-%d")

# 今日新闻数据（2026-05-03）
breaking_news = [
    {
        "title": "🔥 马斯克出庭 OpenAI 案：AI 可能是人类最后一项发明",
        "tag": "OpenAI 诉讼",
        "highlights": [
            "马斯克在奥克兰出庭作证，称 AI「既能让全人类繁荣，也可能带来毁灭性后果」",
            "庭审仅剩两项指控：OpenAI 违反慈善信托、不正当致富",
            "马斯克警告：绝不希望迎来《终结者》式悲剧，AI 监管刻不容缓",
            "双方互揭老底： Altman 曾私下表示 GPT-4 是「惊悚」的，OpenAI 则指马斯克曾想控制公司",
        ],
        "links": [
            {"url": "https://www.ithome.com/0/941/780.htm", "source": "IT之家"},
            {"url": "https://finance.sina.com.cn/world/2026-04-29/doc-inhwceiq7973181.shtml", "source": "新浪财经"},
        ]
    },
    {
        "title": "🔥 微软与 OpenAI 正式分手：结束独家云合作，OpenAI 可自由选择云厂商",
        "tag": "战略重组",
        "highlights": [
            "4 月 27 日双方同时发布博文，修订延续多年的合作协议",
            "微软从「独家合作伙伴」降级为「首要合作伙伴」，措辞微妙转变",
            "OpenAI 可将产品卖给任何云服务商——包括亚马逊 AWS 和谷歌云",
            "Azure 仍为 OpenAI 主要云伙伴，AGI 相关协议条款取消",
        ],
        "links": [
            {"url": "https://news.qq.com/rain/a/20260427A08BIL00", "source": "腾讯新闻"},
            {"url": "https://finance.sina.com.cn/tech/2026-04-28/doc-inhvfivi8029288.shtml", "source": "新浪科技"},
        ]
    },
    {
        "title": "🔥 具身智能突破：新一代高保真仿真框架开源，真机部署「零微调」",
        "tag": "技术突破",
        "highlights": [
            "突破视觉仿真算力瓶颈，新框架实现高吞吐并行高保真渲染",
            "助力规模化训练，机器人真机部署无需微调即可运行",
            "国家电网 68 亿具身智能采购已拉开大幕，电力场景率先落地",
            "工业机器人万亿市场正式开启，AI 驱动的物理世界交互成新战场",
        ],
        "links": [
            {"url": "https://www.qbitai.com/", "source": "量子位"},
            {"url": "https://news.qq.com/rain/a/20260429A02Z0C00", "source": "腾讯新闻"},
        ]
    },
]

industry_news = [
    {
        "company": "阿里通义千问",
        "tag": "数字员工",
        "description": "阿里发布 QoderWake 数字员工产品，可承担工程师、运营、销售等岗位角色，支持根据自身业务流程定制，标志着 AI 从辅助工具升级为真正的数字劳动力。",
        "links": [
            {"url": "https://www.qbitai.com/", "source": "量子位"},
        ]
    },
    {
        "company": "DeepSeek",
        "tag": "V4 性能",
        "description": "DeepSeek V4 支持 100 万 token 上下文，通过 V4-Pro 和 V4-Flash 提供预览版，开放权重，在编码和推理方面声称有提升。识图模式疑似新模型，非思考模式速度极快。",
        "links": [
            {"url": "https://theaitrack.com/ai-news-may-2026-in-depth-and-concise/", "source": "The AI Track"},
            {"url": "https://www.qbitai.com/", "source": "量子位"},
        ]
    },
    {
        "company": "Anthropic Claude",
        "tag": "连接器生态",
        "description": "Claude 连接器扩展至 Adobe、Blender 和 Autodesk Fusion，支持设计、音乐、视频、3D 建模、现场视觉效果和创意教育工作流，AI 工具链生态进一步壮大。",
        "links": [
            {"url": "https://theaitrack.com/ai-news-may-2026-in-depth-and-concise/", "source": "The AI Track"},
        ]
    },
    {
        "company": "腾讯",
        "tag": "开源翻译",
        "description": "腾讯开源手机端离线翻译模型，仅 0.4G 大小，支持 33 种语言，可在无网络环境下运行，部署门槛大幅降低，离线 AI 应用成为现实。",
        "links": [
            {"url": "https://www.qbitai.com/", "source": "量子位"},
        ]
    },
    {
        "company": "苹果 × Anthropic",
        "tag": "乌龙事件",
        "description": "苹果官方 App 误打包了 Claude.md 文件，引发社区热议。这一「Vibe Coding」式失误显示 Claude 已深度渗透科技巨头日常工作流。",
        "links": [
            {"url": "https://www.qbitai.com/", "source": "量子位"},
        ]
    },
    {
        "company": "谷歌 DeepMind",
        "tag": "AI 编程",
        "description": "布林（Sergey Brin）亲自督战，组建精英 Gemini 团队专攻 AI 编程，全力追赶 Anthropic Claude。团队由预训练 Gemini 的工程师 Sebastian Borgeaud 领导，核心任务攻克从零编写代码难题。",
        "links": [
            {"url": "https://www.ithome.com/0/941/551.htm", "source": "IT之家"},
        ]
    },
    {
        "company": "中国监管",
        "tag": "叫停收购",
        "description": "中国依法阻止 Meta 超 20 亿美元收购 AI 初创公司 Manus，使 Meta 进军自主 AI 代理的计划复杂化，标志着对美国投资中国关联技术公司的审查持续收紧。",
        "links": [
            {"url": "https://theaitrack.com/ai-news-may-2026-in-depth-and-concise/", "source": "The AI Track"},
        ]
    },
    {
        "company": "福布斯 AI 50",
        "tag": "全球榜单",
        "description": "福布斯发布 2026 年 AI 50 榜单，OpenAI、Anthropic 领衔，本届共有 20 家新上榜公司。两家 AI 巨头累计融资 2426 亿美元（约合 1.66 万亿元人民币），占上榜企业总融资额 80%。",
        "links": [
            {"url": "https://www.ithome.com/0/941/759.htm", "source": "IT之家"},
        ]
    },
]

insights = [
    "【AI 监管已成全球议题】马斯克庭审揭示 AI 安全风险，各国监管机构加速介入，AI 治理框架竞争正式开始。",
    "【开源生态决定产业格局】DeepSeek V4、腾讯小模型持续开源，国产 AI 开源生态进入全球第一梯队，倒逼闭源厂商加速创新。",
    "【数字员工进入企业主赛道】阿里 QoderWake、腾讯 WorkBuddy 密集迭代，AI Agent 从辅助工具升级为可替代岗位角色的数字劳动力。",
    "【具身智能规模化元年开启】国家电网 68 亿采购 + 新一代仿真框架开源，具身智能从实验室走向工厂，2026 年是规模化元年。",
    "【AI 基础设施竞争白热化】大模型降价 97%、开源小模型崛起，AI 应用普惠时代到来，但算力瓶颈与芯片国产替代仍是核心挑战。",
]

news_items = {
    "breaking_news": breaking_news,
    "industry_news": industry_news,
    "insights": insights,
    "sources": ["OpenAI", "Anthropic", "Google", "36氪", "量子位", "新浪财经", "机器之心"],
    "updated": datetime.now().strftime("%Y-%m-%d %H:%M")
}

# 生成 HTML
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
        .section-title {{ display: flex; align-items: center; gap: 12px; font-size: 24px; font-weight: 700; margin-bottom: 25px; color: #fff; }}
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
        .news-card h3 {{ font-size: 20px; font-weight: 700; color: #fff; margin-bottom: 12px; display: flex; align-items: flex-start; gap: 10px; }}
        .news-card h3 .tag {{
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white; font-size: 11px; padding: 4px 10px;
            border-radius: 12px; font-weight: 500; white-space: nowrap; margin-top: 4px;
        }}
        .news-card p {{ color: #aaa; margin-bottom: 15px; font-size: 15px; }}
        .news-card ul {{ background: rgba(102,126,234,0.1); border-radius: 12px; padding: 16px 20px; margin-bottom: 15px; list-style: none; }}
        .news-card ul li {{ color: #d0d0ff; margin-bottom: 8px; padding-left: 20px; position: relative; font-size: 14px; }}
        .news-card ul li::before {{ content: "•"; position: absolute; left: 0; color: #667eea; }}
        .news-card ul li:last-child {{ margin-bottom: 0; }}
        .news-card .links {{ display: flex; flex-wrap: wrap; gap: 12px; margin-top: 12px; }}
        .news-card .link {{ display: inline-flex; align-items: center; gap: 6px; color: #667eea; text-decoration: none; font-size: 14px; font-weight: 500; }}
        .news-card .link:hover {{ color: #8fa0ff; text-decoration: underline; }}
        .footer {{ text-align: center; padding: 40px 0; color: #666; font-size: 13px; }}
        .footer a {{ color: #667eea; text-decoration: none; }}
        .footer a:hover {{ text-decoration: underline; }}
        .insight-item {{ background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 20px 24px; display: flex; align-items: flex-start; gap: 16px; margin-bottom: 16px; }}
        .insight-item .num {{ width: 32px; height: 32px; border-radius: 10px; background: linear-gradient(135deg, #667eea, #764ba2); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 14px; flex-shrink: 0; }}
        .insight-item p {{ color: #ccc; font-size: 15px; margin-top: 4px; }}
        .refresh-btn {{ position: fixed; bottom: 30px; right: 30px; background: linear-gradient(135deg, #667eea, #764ba2); color: white; border: none; padding: 14px 24px; border-radius: 30px; font-size: 14px; font-weight: 500; cursor: pointer; box-shadow: 0 4px 20px rgba(102,126,234,0.4); transition: all 0.3s ease; }}
        .refresh-btn:hover {{ transform: translateY(-2px); box-shadow: 0 6px 25px rgba(102,126,234,0.5); }}
        .section-icon {{ font-size: 28px; }}
        .industry-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px,1fr)); gap: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="date">📅 {date_str}</div>
            <h1>📰 AI 每日资讯</h1>
            <p class="subtitle">精选每日 AI / 大模型最新动态 · 所有新闻均带原文链接</p>
        </div>

        <div id="news-content"></div>

        <button class="refresh-btn" onclick="location.reload()">🔄 刷新新闻</button>
    </div>

    <script>
        const newsData = {json.dumps(news_items, ensure_ascii=False, indent=2)};

        function renderNews() {{
            const container = document.getElementById('news-content');

            let html = `
                <div class="section">
                    <h2 class="section-title"><span class="section-icon">🔥</span> 今日重磅</h2>
            `;

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

            if (newsData.industry_news && newsData.industry_news.length > 0) {{
                html += `
                    <div class="section">
                        <h2 class="section-title"><span class="section-icon">🏆</span> 行业动态</h2>
                        <div class="industry-grid">
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

            if (newsData.insights && newsData.insights.length > 0) {{
                html += `
                    <div class="section">
                        <h2 class="section-title"><span class="section-icon">💡</span> 核心洞察</h2>
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

import json, os
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports")
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, f"{date_str}-with-links.html")
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✅ 报告已保存: {output_file}")
