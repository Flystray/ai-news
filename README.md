# 📰 AI News Center

> 每日自动采集 AI/大模型最新动态，生成精美报告

## 🚀 功能

- 📊 **自动采集** - 聚合 20+ 优质信息源
- 🔗 **带链接** - 每条新闻附带原文链接
- 📱 **多端访问** - 支持手机/电脑访问
- ⚡ **一键生成** - 轻松生成每日资讯

## 🌐 在线访问

| 内容 | 链接 |
|------|------|
| 订阅中心 | https://Flystray.github.io/ai-news/ |
| 今日新闻 | https://Flystray.github.io/ai-news/reports/ |

## 📁 目录结构

```
ai-news/
├── index.html              # 订阅中心首页
├── collect_news.py         # 采集脚本
├── sources.json            # 新闻源配置
├── github-sync.bat         # GitHub同步脚本
├── reports/                # 日报目录
│   └── 2026-03-31-with-links.html
├── README.md               # 本文件
└── SKILL.md                # 技能配置
```

## ⚙️ 本地使用

### 生成今日新闻
```bash
cd ai-news
python collect_news.py
```

### 同步到 GitHub
双击 `github-sync.bat` 或：
```bash
git add .
git commit -m "Update"
git push
```

## 📝 手动更新日报

1. 打开 GitHub 仓库
2. 进入 `reports/` 文件夹
3. 点 **Add file** → **Create new file**
4. 文件名：`reports/2026-04-01-with-links.html`
5. 粘贴内容
6. Commit

## 📡 新闻源

- **国际大厂**: OpenAI, Anthropic, Google DeepMind, Meta AI, Microsoft, xAI
- **国内大厂**: 阿里通义, 百度文心, 字节豆包, 月之暗面Kimi, 智谱AI
- **科技媒体**: 量子位, 机器之心, 36氪, 虎嗅

---
*Powered by WorkBuddy AI Assistant*
