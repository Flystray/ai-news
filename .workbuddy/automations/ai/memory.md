# AI每日新闻自动化 - 执行记忆

## 执行概况
- 自动化ID: ai
- 名称: AI每日新闻
- 状态: ACTIVE

---

## 执行记录

### 2026-05-13
- 执行时间: 2026-05-13 10:43
- 状态: ⚠️ 部分成功（微信公众号推送失败 - IP白名单问题持续，IP已变更为 115.200.7.35；GitHub网络不可达，本地commit已保存）
- 报告路径: reports/2026-05-13-with-links.html
- 新闻来源: 量子位 / 腾讯新闻 / 新浪财经 / AI快讯 / AIToolsRecap / 36氪
- 步骤1: ✅ 生成精美HTML日报（重磅4条 + 行业5条 + 洞察4条）
- 步骤2: ✅ HTML已生成（wechat_article.html + article_2026-05-13.md），推送失败（errcode 40164: IP 115.200.7.35 未在微信白名单）
- 步骤3: ✅ Git commit成功（commit 34ff93b），⚠️ push网络超时（GitHub不可达，需稍后重试）
- 步骤4: 📋 简报摘要在下方输出（无个人微信API直连能力）
- 今日重磅:
  - 快手官宣分拆可灵AI：估值200亿美元、融资20亿美元，腾讯领投
  - 何恺明首个语言模型发布：CV大佬不走GPT路线，扩散模型另起炉灶（仅105M参数）
  - Cerebras冲刺350亿美元IPO：OpenAI签200亿美元算力大单
  - 浙大校友突破32年拉姆齐数下界，AI再次攻克数学圣杯
- 行业动态:
  - OpenAI与Anthropic同日牵手华尔街，驻场AI时代正式开启
  - OpenClaw重磅更新（可操作屏幕/鼠标）+ 360发现23个安全漏洞
  - 阿里千问与淘宝全面打通，业界首个AI购物全链路闭环落地
  - 中国移动连发三大AI产品（MoMA平台+MobileClaw+AI云电脑）
  - 火山引擎Agent Plan：Doubao+Seedance+Seedream一站聚合
- 核心洞察:
  - AI大厂「分拆潮」来袭，估值重塑成为2026年主旋律
  - OpenClaw「长手长脚」标志AI Agent从工具进化为员工
  - 何恺明「扩散LLM」挑战自回归正统，CV天才倒逼NLP革命
  - 从「卖API」到「卖驻场」，AI商业化进入执行力竞争时代
- GitHub链接: https://flystray.github.io/ai-news/reports/2026-05-13-with-links.html

### ⚠️ 待处理1：微信IP白名单（持续，需用户手动添加）
- 需在 mp.weixin.qq.com 后台添加 IP 115.200.7.35 到白名单（注意：IP已多次变更！）
- 添加后重新运行: /c/Users/YF/.workbuddy/binaries/python/versions/3.13.12/python.exe /c/Users/YF/.workbuddy/skills/wechat-mp/push_draft.py 2026-05-13

### ⚠️ 待处理2：GitHub push（本地commit已保存，网络恢复后重试）
- commit ID: 34ff93b（需确认push成功以更新GitHub Pages）
- GitHub Pages URL: https://flystray.github.io/ai-news/reports/2026-05-13-with-links.html

---

### 2026-05-12
- 执行时间: 2026-05-12 10:22
- 状态: ⚠️ 部分成功（微信公众号推送失败 - IP白名单问题持续，IP已变更为 115.200.18.219）
- 报告路径: reports/2026-05-12-with-links.html
- 新闻来源: IT之家 / 36氪 / 新浪财经 / 凤凰网科技 / 中国新闻网 / 量子位 / 人民网 / AITNT / AI ZOL
- 步骤1: ✅ 生成精美HTML日报（重磅4条 + 行业5条 + 洞察4条）
- 步骤2: ✅ HTML已生成（wechat_article.html + article_2026-05-12.md），推送失败（errcode 40164: IP 115.200.18.219 未在微信白名单）
- 步骤3: ✅ Git add/commit/push（commit 6447edb）
- 步骤4: 📋 简报摘要在下方输出（无个人微信API直连能力）
- 今日重磅:
  - OpenAI 砸 40 亿美元成立部署公司，收购 Tomoro 引入 150 名工程师派驻企业
  - DeepSeek 首轮融资 500 亿，梁文锋个人出资 200 亿，21天估值翻5倍至515亿美元
  - OpenAI 推出 Daybreak 安全防御项目，AI 代码安全检查进入开发流程
  - 千问与淘宝全面打通，阿里率先实现 AI 购物全链路闭环
- 行业动态:
  - Anthropic Q1 年化增长 80 倍，CEO 预测将出现 10 亿美元"一人公司"
  - OpenAI 研究员提出"启发式学习"新范式，无需神经网络也能打 Atari 满分
  - 三部门联合印发《智能体规范应用与创新发展实施意见》
  - 百度发布文心 5.1，RAG 搜索能力国内第一，预训练成本仅业界 6%
  - 企业微信 5.0.8 上线"记录面聊"功能
- 核心洞察:
  - AI 巨头全面转向"企业服务战"，从卖API升级为卖解决方案
  - 中国 AI 进入"超级独角兽"时代，国有资本加速入场
  - "启发式学习"挑战梯度下降正统地位，AI训练范式可能迎来根本变革
  - 监管从"管模型"走向"管行为"，中国率先为AI Agent专项立法
- GitHub链接: https://flystray.github.io/ai-news/reports/2026-05-12-with-links.html

