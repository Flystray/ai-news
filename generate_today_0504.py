# -*- coding: utf-8 -*-
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
from datetime import datetime

date_str = datetime.now().strftime("%Y-%m-%d")

# 今日新闻数据（2026-05-04）
breaking_news = [
    {
        "title": "🔥 马斯克 OpenAI 庭审出庭：AI 可能是人类最后一项发明",
        "tag": "OpenAI 诉讼",
        "highlights": [
            "马斯克在奥克兰出庭作证，称 AI「既能让全人类繁荣，也可能带来毁灭性后果」",
            "庭审仅剩两项指控：OpenAI 违反慈善信托、不正当致富；Altman 曾私下称 GPT-4 是「惊悚」的",
            "马斯克警告：绝不希望迎来《终结者》式悲剧，AI 监管刻不容缓",
            "双方互揭老底：OpenAI 指马斯克曾想控制公司，Altman 被曝曾讨论「人类不可持续性」",
        ],
        "links": [
            {"url": "https://finance.sina.com.cn/world/2026-04-29/doc-inhwceiq7973181.shtml", "source": "新浪财经"},
            {"url": "https://www.ithome.com/0/941/780.htm", "source": "IT之家"},
        ]
    },
    {
        "title": "🔥 GPT-5.6 曝光：OpenAI 紧急封禁「哥布林怪癖」事件始末",
        "tag": "模型争议",
        "highlights": [
            "GPT-5.5 发布仅数日，开发者即在 Codex 后台日志中发现 GPT-5.6 偷跑痕迹",
            "新模型被发现对「哥布林」图像产生异常迷恋，API 日志出现大量相关请求",
            "OpenAI 紧急发布博客揭秘：系内部测试人员注入的风格引导提示词所致，非模型固有缺陷",
            "社区调侃：技术宅的「恶趣味」差点又成一场公关危机；GPT-5.6 正式版即将发布",
        ],
        "links": [
            {"url": "https://www.36kr.com/p/3789105348812037", "source": "36氪"},
            {"url": "https://news.qq.com/rain/a/20260424A07LIA00", "source": "腾讯新闻"},
        ]
    },
    {
        "title": "🔥 谷歌 400 亿美元豪赌 Anthropic：敌人的敌人是朋友",
        "tag": "战略投资",
        "highlights": [
            "谷歌承诺以 3800 亿美元估值投入 100 亿美元现金，后续追加 300 亿美元",
            "战略逻辑：与其用 Gemini 硬刚 Claude，不如把对手变成 TPU 最大买家",
            "Anthropic 年化收入一年暴涨 30 倍冲到 300 亿，云计算成最核心收入来源",
            "分析：AI 竞争进入「合纵连横」时代，资本绑定比技术竞争更有效",
        ],
        "links": [
            {"url": "https://finance.sina.com.cn/wm/2026-04-25/doc-inhvupep0114847.shtml", "source": "新浪财经"},
            {"url": "https://www.36kr.com/p/3784243425565953", "source": "36氪"},
        ]
    },
]

