# AI 每日资讯报告模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{日期} AI 每日资讯</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            padding: 40px 20px;
            color: #e0e0e0;
        }
        .container { max-width: 900px; margin: 0 auto; }
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        .header h1 {
            font-size: 2.5em;
            background: linear-gradient(90deg, #00d4ff, #7c3aed);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }
        .header .date {
            color: #888;
            font-size: 1.1em;
        }
        .section {
            background: rgba(255,255,255,0.05);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 24px;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .section-title {
            font-size: 1.3em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid;
        }
        .section-title.models { border-color: #ff6b6b; color: #ff6b6b; }
        .section-title.tech { border-color: #4ecdc4; color: #4ecdc4; }
        .section-title.industry { border-color: #ffe66d; color: #ffe66d; }
        .news-item {
            background: rgba(0,0,0,0.2);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 16px;
            transition: transform 0.2s, background 0.2s;
        }
        .news-item:hover {
            transform: translateX(4px);
            background: rgba(0,0,0,0.3);
        }
        .news-item h3 {
            font-size: 1.1em;
            margin-bottom: 10px;
            color: #fff;
        }
        .news-item p {
            color: #aaa;
            line-height: 1.6;
            margin-bottom: 12px;
        }
        .news-item .meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.85em;
        }
        .news-item .source {
            color: #666;
        }
        .news-item a {
            color: #00d4ff;
            text-decoration: none;
        }
        .news-item a:hover { text-decoration: underline; }
        .footer {
            text-align: center;
            margin-top: 40px;
            color: #666;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 AI 每日资讯</h1>
            <p class="date">{日期} | 专注 AI 前沿动态</p>
        </div>

        <!-- 通用大模型 -->
        <div class="section">
            <h2 class="section-title models">🧠 通用大模型</h2>
            {大模型新闻列表}
        </div>

        <!-- 技术进展 -->
        <div class="section">
            <h2 class="section-title tech">⚡ 技术进展</h2>
            {技术新闻列表}
        </div>

        <!-- 行业动态 -->
        <div class="section">
            <h2 class="section-title industry">📊 行业动态</h2>
            {行业新闻列表}
        </div>

        <div class="footer">
            <p>由 AI 助手自动生成 | 数据来源：网络公开信息</p>
        </div>
    </div>
</body>
</html>
```
