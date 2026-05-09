# AI每日新闻自动化 - 执行记忆

## 执行概况
- 自动化ID: ai
- 名称: AI每日新闻
- 状态: ACTIVE

---

## 执行记录

### 2026-05-07
- 执行时间: 2026-05-07 09:00
- 状态: ⚠️ 部分成功（微信公众号推送失败 - IP白名单问题持续，IP已变更为 115.200.26.33）
- 报告路径: reports/2026-05-07-with-links.html
- 新闻来源: 新浪财经 / 搜狐 / 腾讯新闻 / 量子位 / 机器之心 / CSDN / AIBars / ITBear / 36氪
- 步骤1: ✅ 生成精美HTML日报（重磅4条 + 行业8条 + 洞察6条）
- 步骤2: ✅ HTML已生成（wechat_article.html + article_2026-05-07.md），推送失败（errcode 40164: IP 115.200.26.33 未在微信白名单）
- 步骤3: ✅ Git add/commit/push（commit 5eee450）
- 步骤4: 📋 简报摘要在下方输出（无个人微信API直连能力）
- 今日重磅: OpenAI与Anthropic同日牵手华尔街（两条路线正面交锋）、Anthropic 5年2000亿美元云账单破纪录、特朗普政府AI政策急转弯（模型发布前须过审）、GPT-5.5 Instant上线（幻觉率降52.5%）
- 行业动态: OpenAI×高通AI手机芯片2028量产、DeepSeek V4开源百万上下文、Meta Llama 3开源可商用、Google Gemini 1.5 Pro降价60%、xAI Grok 4.3发布、华为灵境造物、智谱AI揭秘Scaling降智问题
- 核心洞察: 华尔街资本重塑AI商业化路径、算力军备竞赛逼近经济临界点、开源双线竞争格局成型、AI监管进入上市前审批时代、端侧AI芯片重塑移动生态、具身智能规模化元年已至
- GitHub链接: https://flystray.github.io/ai-news/reports/2026-05-07-with-links.html

---

### ⚠️ 待处理：微信IP白名单（持续，需用户手动添加）
- 需在 mp.weixin.qq.com 后台添加 IP 115.200.26.33 到白名单（注意：IP已变更！）
- 添加后重新运行: /c/Users/YF/.workbuddy/binaries/python/versions/3.13.12/python.exe /c/Users/YF/.workbuddy/skills/wechat-mp/push_draft.py 2026-05-07

---

### 2026-05-06
- 执行时间: 2026-05-06 09:00
- 状态: ⚠️ 部分成功（微信公众号推送失败 - IP白名单问题持续）
- 报告路径: reports/2026-05-06-with-links.html
- 新闻来源: TechCrunch / AITNT / 腾讯新闻 / 新浪财经 / 搜狐 / 网易 / 36氪 / The AI Track / 虎嗅 / 澎湃等
- 步骤1: ✅ 生成精美HTML日报（重磅4条 + 行业8条 + 洞察6条）
- 步骤2: ✅ HTML已生成（wechat_article.html + article_2026-05-06.md），推送失败（errcode 40164: IP 220.176.214.175 未在微信白名单）
- 步骤3: ✅ Git add/commit/push（commit 5b9313e）
- 步骤4: 📋 简报摘要在下方输出（无个人微信API直连能力）
- 今日重磅: GPT-5.5 Instant发布成默认模型、斯坦福HAI重组李飞飞升职、豆包推付费会员68元起、马斯克诉OpenAI庭审第二周
- 行业动态: Claude Mythos安全事件/Anthropic估值9000亿、微软结束OpenAI云独占、中国叫停Meta收购Manus、Gemini企业Agent平台、DeepSeek V4、MiniMax M2.5、具身智能破百亿、Qwen3.6开源
- 核心洞察: AI商业化拐点、学术AI组织力应对、OpenAI庭审暴露行业原罪、企业Agent战争元年、具身智能产业化、AI安全实战阶段
- GitHub链接: https://flystray.github.io/ai-news/reports/2026-05-06-with-links.html