industry_news = [
    {
        "company": "DeepSeek",
        "tag": "V4 发布",
        "description": "DeepSeek V4 正式开源，支持 100 万 token 超长上下文，提供 V4-Pro 和 V4-Flash 预览版。识图模式疑似新模型架构，非思考模式响应速度极快，在编码和推理方面均有显著提升，开放权重供社区使用。",
        "links": [
            {"url": "https://www.qbitai.com/2026/05/412737.html", "source": "量子位"},
            {"url": "https://news.qq.com/rain/a/20260429A02Z0C00", "source": "腾讯新闻"},
        ]
    },
    {
        "company": "智谱 AI",
        "tag": "Scaling 瓶颈",
        "description": "智谱公布大模型「降智」的隐秘原因：随着模型规模增大，Scaling Law 面临不可避免的边际效益递减。文章揭示了预训练阶段数据质量、合成数据与模型能力之间的复杂权衡，引发行业对下一代训练范式的思考。",
        "links": [
            {"url": "https://www.qbitai.com/2026/05/412585.html", "source": "量子位"},
        ]
    },
    {
        "company": "华为 × 中科大",
        "tag": "具身智能",
        "description": "华为携手中科大发布「灵境造物」平台，以 openJiuwen 为底座，首发 Coordination Engineering 全栈解决方案，瞄准具身智能的物理世界交互难题，实现从仿真到真机部署的全链路支撑。",
        "links": [
            {"url": "https://www.qbitai.com/2026/05/412696.html", "source": "量子位"},
        ]
    },
    {
        "company": "Anthropic Claude",
        "tag": "设计工具",
        "description": "Claude Opus 4.7 发布，同步推出 Claude Design 对话式设计工具，支持视觉输出、原型设计和协作编辑，由最新 Opus 4.7 驱动，目前处于研究预览阶段，展示了 AI 在设计领域的新可能。",
        "links": [
            {"url": "https://support.claude.com/zh-CN/articles/12138966-%E5%8F%91%E5%B8%83%E8%AF%B4%E6%98%8E", "source": "Anthropic"},
            {"url": "https://zhuanlan.zhihu.com/p/2029634498711630707", "source": "知乎"},
        ]
    },
    {
        "company": "苹果",
        "tag": "乌龙事件",
        "description": "苹果官方 App 误打包了 Claude.md 内部文档，引发社区热议。这一「Vibe Coding」式失误显示 Claude 已深度渗透科技巨头日常工作流，也折射出 AI 工具融入工程流程中的安全管控盲区。",
        "links": [
            {"url": "https://www.qbitai.com/2026/05/412713.html", "source": "量子位"},
        ]
    },
    {
        "company": "阿里通义千问",
        "tag": "数字员工",
        "description": "阿里发布 QoderWake 数字员工产品，支持工程师、运营、销售等岗位角色定制，标志着 AI 从辅助工具升级为可独立承担业务流程的数字劳动力，企业级 AI Agent 应用进入主赛道。",
        "links": [
            {"url": "https://www.qbitai.com/", "source": "量子位"},
        ]
    },
    {
        "company": "国家电网",
        "tag": "具身大单",
        "description": "国家电网计划采购具身智能设备约 8500 台，总投资约 68 亿元，涵盖电力巡检、设备维护等场景，标志着具身智能从技术验证走向大规模商业化落地，2026 年正式开启规模化元年。",
        "links": [
            {"url": "https://news.qq.com/rain/a/20260429A02Z0C00", "source": "腾讯新闻"},
        ]
    },
    {
        "company": "GitHub",
        "tag": "1930 AI",
        "tag2": "程序员",
        "description": "GitHub Trending 出现「1930 年的 AI 抢程序员饭碗」话题，探讨 AI 编程工具对开发者职业未来的深远影响，引发技术社区对职业路径转型的广泛讨论。",
        "links": [
            {"url": "https://www.qbitai.com/2026/05/412896.html", "source": "量子位"},
        ]
    },
]

insights = [
    "【AI 监管从议题到行动】马斯克庭审将 AI 安全风险推至聚光灯下，各国监管机构加速立法，AI 治理框架竞争正式开始，谁能率先建立有效治理体系，谁就掌握了未来标准话语权。",
    "【Scaling Law 遭遇瓶颈】智谱「降智」揭秘和 DeepSeek V4 的性能取舍，显示大模型能力提升正面临边际效益递减，行业急需新范式突破，数据质量和训练方法创新成为新焦点。",
    "【开源与闭源进入新博弈】DeepSeek V4 开源 + 谷歌绑定 Anthropic，开源生态与资本联盟形成两条截然不同的路线，2026 年是两条路线真正正面交锋的元年。",
    "【具身智能规模化落地】华为灵境造物 + 国家电网 68 亿大单 + 新一代仿真框架开源，具身智能从实验室走向工厂，从 demo 走向可复制的商业产品，2026 是规模化元年。",
    "【AI 原住民代际更替】苹果打包 Claude 文档、村口吵架式庭审、GPT-5.6 哥布林怪癖——AI 已深度嵌入科技从业者日常，新的「AI 原住民」思维方式正在重塑整个产业。",
]

news_items = {
    "breaking_news": breaking_news,
    "industry_news": industry_news,
    "insights": insights,
    "sources": ["OpenAI", "Anthropic", "Google", "DeepSeek", "智谱AI", "量子位", "36氪", "新浪财经", "机器之心"],
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
        .news-card h3 {{ font-size: 20px; font-weight: 700; color: #fff; margin-bottom: 12px; display: flex; align-items: flex-start; gap: 10px; flex-wrap: wrap; }}
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
                            <h3>${{item.company}} <span class="tag">${{item.tag}}</span>${{item.tag2 ? `<span class="tag">${{item.tag2}}</span>` : ''}}</h3>
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

import os
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports")
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, f"{date_str}-with-links.html")
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✅ 报告已保存: {output_file}")
