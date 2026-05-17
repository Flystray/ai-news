# -*- coding: utf-8 -*-
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
from datetime import datetime

date_str = datetime.now().strftime("%Y-%m-%d")

# 今日新闻数据（2026-05-17）
breaking_news = [
    {
        "title": "🔥 GPT-5.6 曝光：下月发布！OpenAI 内部测试已启动，1.5M 超长上下文实测可跑通",
        "tag": "OpenAI 重磅",
        "highlights": [
            "GPT-5.5 发布仅三周，GPT-5.6 开发进度已全速推进，内部测试代码被知名爆料人 Leo 泄露",
            "OpenAI Codex 日志中惊现 rollout mapping 痕迹，部分调用已悄然路由至 GPT-5.6",
            "用户通过 ChatGPT Pro 的 OAuth 认证，已成功在 Codex 环境中调用尚未发布的 gpt-5.6 模型",
            "1.5M token 超长上下文已能跑通，Codex ultrafast 模式主力推理速度提升 2-3 倍",
        ],
        "links": [
            {"url": "https://www.36kr.com/p/3808515686309377", "source": "36氪"},
            {"url": "https://www.itbear.com.cn/html/2026-05/1339410.html", "source": "ITBear"},
            {"url": "https://www.chinaz.com/ainews/27986.shtml", "source": "站长之家"},
        ]
    },
    {
        "title": "🔥 无锡 Token 工厂启动：首批 4 台华为昇腾 384 超节点，国产算力再下一城",
        "tag": "国产算力",
        "highlights": [
            "弘信电子与无锡高新区合作建立大规模 Token 工厂，首批部署 4 台华为昇腾 384 超节点服务器",
            "每套超节点拥有 384 卡算力，目标是打造「国芯国模」规模化高性能算力集群新样板",
            "阿里平头哥自研 GPU 同步规模化量产，台积电预计 2030 年全球芯片市场达 1.5 万亿美元",
            "摩尔线程与国家具身智能应用中试基地签约，成立「具身智能算力与仿真联合实验室」",
        ],
        "links": [
            {"url": "https://www.ithome.com/", "source": "IT之家"},
            {"url": "https://maomu.com/news", "source": "猫目AI"},
        ]
    },
    {
        "title": "🔥 AI 融资格局重塑：贝索斯新公司估值 380 亿美元，Anthropic 寻求 9000 亿美元融资",
        "tag": "融资战报",
        "highlights": [
            "贝索斯新 AI 公司募资说明书首度曝光，估值达 380 亿美元（约 2750 亿元人民币）",
            "Anthropic 正以 9000 亿美元估值寻求至少 300 亿美元融资，刷新 AI 领域融资纪录",
            "阶跃星辰完成 25 亿美元融资，腾讯跟投并达成战略合作，国产大模型融资持续升温",
            "AI 芯片年度最大 IPO 冲刺：估值约 3800 亿元人民币，矛头直指英伟达",
        ],
        "links": [
            {"url": "https://maomu.com/news", "source": "猫目AI"},
            {"url": "https://www.36kr.com/", "source": "36氪"},
        ]
    },
    {
        "title": "🔥 OpenAI vs Anthropic 补贴大战开打：AI 编程市场争夺进入白热化",
        "tag": "AI 编程",
        "highlights": [
            "OpenAI 为迁移至 Codex 的企业提供价值 400 美元的免费额度，正式开启补贴战",
            "Anthropic 紧急推出 Opus 4.7 Fast 抢先应战，Claude Code vs Codex/GPT-5.6 三方混战",
            "xAI 发布 Grok Build——首款终端编程智能体，支持并行子智能体与无头模式嵌入",
            "阿里 Qoder 1.0 发布：从 AI IDE 升级为智能体自主开发工作台，四方争霸格局形成",
        ],
        "links": [
            {"url": "https://www.msn.cn/zh-cn/news/other/openai%E7%8B%82%E9%A3%99%E8%BF%AD%E4%BB%A3gpt-56-%E8%A1%A5%E8%B4%B4%E6%88%98%E5%85%A8%E9%9D%A2%E6%89%93%E5%93%8D/gm-GMA1461849", "source": "MSN中国"},
            {"url": "https://blog.csdn.net/2401_84289488/article/details/161144504", "source": "CSDN"},
        ]
    },
]