### ⚠️ 待处理：微信IP白名单（持续，需用户手动添加）
- 需在 mp.weixin.qq.com 后台添加 IP 115.200.18.219 到白名单（注意：IP已多次变更！）
- 添加后重新运行: /c/Users/YF/.workbuddy/binaries/python/versions/3.13.12/python.exe /c/Users/YF/.workbuddy/skills/wechat-mp/push_draft.py 2026-05-12

---

### 2026-05-09
- 执行时间: 2026-05-09 09:00
- 状态: ⚠️ 部分成功（微信公众号推送失败 - IP白名单问题持续，IP已变更为 115.200.21.94）
- 报告路径: reports/2026-05-09-with-links.html
- 新闻来源: 新智元 / Reuters / TechCrunch / 袁帅AI简报 / 36氪 / llm-stats.com / MacRumors / 凤凰网科技 / EET-China
- 步骤1: ✅ 生成精美HTML日报（重磅4条 + 行业5条 + 洞察4条）
- 步骤2: ✅ HTML已生成（wechat_article.html + article_2026-05-09.md），推送失败（errcode 40164: IP 115.200.21.94 未在微信白名单）
- 步骤3: ✅ Git add/commit/push（commit e00156a）
- 步骤4: 📋 简报摘要在下方输出（无个人微信API直连能力）
- 今日重磅:
  - xAI正式解散并入SpaceX，成立不到三年，2500亿估值归零，GPU利用率仅11%
  - Anthropic讨论万亿美元融资，同时签订18亿美元Akamai算力合同
  - Google Fitbit更名为Google Health，Gemini健康助手5月19日上线$9.99/月
  - Claude Managed Agents四项更新，Outcomes使docx准确率+8.4%，pptx+10.1%
- 行业动态:
  - OpenAI三款Realtime语音模型发布（翻译/转写/音频理解）
  - OpenAI Codex Chrome周活400万，年初增长8倍
  - Kimi完成136亿元D轮融资，创中国大模型单笔融资最高纪录
  - Mistral 128B开源旗舰模型发布
- 核心洞察:
  - xAI解散是AI资本泡沫标志性事件
  - Anthropic从卖模型升级为建平台
  - AI入口竞争从手机延伸到车机
  - 开源双线竞争格局完全成型
- GitHub链接: https://flystray.github.io/ai-news/reports/2026-05-09-with-links.html

---

### ⚠️ 待处理：微信IP白名单（持续，需用户手动添加）
- 需在 mp.weixin.qq.com 后台添加 IP 115.200.21.94 到白名单（注意：IP已多次变更！）
- 添加后重新运行: /c/Users/YF/.workbuddy/binaries/python/versions/3.13.12/python.exe /c/Users/YF/.workbuddy/skills/wechat-mp/push_draft.py 2026-05-09

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
- 添加后重新运行: C:\Users\YF\.workbuddy\binaries\python\versions\3.13.12\python.exe C:\Users\YF\.workbuddy\binaries\python\versions\3.13.12\python.exe C:\Users\YF\.workbuddy\skills\wechat-mp\push_draft.py 2026-05-08

---

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

### 2026-05-10
- 执行时间: 2026-05-10 09:00
- 状态: ⚠️ 部分成功（微信公众号推送失败 - IP白名单问题持续，IP已变更为 115.200.11.207）
- 报告路径: reports/2026-05-10-with-links.html
- 新闻来源: AITNT / 新浪财经 / 36氪 / 腾讯新闻 / 澎湃新闻 / EET-China / 中国新闻网 / IT熊
- 步骤1: ✅ 生成精美HTML日报（重磅4条 + 行业5条 + 洞察4条）
- 步骤2: ⚠️ HTML已生成（wechat_article.html），推送失败（errcode 40164: IP 115.200.11.207 未在微信白名单）
- 步骤3: ✅ Git add/commit/push（commit b84f487）
- 步骤4: 📋 简报摘要在下方输出（无个人微信API直连能力）
- 今日重磅:
  - Hermes Agent 登顶 OpenRouter 全球调用榜，单日 Token 消耗 2710 亿，首次超越 OpenClaw
  - 谷歌秘密内测 AI 智能体 Remy，对标 OpenClaw，或于 I/O 2026 正式亮相
  - 月之暗面 Kimi 完成 136 亿元 D 轮融资，创中国大模型单笔融资最高纪录
  - 人工智能终端国家标准发布，涉及手机、眼镜、耳机等七大品类
- 行业动态:
  - GPT-5.5 Instant 正式上线，幻觉率降低 52.5%
  - 豆包启动付费订阅测试，三档方案最高 5088 元/年
  - Gemini 2.5 Pro I/O 版登顶 AI 编程榜
  - 宇树科技开放全球首个人形机器人任务动作应用商店
- 核心洞察:
  - AI Agent 竞赛进入白热化，中国开源模型登上全球舞台
  - 中国 AI 大模型进入百亿独角兽时代，国有资本大比例入场
  - 人形机器人应用商店开启，具身智能迈入平台化竞争
- GitHub链接: https://flystray.github.io/ai-news/reports/2026-05-10-with-links.html

### ⚠️ 待处理：微信IP白名单（持续，需用户手动添加）
- 需在 mp.weixin.qq.com 后台添加 IP 115.200.11.207 到白名单（注意：IP 已多次变更！）
- 添加后重新运行: C:/Users/YF/.workbuddy/binaries/python/versions/3.13.12/python.exe C:/Users/YF/.workbuddy/skills/wechat-mp/push_draft.py 2026-05-10

---
