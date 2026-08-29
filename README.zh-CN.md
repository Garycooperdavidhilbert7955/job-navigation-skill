<div align="center">

# 循证求职与简历顾问

### 研究近期岗位与真实JD，对照你的简历，判断适合什么、缺什么、先做什么

[English](README.md) · [架构](ARCHITECTURE.md) · [路线图](ROADMAP.md) · [参与贡献](CONTRIBUTING.md)

![状态](https://img.shields.io/badge/status-beta-f59e0b)
![版本](https://img.shields.io/badge/version-0.4.0--beta-2563eb)
![Agents](https://img.shields.io/badge/agents-ChatGPT%20%7C%20Codex%20%7C%20Claude%20%7C%20DeepSeek-111827)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB)
![许可证](https://img.shields.io/badge/license-MIT-16a34a)

`v0.4.0-beta`

</div>

这是一款面向应届生、求职者和职业转型者的跨Agent职业Skill。它研究近期行业、岗位和招聘JD，把市场要求与你提供的简历、项目和技能证据逐项对照，帮助你决定目标岗位、补足证据并安排下一步求职行动。

> **产品定位：**专注求职市场研究、细分岗位匹配、简历证据诊断、技能提升排序和30/60/90天求职计划。与目标岗位无关的通用教育、个人成长或其他生活决策不属于当前产品范围。

## 手册导航

- [1. 适合哪些用户](#1-适合哪些用户)
- [2. 产品功能](#2-产品功能)
- [3. 典型使用场景](#3-典型使用场景)
- [4. 输出结果示例](#4-输出结果示例)
- [5. 本地部署](#5-本地部署)
- [6. 正确使用方法](#6-正确使用方法)
- [7. 工作原理](#7-工作原理)
- [8. 技术设计与壁垒](#8-技术设计与壁垒)
- [9. 隐私、限制与注意事项](#9-隐私限制与注意事项)
- [10. 当前验证状态](#10-当前验证状态)
- [11. 维护与故障排查](#11-维护与故障排查)

## 1. 适合哪些用户

### 特别适合

- 正在选择岗位、积累求职证据的学生和应届生；
- 想用近期JD检查简历、项目和作品集的求职者；
- 想转行，但不愿在验证方向前先花大量时间和学费的人；
- 正在比较求职城市、行业、岗位或职业技能投资的职场人；
- 希望建议有来源、有边界，而不是只得到鼓励和泛泛建议的人。

### 不适合

- 自动投递职位、自动联系招聘者或操作招聘网站账号；
- 只靠关键词计算ATS分数；
- 虚构简历成果、指标或个人贡献；
- 保证获得工作、录取、收入或其他结果；
- 与求职无关的通用个人决策、教育规划或生活建议。

这是一套**求职决策与证据诊断工具，不是录用预测器**。它负责检索、比较和排序；你负责检查证据并保留最终决定权。

## 2. 产品功能

| 功能 | 用户会得到什么 | 内置边界 |
|---|---|---|
| 岗位与行业研究 | 有截止日期的官方、公司、招聘平台和劳动力市场证据 | 不会声称所有指定平台都已成功访问 |
| 证据校准 | 区分事实、推断、预测和建议 | 不会把著名模型当作事实证明 |
| 个性化分析 | 将证据与你提供的目标、限制和经历对照 | 不会补充你没有提供的技能或经历 |
| 岗位市场分析 | 去重后的JD要求、需求带、必需/加分项拆分 | 不会把招聘广告频率称为全部市场需求 |
| 简历证据诊断 | 技能、证据、表达、经验和约束差距 | 不会把团队或模拟成果改写成个人真实结果 |
| 技能优先级 | 立即做、低成本验证、下一步构建、暂缓 | 不会要求学习所有JD中的全部工具 |
| 行动计划 | 一个方向、最多三项立即行动、投入和完成标准 | 时间或精力不足时会主动缩小计划 |
| 结果复盘 | 近期行为信号、后续结果指标和复盘节点 | 不会把一次好评或前后变化当作因果证明 |

## 3. 典型使用场景

| 使用场景 | 你需要提供 | Skill应该返回 |
|---|---|---|
| 应届生选择岗位 | 学历、项目、城市、求职时间、每周可用时间 | 细分岗位适配、证据差距和低成本市场测试 |
| 简历对比近期市场 | 脱敏简历、目标岗位和地区 | JD要求矩阵、候选人证据等级和行动优先级 |
| 职业转型 | 可迁移经历、限制、备选方向和风险承受度 | 方向比较、低成本验证实验和暂缓事项 |
| 行业或岗位趋势 | 地区、时间窗口、岗位名称及决策目标 | 有来源的趋势、矛盾、限制和个人影响 |
| 求职技能投资 | 目标JD差距、课程或证书成本、时间和替代证据路径 | 应该学习、先做项目、换证明方式还是暂缓 |
| 30/60/90天计划 | 目标、现状、每周投入和截止日期 | 符合时间预算的阶段目标，首屏只展示第一周 |

### 如果资料不完整会怎样？

- 要求简历差距分析却没有提供简历或事实背景时，Skill必须先索取材料，不能凭空构造候选人。
- 目标岗位或地区缺失且会改变市场判断时，每次只提出一个关键职业范围问题。
- 平台无法访问时，必须披露失败并缩小结论范围，不能伪造搜索结果。

## 4. 输出结果示例

首屏专门为疲惫或不熟悉研究方法的用户设计：

```text
结论
先验证AI运营，不要把AI产品经理设为唯一方向。
你目前的数据分析证据强于产品所有权证据。

接下来三件事
1. 把一个项目改写成“用户问题→决定→结果”案例。2小时。
2. 标注10条可用公司官网JD中的重复要求。90分钟。
3. 请两位从业者只评审这个案例。45分钟。

最大不确定性
两个指定招聘平台无法访问，因此当前样本只能用于方向判断。
```

只有在有用时才继续展示证据细节：

```text
事实｜中可信度
[有日期和附近引用的当前市场观察]

你的证据
[只使用简历、项目或作品集真正支持的内容]

推断
[为什么市场与个人证据更接近某个细分岗位]

建议
[结合个人限制、可逆且可验证的下一步]

复盘
完成10次定向投递或2次从业者访谈后更新判断。
```

目标不是生成更长的报告，而是得到一项可以检查的决定：**知道什么、不知道什么、与你有什么关系、下一步做什么。**

[虚构的精简示例](examples/early-career-ai-role-brief.md)只展示输出形态，不代表最新市场证据或效果证明。

## 5. 本地部署

### 5.1 先理解部署方式

本仓库只维护一份核心`SKILL.md`和reference规则，再通过轻量适配层部署到ChatGPT、Codex、Claude和DeepSeek。不同Agent不会各自维护一套容易漂移的职业分析逻辑。

产品显示名是“循证求职与简历顾问”。为兼容现有安装和调用方式，技术标识仍保留为`evidence-based-personal-advisor`。

| Agent界面 | 本仓库支持方式 | 部署入口 |
|---|---|---|
| Codex | 原生文件系统Skill | `scripts/install.py --agent codex` |
| ChatGPT | 包含核心Skill的OpenAI通用Plugin | `.codex-plugin/plugin.json`与ChatGPT发布包 |
| Claude Code | 原生文件系统Skill | `scripts/install.py --agent claude` |
| claude.ai | 上传自定义Skill | Claude Skill ZIP |
| Claude Code中的DeepSeek | 由Claude Code加载同一Skill，DeepSeek作为模型提供商 | Claude安装方式加DeepSeek官方Claude Code接入 |
| DeepSeek API | 系统指令适配器，可选内置网页搜索 | `adapters/deepseek/run.py` |

仓库不会自动把Skill、简历或评测记录上传给任何提供商。你实际使用某个Agent时提交的材料，将受该提供商的账号、工具和数据设置约束，详见[隐私说明](#9-隐私限制与注意事项)。

### 5.2 系统要求

- 上表中的至少一个Agent环境；
- Python 3.11或更高版本；
- 已下载或克隆的本仓库；
- 只有在需要检索最新资料时才需要网络访问。

不需要安装额外Python依赖。安装器和验证器只使用标准库。

### 5.3 下载仓库

在GitHub仓库页面选择一种方式：

**下载ZIP**

1. 点击 **Code → Download ZIP**；
2. 解压文件；
3. 在解压后的仓库根目录打开终端或PowerShell，不要进入内部Skill文件夹。

**Git克隆**

1. 在GitHub仓库页面点击 **Code**；
2. 复制HTTPS或SSH地址；
3. 使用你的Git客户端完成克隆；
4. 在克隆得到的`evidence-based-personal-advisor`文件夹中打开终端或PowerShell。

本手册后续命令都默认仓库根目录是当前工作目录。

### 5.4 安装前验证

macOS、Linux或PowerShell：

```bash
python3 scripts/validate_repo.py
```

如果Windows把Python注册为`python`：

```powershell
python scripts\validate_repo.py
```

预期输出：

```text
Validation passed.
Skill: evidence-based-personal-advisor
Evaluation cases: 9
```

该命令会检查必要文件、frontmatter、版本一致性、本地路径泄漏、相对链接、符号链接和常见密钥模式。它不能证明网页研究和建议本身正确。

### 5.5 安装到Codex

macOS或Linux：

```bash
python3 scripts/install.py --agent codex
```

Windows PowerShell：

```powershell
python scripts\install.py --agent codex
```

安装器会把目标解析为：

```text
${CODEX_HOME}/skills/evidence-based-personal-advisor
```

如果没有设置`CODEX_HOME`，则使用：

```text
~/.codex/skills/evidence-based-personal-advisor
```

安装采用事务式流程：先验证仓库，拒绝符号链接，把文件复制到临时目录，再移动到最终位置；如果目标已存在则停止，不会直接覆盖。

### 5.6 打包给ChatGPT

ChatGPT和Codex共享OpenAI Plugin格式。本仓库已经包含必须的`.codex-plugin/plugin.json`以及核心`skills/`目录。

生成可分发Plugin压缩包：

```bash
python3 scripts/package_skill.py --target chatgpt
```

压缩包会生成在`dist/`。它可以进入[OpenAI Plugin开发与发布流程](https://developers.openai.com/plugins/build/plugins)；正式上架后，用户也可以从通用Plugin目录安装。仅在本地生成ZIP不会自动发布或安装。

安装Plugin后，ChatGPT可以根据请求自动选择Skill，也可以通过`@`显式选择。

### 5.7 安装到Claude

Claude Code使用相同的`SKILL.md`目录格式：

```bash
python3 scripts/install.py --agent claude
```

默认安装位置：

```text
~/.claude/skills/evidence-based-personal-advisor
```

给claude.ai生成可上传的Skill压缩包：

```bash
python3 scripts/package_skill.py --target claude
```

在支持自定义Skill的账号中，通过 **Settings → Features** 上传生成的Claude压缩包。Claude各个界面的Skill相互独立：安装到Claude Code不会自动同步到claude.ai或Claude API。详见[Anthropic Agent Skills官方文档](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)。

Claude API的Skill容器本身不能访问网络。因此，除非宿主应用另外提供可用的搜索工具或检索结果，本项目不会声称Claude API版本能够完成近期岗位市场研究。

### 5.8 使用DeepSeek

支持两条路径：

1. **推荐的Agent方式：**先按上面的方法安装Claude Code Skill，再根据[DeepSeek官方Coding Agent接入说明](https://api-docs.deepseek.com/guides/coding_agents/)让Claude Code使用DeepSeek。Claude Code负责发现Skill，DeepSeek负责模型推理。
2. **直接使用API：**运行仓库中的标准库适配器，调用DeepSeek Responses API。

不联网测试适配器：

```bash
python3 adapters/deepseek/run.py --self-test
```

实际调用前，通过终端或密钥管理器设置`DEEPSEEK_API_KEY`，然后从标准输入传入已经脱敏的文本请求：

```bash
python3 adapters/deepseek/run.py <<'EOF'
我想申请[地区]的[岗位]。请研究近期JD，并结合以下脱敏简历事实分析：
[只填写必要事实]。请给出最重要的三项下一步行动。
EOF
```

适配器使用DeepSeek的`instructions`字段和可选内置`web_search`。由于DeepSeek API不会渐进式读取本地Skill文件，适配器需要内联运行时reference，通常会比Codex或Claude Code消耗更多输入Token。本仓库没有声称DeepSeek消费级网页聊天支持原生Skill上传。

### 5.9 安装到自定义Skill目录

只有在你的Codex环境已经配置为发现该目录时，才使用自定义路径：

```bash
python3 scripts/install.py --agent codex --dest "/absolute/path/to/codex/skills"
```

例如，将个人Skill统一保存在macOS桌面目录：

```bash
python3 scripts/install.py --agent codex --dest "$HOME/Desktop/codex/skill"
```

`--dest`指向Skill父目录，安装器会在其中创建最终的`evidence-based-personal-advisor`文件夹。

如需自定义Claude Code目录，请使用`--agent claude`并传入对应父目录。

### 5.10 验证安装结果

macOS或Linux默认路径：

```bash
test -f "$HOME/.codex/skills/evidence-based-personal-advisor/SKILL.md" && echo "Skill files installed"
```

Windows PowerShell：

```powershell
Test-Path "$HOME\.codex\skills\evidence-based-personal-advisor\SKILL.md"
```

Claude Code默认安装验证：

```bash
test -f "$HOME/.claude/skills/evidence-based-personal-advisor/SKILL.md" && echo "Claude Skill files installed"
```

然后新建一个Codex任务，并显式调用：

```text
使用 $evidence-based-personal-advisor，研究近期目标岗位和JD，结合我的简历证据找出岗位适配、差距和优先行动。
```

不同Codex环境和配置对本地Skill的发现方式可能不同。如果没有显示或触发，请重启Codex、检查安装目录，并使用完整的`$evidence-based-personal-advisor`显式调用。

ChatGPT安装Plugin后使用`@`选择；Claude Code请新建会话并要求使用`evidence-based-personal-advisor`，也可以让Claude根据请求自动匹配。

### 5.11 安全升级

安装器会主动拒绝覆盖已有Skill。请使用可恢复的升级方式：

1. 下载或拉取新版本仓库；
2. 验证新版本；
3. 把当前安装移动为备份；
4. 重新运行安装器；
5. 新建Codex任务并运行一个熟悉的测试问题；
6. 确认新版本正常后再删除备份。

macOS或Linux默认路径示例：

```bash
mv "$HOME/.codex/skills/evidence-based-personal-advisor" \
  "$HOME/.codex/skills/evidence-based-personal-advisor.backup"
python3 scripts/install.py --agent codex
```

回滚：

```bash
mv "$HOME/.codex/skills/evidence-based-personal-advisor" \
  "$HOME/.codex/skills/evidence-based-personal-advisor.failed"
mv "$HOME/.codex/skills/evidence-based-personal-advisor.backup" \
  "$HOME/.codex/skills/evidence-based-personal-advisor"
```

如果使用自定义目录，请把`$HOME/.codex/skills`替换为安装时使用的同一个父目录。

Windows PowerShell升级：

```powershell
Move-Item "$HOME\.codex\skills\evidence-based-personal-advisor" `
  "$HOME\.codex\skills\evidence-based-personal-advisor.backup"
python scripts\install.py --agent codex
```

Windows PowerShell回滚：

```powershell
Move-Item "$HOME\.codex\skills\evidence-based-personal-advisor" `
  "$HOME\.codex\skills\evidence-based-personal-advisor.failed"
Move-Item "$HOME\.codex\skills\evidence-based-personal-advisor.backup" `
  "$HOME\.codex\skills\evidence-based-personal-advisor"
```

Claude Code采用相同步骤，但目录换成`$HOME/.claude/skills`，并通过`--agent claude`重新安装。ChatGPT和claude.ai版本分别通过各自的Plugin或Skill管理界面升级。

### 5.12 可恢复卸载

把Skill移出活动目录，不立即删除：

```bash
mv "$HOME/.codex/skills/evidence-based-personal-advisor" \
  "$HOME/.codex/evidence-based-personal-advisor.uninstalled"
```

重启Codex并确认Skill不再被发现。只有确定不需要恢复时，再删除移动后的备份。

Windows PowerShell：

```powershell
Move-Item "$HOME\.codex\skills\evidence-based-personal-advisor" `
  "$HOME\.codex\evidence-based-personal-advisor.uninstalled"
```

Claude Code请把对应文件夹移出`$HOME/.claude/skills`。ChatGPT或claude.ai版本应从各自的Skill或Plugin管理界面移除。

## 6. 正确使用方法

### 6.1 只准备决策真正需要的背景

- 目标岗位和地区；
- 做决定的截止时间；
- 每周时间、预算、风险承受度和不能妥协的限制；
- 已删除不必要身份信息的简历、作品集、成绩单或项目证据；
- 你如何定义成功，以及希望避免什么。

删除电话号码、个人邮箱、身份证件、精确住址、私人链接和与决定无关的机密信息。

### 6.2 选择研究档位

| 档位 | 适用情况 | 通用研究范围 |
|---|---|---|
| `quick` | 快速了解、“先给方向”、低成本测试 | 4–8个有效来源、1–2个模型、精简回答 |
| `standard` | 大多数岗位、简历和求职方向分析 | 8–15个背景/研究来源、2–4类来源、1–3个模型 |
| `deep` | 明确要求系统比较或影响重大的决定 | 更广纳入规则、矛盾分析、明确检索限制 |

对于标准职业分析，career模块会在访问条件和市场规模允许时，另外抽取20–40条去重JD。JD记录数和背景研究来源数是两套控制指标。样本不足时可以减少，但必须披露；任何数字都不是为了凑数量。

连续两轮搜索都没有新增会改变决定的信息时，研究应停止。

### 6.3 提示词模板

**简历与近期市场**

```text
使用 $evidence-based-personal-advisor：

我的目标是于[日期]前申请[地区]的[岗位]。请研究最近[时间窗口]的行业和
岗位趋势，抽样分析近期JD，并结合我的脱敏简历找出岗位适配、技能差距、
证据差距和最重要的三项行动。请区分事实、推断和建议，标注研究截止日期、
证据可信度和无法访问的来源。我每周可以投入[小时]。
```

**职业转型**

```text
使用 $evidence-based-personal-advisor 比较[方向A]、[方向B]和[方向C]。
我可迁移的证据是[简要事实]，限制是[时间/预算/地区/风险]。
请结合最新市场证据，在我作出长期投入前设计最便宜且可能改变决定的实验。
```

**与目标岗位相关的技能、证书或课程选择**

```text
使用 $evidence-based-personal-advisor 判断[技能/证书/课程]是否是弥补
[目标岗位的具体差距]的最佳方式。结合近期JD比较价格、时间、替代项目或作品证据，
并告诉我应该立即学习、先低成本验证、下一步构建还是暂缓。
```

## 7. 工作原理

```text
你的问题与个人材料/描述
        │
        ▼
明确决定与研究预算
        │
        ▼
核心结论 → 最佳来源类型 → 最新证据
        │
        ▼
去重、可信度与矛盾检查
        │
        ▼
市场证据 ↔ 你的可检查证据
        │
        ▼
一个方向 → ≤3项立即行动 → 复盘闭环
```

职业分析进一步使用：

```text
JD要求 → 需求带 → 候选人证据 → 证据等级
→ 差距类型 → 建议证明方式 → 行动优先级
```

候选人证据使用独立的A/B/C/D/U等级，避免“市场来源很可靠”被错误转化为“候选人已经具备这项技能”。

## 8. 技术设计与壁垒

真正的壁垒不是模型数量，而是流程、边界和评测的组合：

1. **结论—来源路由**：行业趋势、招聘规模、岗位要求、薪酬信号和从业摩擦使用不同来源层级。
2. **双证据轴**：市场来源可信度与候选人证据强度始终分开。
3. **JD标准化与去重**：跨平台转载只计一次，必需与加分项分开，发布时间与页面刷新时间分开。
4. **先证据、后模型**：只在收集证据后选择商业、学术或实践模型；不能改变行动的模型会被删除。
5. **控制认知负担**：首屏只有一个方向、最多三项行动、投入和完成标准。
6. **失败可见**：平台受阻、样本不足、来源矛盾和访问失败会被明确报告。
7. **四层验证**：结构有效、行为符合、优于基础提示、改善真实结果是四种不同主张。
8. **隐私友好的评测**：本地JSONL只汇总评分、成本和失败，不要求把简历或原始提示放入公开仓库。

完整运行和评测结构见[ARCHITECTURE.md](ARCHITECTURE.md)。

## 9. 隐私、限制与注意事项

### 隐私

- 仓库不会接收或收集你的简历和评测记录。
- 本地安装不等于离线推理。ChatGPT、Codex、Claude、DeepSeek及启用的工具可能把材料发送给各自配置的提供商或服务。
- Skill要求当前Agent不要把简历原文、身份信息、联系方式和机密记录放入网页搜索。
- 这是提示层约束，不是网络沙箱；风险较高时应检查生成的查询。
- DeepSeek适配器会把标准输入中的脱敏请求以及内联Skill指令发送到配置的DeepSeek端点，但不会自动读取或上传简历文件。

### 检索限制

- 招聘平台可能要求登录、返回个性化结果、阻止自动访问或保留过期页面。
- Skill不包含BOSS直聘、LinkedIn或Indeed专用爬虫，只使用当前Agent环境可用的网络能力。
- 不同Agent的登录状态、浏览器访问、内置搜索、文件解析和引用行为并不相同。
- DeepSeek API适配器需要加载更多指令Token，不能完全复现文件系统Skill的渐进式加载。
- JD样本是便利样本，不是具有统计代表性的劳动力市场调查。
- 招聘广告频率只能作为方向信号，不等于全部招聘数量。
- 分析模型用于组织思考，不负责证明事实。
- 最新来源仍可能错误、不完整或被误读。

### 用户责任

- 行动或提交材料前，检查关键结论和生成的职业内容。
- 不接受虚构的指标、个人贡献、证书或结果。
- 遵守所访问网站和数据来源的服务条款。
- 不把本工具的岗位适配判断理解为录用概率或结果保证。

安全和私下报告方式见[SECURITY.md](SECURITY.md)。

## 10. 当前验证状态

| 证据层级 | 当前状态 |
|---|---|
| 仓库结构与隐私检查 | 已在本地通过；已配置GitHub CI工作流 |
| Codex与Claude Code安装器 | 已通过隔离的本地安装测试 |
| ChatGPT与Claude压缩包生成 | 已通过压缩包结构检查 |
| DeepSeek API适配器 | 载荷与解析自测通过；尚未发布真实账号调用结果 |
| 不同模型/工具下稳定遵循规则 | 已有9个场景，尚未发布可重复结果 |
| 优于不使用Skill的中性基础提示 | 尚未证明 |
| 改善真实用户结果 | 尚未证明 |

这里不会出现虚构的使用人数。在至少获得10组成对任务和10位相关用户的有效数据前，准确度、行动性和Token节省都只是设计目标，不是已经证明的优势。

测试本地评测组件：

```bash
python3 skills/evidence-based-personal-advisor/scripts/summarize_evals.py --self-test
python3 skills/evidence-based-personal-advisor/scripts/summarize_evals.py --template
```

收集结果前请阅读[效果评测与用户反馈协议](skills/evidence-based-personal-advisor/references/evaluation-and-user-feedback.md)。原始提示、简历、雇主身份和模型完整输出不能放入公开仓库。

## 11. 维护与故障排查

| 问题 | 先检查 | 下一步 |
|---|---|---|
| 找不到`python3` | 运行`python --version` | Windows改用`python`，或安装受支持的Python版本 |
| 验证失败 | 查看第一条缺失文件、链接、本地路径或密钥提示 | 只修复对应项目，不要绕过验证 |
| 目标目录已存在 | 安装器正在保护现有版本 | 按上面的备份升级流程操作 |
| 文件存在但Codex没有显示Skill | 确认父目录是当前环境的Skill目录 | 新建任务、显式调用，然后在需要时重启Codex |
| 指定招聘平台无法访问 | 检查登录和平台限制 | 提供导出的链接/文本，或接受范围更窄且明确标注的样本 |
| ChatGPT压缩包无法安装 | 确认Plugin已经发布，或当前账号已启用开发/本地来源 | 验证`.codex-plugin/plugin.json`；生成压缩包不等于创建上架条目 |
| DeepSeek在回答前报错 | 检查API密钥、端点、模型可用性和账号权限 | 先运行`--self-test`，重试时不要把个人信息写入日志 |
| 输出太长 | 指定`quick`并说明每周可用时间 | 只要求结论、三项行动和最大不确定性 |
| 简历分析出现虚构内容 | 立即停止使用该输出 | 删除不支持的内容并提交脱敏Bug报告 |

## 项目文件

```text
evidence-based-personal-advisor/
├── .codex-plugin/plugin.json            # ChatGPT/Codex通用Plugin清单
├── adapters/deepseek/run.py              # DeepSeek Responses API适配器
├── skills/evidence-based-personal-advisor/
│   ├── SKILL.md                         # 核心决策路由
│   ├── agents/openai.yaml               # Codex界面元数据
│   ├── references/                      # 按需加载的专业规则
│   ├── evals/cases.yaml                 # 9个行为测试场景
│   └── scripts/summarize_evals.py       # 本地成对结果汇总器
├── examples/                            # 明确标注边界的示例
├── scripts/install.py                   # 事务式安装器
├── scripts/package_skill.py             # ChatGPT与Claude压缩包生成器
├── scripts/validate_repo.py             # 结构与隐私检查
├── ARCHITECTURE.md
├── ROADMAP.md
├── CHANGELOG.md
└── .github/                             # CI、Issue表单和PR清单
```

## 参与贡献与许可证

欢迎提交真实失败、清晰度改进、行为测试、翻译和保护隐私的汇总评测。请先阅读[CONTRIBUTING.md](CONTRIBUTING.md)并遵守[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。

[MIT](LICENSE)。欢迎使用、检查和修改，也欢迎报告它在哪里失败。