industry_news = [
    {
        "company": "OpenAI",
        "tag": "金融落地",
        "description": "OpenAI 宣布 ChatGPT Pro 用户可通过 Plaid 接口连接全球 12000+ 金融机构，实时分析消费、管理资产组合，并将于后续集成 Intuit 服务（税务申报、信用管理）。Greg Brockman 正式担任产品负责人，ChatGPT/Codex/开发者 API 整合为单一团队。",
        "links": [
            {"url": "https://blog.csdn.net/2401_84289488/article/details/161144504", "source": "CSDN"},
        ]
    },
    {
        "company": "Anthropic Claude",
        "tag": "科研助手",
        "description": "Claude Code 全套论文流水线正式开源（GitHub 6.4k Stars），涵盖文献综述、实验设计、数据分析、论文写作4个 skill，跑通整套科研流程，费用参考透明，「复杂需求还得 Claude」成业界共识。",
        "links": [
            {"url": "https://www.36kr.com/", "source": "36氪"},
            {"url": "https://maomu.com/news", "source": "猫目AI"},
        ]
    },
    {
        "company": "字节跳动",
        "tag": "空间智能",
        "description": "字节提出视觉生成第三路线——不依赖扩散模型也不依赖纯自回归，采用「边画边改」新范式，挑战当前视觉生成主流技术路线，在世界模型领域持续发力。",
        "links": [
            {"url": "https://txtmix.com/posts/news/ai-morning-news-2026-05-15/", "source": "TextMix"},
        ]
    },
    {
        "company": "谷歌 DeepMind",
        "tag": "具身智能",
        "description": "谷歌持续推进 Android AI 化战略，Gemini Intelligence 深度整合至 Android 17。同时在具身智能领域与波士顿动力等企业展开合作，探索 AI 与物理世界的深度融合路径。",
        "links": [
            {"url": "https://www.36kr.com/", "source": "36氪"},
        ]
    },
    {
        "company": "百度",
        "tag": "新度量衡",
        "description": "李彦宏在 Create 2026 大会上首次提出 DAA（日活智能体数）概念，将其定位为替代 Token 的 AI 时代新度量衡，更接近 AI 计算本质，百度美股当日涨超 7%。",
        "links": [
            {"url": "https://txtmix.com/posts/news/ai-morning-news-2026-05-15/", "source": "TextMix"},
        ]
    },
    {
        "company": "港大 × 阿里",
        "tag": "机器人提速",
        "description": "港大开源 FASTER VLA 模型，首创 TTFA（Time To First Action）指标，实现单步采样反应，相比现有方法提速 10 倍，大幅降低实体机器人反应延迟。千问团队四篇论文入选 ICML/ACL，推理速度提升 36%。",
        "links": [
            {"url": "https://txtmix.com/posts/news/ai-morning-news-2026-05-15/", "source": "TextMix"},
        ]
    },
    {
        "company": "快手",
        "tag": "资本故事",
        "description": "快手考虑将可灵 AI 单独上市，资本市场可为 AI 故事短暂狂热，但最终一定会回归商业常识。可灵 AI 自分拆以来估值 200 亿美元，持续为快手贡献 AI 叙事。",
        "links": [
            {"url": "https://maomu.com/news", "source": "猫目AI"},
        ]
    },
    {
        "company": "国家具身智能基地",
        "tag": "规模化落地",
        "description": "国家具身智能应用中试基地正式揭牌，摩尔线程提供国产算力方案，与基地签署战略合作成立联合实验室，标志着具身智能从技术验证迈向规模化产业落地阶段。",
        "links": [
            {"url": "https://www.ithome.com/", "source": "IT之家"},
        ]
    },
]

insights = [
    "【AI 算力进入「国芯国模」时代】无锡 Token 工厂 + 华为昇腾 384 超节点 + 阿里平头哥 GPU 量产，国产算力集群加速成型，从单点建设转向全网协同。",
    "【AI 编程战争全面升级】OpenAI Codex vs Anthropic Claude Code vs xAI Grok Build vs 阿里 Qoder，四方争霸格局形成，价格战与补贴战同步开打，AI 编程进入普惠时代。",
    "【具身智能规模化元年正式开启】国家具身智能基地 + 摩尔线程联合实验室 + 港大 FASTER 开源，AI 从数字世界走向物理世界，规模化产业落地成为 2026 年主旋律。",
    "【AI 融资格局重塑，百亿融资成常态】贝索斯新公司、Anthropic、阶跃星辰三方融资潮，AI 行业进入「大者恒大」时代，资本门槛持续抬高，中小玩家生存空间收窄。",
    "【DAA 概念首提：AI 商业价值度量重构】百度李彦宏提出替代 Token 的新度量衡，AI 产业从「比参数」到「比干活」，真正衡量 AI 价值的商业指标呼之欲出。",
]

news_items = {
    "breaking_news": breaking_news,
    "industry_news": industry_news,
    "insights": insights,
    "sources": ["36氪", "猫目AI", "IT之家", "CSDN", "量子位", "TextMix", "站长之家", "MSN中国"],
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
