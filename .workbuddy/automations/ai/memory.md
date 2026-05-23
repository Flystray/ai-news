# AI每日新闻自动化 - 执行记忆

## 执行概况
- 自动化ID: ai
- 名称: AI每日新闻
- 状态: ACTIVE

---

## 执行记录

### 2026-05-17
- 执行时间: 2026-05-17 15:14
- 状态: ⚠️ 部分成功（微信公众号推送失败 - IP白名单问题持续，IP已变更为 115.200.24.137；GitHub push成功）
- 报告路径: reports/2026-05-17-with-links.html
- 新闻来源: 猫目AI / 36氪 / IT之家 / CSDN / TextMix / 站长之家 / MSN中国
- 步骤1: ✅ 生成精美HTML日报（重磅4条 + 行业8条 + 洞察5条）
- 步骤2: ✅ HTML已生成（wechat_article.html + cover_2026-05-17.png），推送失败（errcode 40164: IP 115.200.24.137 未在微信白名单）
- 步骤3: ✅ Git add/commit/push（commit 4df57a6 → 0d2add6）
- 步骤4: 📋 简报摘要在下方输出（无个人微信API直连能力）
- 今日重磅:
  - GPT-5.6曝光：下月发布，1.5M超长上下文实测可跑通，Codex ultrafast 2-3倍提速
  - 无锡Token工厂启动：首批4台华为昇腾384超节点，国产算力再下一城
  - AI融资格局重塑：贝索斯新公司估值380亿美元，Anthropic寻求9000亿美元融资
  - OpenAI vs Anthropic补贴大战开打：400美元补贴争抢Claude Code企业用户
- 行业动态:
  - OpenAI ChatGPT Pro接入12000+金融机构，Greg Brockman正式担任产品负责人
  - Claude Code全套论文流水线开源（6.4k Stars）
  - 字节跳动提出视觉生成第三路线「边画边改」新范式
  - 百度李彦宏首提DAA概念，百度美股涨超7%
  - 港大FASTER VLA模型开源，提速10倍
  - 快手可灵AI考虑单独上市，估值200亿美元
  - 国家具身智能应用中试基地揭牌，摩尔线程共建算力实验室
  - 谷歌持续推进Android AI化战略
- 核心洞察:
  - AI算力进入「国芯国模」时代
  - AI编程战争全面升级，四方争霸+价格战开打
  - 具身智能规模化元年正式开启
  - AI融资格局重塑，百亿融资成常态
  - DAA概念首提，AI商业价值度量重构
- GitHub链接: https://flystray.github.io/ai-news/reports/2026-05-17-with-links.html

### 2026-05-23
- 执行时间: 2026-05-23 18:52
- 状态: ⚠️ 部分成功（微信推送IP白名单问题持续，GitHub push因网络不通失败）
- 报告路径: reports/2026-05-23-with-links.html
- 步骤1: ✅ HTML日报生成（重磅4/行业8/洞察5）
- 步骤2: ⚠️ wechat_article.html+封面已生成，推送失败（IP: 115.200.11.65）
- 步骤3: ⚠️ commit 7e32994已创建，push失败（github.com:443不可达）
- 步骤4: ✅ 简报摘要已输出
- 今日重磅:
  - OpenAI冲刺IPO：估值超8500亿美元，最快本周提交招股书，Q1营收57亿美元
  - Karpathy官宣加入Anthropic预训练团队，AI人才争夺战升级
  - Project Glasswing首月战报：溢出1万高危漏洞，真实率90.6%
  - Anthropic即将首度盈利：Q2营收预计109亿美元，运营利润5.59亿
- 行业动态:
  - 智谱GLM-5.1-highspeed：400 tokens/s刷新全球速度上限 + ZCube架构落地
  - 联想全年营收5899亿元创新高，AI收入翻倍增长105%
  - 渣打银行AI替代7800个后台岗位，CEO致歉
  - 深开鸿M-Robots OS 2.0：全国首个开源鸿蒙机器人操作系统
  - DeepSeek融资700亿+DeepSeek Code即将上线
  - ChatGPT解锁AI填表：拍照+口述自动填表
  - 安诊儿与蚂蚁阿福完成系统对接，服务超2亿人次
  - 三大运营商齐推Token套餐，AI算力公共事业化
- 核心洞察:
  - AI变现加速期：IPO+盈利+万亿估值三重信号
  - AI安全实战交付：从能力展示到生产力
  - AI编程四方争霸：GPT-5.6/Claude Code/DeepSeek Code/GLM-5.1
  - "渣打时刻"：AI替代白领就业进入执行阶段
  - 国产机器人OS系统化：M-Robots OS 2.0有望重现Android效应
- GitHub链接: https://flystray.github.io/ai-news/reports/2026-05-23-with-links.html

### ⚠️ 待处理：微信IP白名单（持续，需用户手动添加）
- 当前IP: 115.200.11.65（已变更，之前是115.200.24.137）
- 需在 mp.weixin.qq.com 后台添加 IP 115.200.11.65 到白名单
- 添加后重试: C:\Users\YF\.workbuddy\binaries\python\versions\3.13.12\python.exe C:\Users\YF\.workbuddy\skills\wechat-mp\push_draft.py 2026-05-23
