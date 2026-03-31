# 📰 AI News Center - AI新闻订阅中心

> 每日自动采集 AI/大模型最新动态，生成精美报告

## 🎯 功能

- 📊 **自动采集** - 聚合 20+ 优质信息源
- 🔗 **带链接** - 每条新闻附带原文链接
- 📱 **多端访问** - 支持手机/电脑访问
- ⚡ **一键生成** - 轻松生成每日资讯

## 🚀 快速开始

### 生成今日新闻
```bash
python collect_news.py
```

### 查看报告
打开 `reports/2026-03-31-with-links.html`

### 同步到 GitHub
```bash
./github-sync.bat
```

## 📁 目录结构

```
ai-news/
├── index.html              # 订阅中心首页
├── collect_news.py         # 采集脚本
├── sources.json            # 新闻源配置
├── reports/                # 日报目录
│   └── 2026-03-31-with-links.html
└── github-sync.bat         # GitHub同步脚本
```

## 🔗 在线访问

| 内容 | 链接 |
|------|------|
| 订阅中心 | https://Flystray.github.io/ai-news/ |
| 今日新闻 | https://Flystray.github.io/ai-news/reports/ |

## ⚙️ 配置新闻源

编辑 `sources.json` 添加更多来源：

```json
{
  "分类名": [
    {"name": "媒体名", "url": "网址", "tags": ["标签"]}
  ]
}
```
