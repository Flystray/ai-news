---
name: ai-news
disable: false
allowed-tools: 
---

# AI News Center - 技能配置

## 简介
AI 每日新闻采集与订阅中心技能，自动获取并整理每日 AI/大模型最新动态，生成带原文链接的精美 HTML 报告。

## 文件结构
```
ai-news/
├── SKILL.md                    # 本配置文件
├── index.html                  # 订阅中心前端页面
├── collect_news.py             # 新闻采集脚本
├── sources.json                # 新闻源配置
├── 一键生成今日新闻.bat        # Windows快捷脚本
├── reports/                    # 日报存放目录
│   └── 2026-03-31-with-links.html
├── github-sync.bat             # 一键同步到GitHub
└── README.md                   # 使用说明
```

## 使用方法

### 1. 生成今日新闻
- 方式A：双击 `一键生成今日新闻.bat`
- 方式B：告诉 AI "今天的 AI 新闻"
- 方式C：`python collect_news.py`

### 2. 访问新闻报告
- 本地：`reports/2026-03-31-with-links.html`
- 在线：`https://你的用户名.github.io/ai-news/reports/2026-03-31-with-links.html`

### 3. 同步到 GitHub
- 双击 `github-sync.bat`
- 或手动 push

## 配置

### 新闻源 (sources.json)
```json
{
  "国际大厂": ["OpenAI", "Anthropic", "Google DeepMind", ...],
  "国内大厂": ["阿里通义", "百度文心", "字节豆包", ...],
  "科技媒体": ["量子位", "机器之心", "36氪", ...]
}
```

### 报告规则
- ✅ 每条新闻必须带原文链接
- ✅ 命名格式：`{日期}-with-links.html`
- ✅ 分类：重磅发布、商业动态、技术突破、核心洞察

## GitHub Pages
- 仓库：https://github.com/Flystray/ai-news
- 订阅中心：https://Flystray.github.io/ai-news/
- 今日新闻：https://Flystray.github.io/ai-news/reports/

## 作者
- 创建日期：2026-03-31
- 维护者：Administrator