---

### ⚠️ 待处理：微信IP白名单（持续，需用户手动添加）
- 需在 mp.weixin.qq.com 后台添加 IP 220.176.214.175 到白名单
- 添加后重新运行: C:\Users\YF\.workbuddy\binaries\python\versions\3.13.12\python.exe C:\Users\YF\.workbuddy\skills\wechat-mp\push_draft.py 2026-05-06

---

### 2026-05-04
- 执行时间: 2026-05-04 09:00
- 状态: ⚠️ 部分成功（微信公众号推送失败 - IP白名单问题持续，IP已变更）
- 报告路径: reports/2026-05-04-with-links.html
- 新闻来源: 量子位/36氪/新浪财经/腾讯新闻/Anthropic官方
- 步骤1: ✅ 生成精美HTML日报（重磅3条 + 行业8条 + 洞察5条）
- 步骤2: ✅ HTML已生成（wechat_article.html），推送失败（errcode 40164: IP 220.176.214.175 未在微信白名单）
- 步骤3: ✅ Git add/commit/push（commit a074e31）
- 步骤4: 📋 简报摘要在下方输出（无个人微信API直连能力）
- 今日重磅: 马斯克OpenAI庭审警告AI风险、GPT-5.6哥布林怪癖事件、谷歌400亿豪赌Anthropic
- 行业动态: DeepSeek V4开源百万上下文、智谱揭秘Scaling瓶颈、华为灵境造物、Claude Opus 4.7、国家电网68亿具身智能大单
- 核心洞察: AI监管从议题到行动、Scaling Law瓶颈、具身智能规模化元年开启、AI原住民代际更替
- GitHub链接: https://flystray.github.io/ai-news/reports/2026-05-04-with-links.html
---

### 2026-05-08
- 执行时间: 2026-05-08 09:00
- 状态: ⚠️ 部分成功（微信公众号推送失败 - IP白名单问题持续，IP已变更为 115.200.6.159）
- 报告路径: reports/2026-05-08-with-links.html
- 新闻来源: 腾讯资讯 / 第一财经 / 新浪财经 / 华峰资本 / 中新社
- 步骤1: ✅ 生成精美HTML日报（重磅4条 + 行业8条 + 洞察5条）
- 步骤2: ✅ HTML已生成（wechat_article.html + article_2026-05-08.md），推送失败（errcode 40164: IP 115.200.6.159 未在微信白名单）
- 步骤3: ✅ Git add/commit/push（commit d46d7f1）
- 步骤4: 📋 简报摘要在下方输出（无个人微信API直连能力）
- 今日重磅: 月之暗面Kimi约20亿美元融资（估值超200亿美元）、马斯克解散xAI并入SpaceX、中央网信办「清朗」整治AI乱象专项行动（4个月）、腾讯混元Hy3 Token调用量两周增长10倍
- 行业动态: 宇树开放全球首个人形机器人任务动作应用商店、通义千问PC端AI语音输入、英矽智能发布LabClaw自动实验室操作系统、宇树G1化身僧侣在韩国寺庙受戒、科创50 AI硬件板块暴涨9%、三星中国大陆家电全线停售
- 核心洞察: 国产AI进入百亿独角兽时代、AI监管从行业自律走向国家主权、AI整合时代生态帝国竞争来临、人形机器人平台化iPhone时刻到来、大模型应用爆发元年已至
- GitHub链接: https://flystray.github.io/ai-news/reports/2026-05-08-with-links.html

### ⚠️ 待处理：微信IP白名单（持续，需用户手动添加）
- 需在 mp.weixin.qq.com 后台添加 IP 115.200.6.159 到白名单（注意：IP已多次变更！）
- 添加后重新运行: C:\Users\YF\.workbuddy\binaries\python\versions\3.13.12\python.exe C:\Users\YF\.workbuddy\skills\wechat-mp\push_draft.py 2026-05-08
