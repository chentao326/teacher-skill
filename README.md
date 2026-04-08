# 老师.skill

> 好老师不是告诉你答案的人，是帮你找到答案的人。

[安装](#安装) · [使用](#使用) · [效果示例](#效果示例) · [English](README_EN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Multi-Platform](https://img.shields.io/badge/Multi--Platform-5%20Platforms-orange)]()

---

把一份文档、一本书、一门课程丢给 AI，它会像一位耐心的老师一样，先了解你的基础，再用你能听懂的方式，一步步教会你。

不假设你"应该知道"什么，不急于给答案，不跳过任何一步。每个知识点讲完都会确认你真的懂了，然后再往下走。

---

## 安装

### Claude Code

```bash
# 项目级（仅当前项目可用）
mkdir -p .claude/skills
git clone https://github.com/yourname/teacher-skills .claude/skills/teacher-skills

# 全局（所有项目可用）
git clone https://github.com/yourname/teacher-skills ~/.claude/skills/teacher-skills
```

> **重要**：Claude Code 从 git 仓库根目录扫描 `.claude/skills/`，请确保目录结构正确。

### OpenAI Codex CLI

```bash
# 启用 skills 功能
codex --enable skills

# 项目级
mkdir -p .codex/skills
git clone https://github.com/yourname/teacher-skills .codex/skills/teacher-skills

# 全局
git clone https://github.com/yourname/teacher-skills ~/.codex/skills/teacher-skills
```

### OpenCode

```bash
# 项目级
mkdir -p .opencode/skills
git clone https://github.com/yourname/teacher-skills .opencode/skills/teacher-skills

# 个人级
git clone https://github.com/yourname/teacher-skills ~/.config/opencode/skills/teacher-skills
```

### OpenClaw

```bash
git clone https://github.com/yourname/teacher-skills ~/.openclaw/workspace/skills/teacher-skills
# 重启 Gateway 生效
```

### TRAE

TRAE 使用 Rules 系统而非 Skills 目录。将 `SKILL.md` 复制为规则文件：

```bash
mkdir -p .trae/rules
cp teacher-skills/SKILL.md .trae/rules/teacher.md
```

在规则文件顶部添加 TRAE 元数据：

```yaml
---
description: "AI老师：给定资料后像老师一样教会用户理解内容，支持学情诊断和分级教学"
alwaysApply: false
priority: 2
---
```

在聊天中用 `#teacher` 引用。

---

## 环境要求

- Node.js 18+（Claude Code / Codex CLI 依赖）
- Claude Pro/Max 订阅或 Anthropic API Key（Claude Code）
- OpenAI API Key（Codex CLI）
- Python 3.9+（可选，仅进度追踪脚本需要）

---

## 使用

安装完成后，对 AI 说：

```
教我这份文档的内容
```

然后粘贴或上传你的资料。AI 会自动进入教学流程。

你也可以直接指定主题：

```
/teacher 机器学习
```

### 模仿名师风格

如果你想 AI 用某位老师的教学风格来教你：

```
用这个风格教我线性代数
```

然后上传课程字幕文件（SRT/VTT/TXT），或提供视频链接（YouTube/Bilibili）。

AI 会自动分析该教师的教学风格（句式、词汇、节奏、互动方式等），然后用这种风格教你。

```
❯ 用这个风格教我（上传某名师的课程字幕）

   我正在分析这份教学素材...

   风格分析完成。这位老师的教学风格是：
   "用密集的短句和生活化的类比拆解复杂概念，
    每讲完一个知识点就用反问确认理解，口头禅是'对吧？'和'很简单'。"

   接下来我会用这种风格教你。如果觉得模仿得不像，
   可以提供更多素材让我调整。
```

### 管理命令

| 命令 | 说明 | 示例 |
|------|------|------|
| `/teacher status` | 查看当前学习进度 | `/teacher status` |
| `/teacher reset` | 重置学习会话 | `/teacher reset` |
| `/teacher level` | 手动调整能力等级 | `/teacher level advanced` |
| `/teacher skip` | 跳过当前单元 | `/teacher skip` |
| `/teacher review` | 回顾已学内容 | `/teacher review` |
| `/teacher quit` | 结束当前学习 | `/teacher quit` |
| `/teacher style` | 查看当前教学风格档案 | `/teacher style` |
| `/teacher style off` | 关闭风格模仿 | `/teacher style off` |
| `/teacher style more` | 增强风格模仿强度 | `/teacher style more` |
| `/update-teacher {slug}` | 追加新材料进化教学档案 | `/update-teacher wang-laoshi` |
| `/list-teachers` | 列出所有已创建的教学档案 | `/list-teachers` |
| `/teacher rollback {v}` | 回滚到指定版本 | `/teacher rollback v3` |

---

## 效果示例

> 输入：教我这份 PDF 的内容（上传《线性代数应该这样学》第三章）

```
❯ 我已经收到了你的资料，让我先看看内容。

   这份资料是《线性代数应该这样学》第三章，主要讲的是"线性映射"。
   大约包含 5 个核心知识点。学完之后你将能够理解什么是线性映射、
   如何判断一个映射是否线性、以及矩阵如何表示线性映射。

   在开始之前，我想先了解一下你的情况——
   你之前学过线性代数吗？了解多少？
```

```
❯ 学过一点点，但矩阵那些东西已经记不清了...

   明白。根据我们的交流，我判断你在"线性代数"领域属于中等基础。
   我会用脚手架式教学法来教你：先帮你梳理框架，再逐步深入。
   如果觉得太快或太慢，随时告诉我。

   我们大概会按这个顺序来学：
   ① 线性映射的定义（什么是线性映射）
   ② 判断线性映射的方法
   ③ 线性映射的核与像
   ④ 矩阵表示
   ⑤ 总结与练习

   准备好了吗？我们从①开始。
```

```
❯ 好的

   来看第一个概念：线性映射。

   你可以把它想象成一个"规则"——它接受一个输入向量，
   然后按照某种固定的方式，输出另一个向量。

   但这个"规则"有两个硬性要求：
   1. 加法保持：f(u + v) = f(u) + f(v)
   2. 数乘保持：f(cu) = c · f(u)

   用大白话说就是：先加再变 = 变完再加，先乘再变 = 变完再乘。

   到目前为止能跟上吗？
```

---

## 功能特性

### 学情诊断

通过自然对话评估用户的学习能力，不让人感觉在"考试"。

| 能力等级 | 判断依据 | 教学策略 |
|---------|---------|---------|
| 🔴 弱基础 | 完全零基础，领域术语陌生 | 讲授式 + 大量类比 + 小步快跑 |
| 🟡 中等基础 | 有模糊印象，概念不清晰 | 脚手架式 + 渐进练习 |
| 🟢 强基础 | 能准确描述核心概念 | 探究式 + 挑战性练习 |

诊断不是一次性的。教学过程中会根据用户表现持续修正判断，支持动态升级或降级。

### 三级教学策略

| | 🔴 弱基础 | 🟡 中等基础 | 🟢 强基础 |
|---|----------|-----------|----------|
| **方法** | 讲授式 + 大量类比 | 脚手架式 | 探究式 |
| **讲解/练习** | 70% / 30% | 50% / 50% | 30% / 70% |
| **检查方式** | 选择题/判断题 | 复述题/应用题 | 分析题/设计题 |
| **节奏** | 慢，每步都检查 | 中等，每概念检查 | 快，每2-3概念检查 |

### 通俗化讲解

内置万能类比库，将抽象概念翻译成日常语言：

| 抽象概念 | 类比 |
|---------|------|
| 算法 | 菜谱 |
| 缓存 | 冰箱 |
| 递归 | 俄罗斯套娃 |
| API | 餐厅服务员 |
| 容器(Docker) | 集装箱 |
| 版本控制(Git) | 游戏存档 |

### 进化机制

教学档案创建后支持三种进化方式：

- **追加材料**：提供新的课程资料，增量 merge 进现有档案，不覆盖已有结论
- **对话纠正**：说"这不对"/"老师不会这样说"，立即生效并记录 Correction
- **版本管理**：每次更新自动存档，最多保留 10 个历史版本，支持回滚

### 风格模仿

上传课程字幕或提供视频链接，AI 自动提取教师的教学风格并模仿：

| 输入方式 | 说明 |
|---------|------|
| 课程字幕（SRT/VTT/TXT） | 最佳，直接上传文件 |
| 视频链接（YouTube/Bilibili） | 自动提取字幕（需安装 yt-dlp） |
| 文字稿/文章 | 直接粘贴教学文本 |

风格分析覆盖六个维度：句式结构、词汇特征、教学节奏、互动模式、内容组织、情感态度。

> **依赖**：视频字幕提取需要 `yt-dlp`（`pip install yt-dlp`）。如果视频没有字幕，请上传课程字幕文件。

---

## 项目结构

```
teacher-skills/
├── SKILL.md                              # 主入口：教学调度器 + 完整SOP
├── README.md                             # 中文文档
├── README_EN.md                          # 英文文档
├── LICENSE                               # MIT 许可证
│
├── config/
│   └── skill-config.json                 # 项目配置
│
├── prompts/
│   ├── intake.md                       # 教师信息录入（3问+教学标签库）
│   ├── style-extractor.md              # 教学风格六维度提取指南
│   ├── style-profile-template.md       # 教学风格档案模板
│   ├── teaching_analyzer.md            # 教学风格分析 Prompt
│   ├── teaching_builder.md             # 教学档案生成模板（Layer 0-5）
│   ├── merger.md                       # 增量 Merge Prompt
│   └── correction_handler.md           # 对话纠正处理
│
├── scripts/
│   ├── generate_quiz.py                # 练习题生成（按等级/题型）
│   ├── evaluate_answer.py              # 答案评估 + 反馈模板
│   ├── track_progress.py               # 学习进度追踪
│   ├── extract_subtitle.py             # 视频/字幕提取工具
│   └── skill_writer.py                 # 教学档案文件管理器
│
├── ref/
│   ├── learner-diagnosis.md              # 学情诊断指南
│   ├── teaching-strategies.md            # 三级教学策略（强/中/弱）
│   ├── teaching-techniques.md            # 通俗化讲解技巧 + 类比库 + 表达DNA
│   └── question-templates.md             # 出题模板库
│
├── adapters/
│   └── trae-teacher.md                   # TRAE 平台适配文件
│
└── subjects/
    ├── _template-SKILL.md                # 学科子Skill模板（可复用）
    ├── math-teacher-SKILL.md             # 数学教学策略
    └── programming-teacher-SKILL.md      # 编程教学策略
```

---

## 扩展学科

复制模板创建新的学科子 Skill：

```bash
cp subjects/_template-SKILL.md subjects/your-subject-SKILL.md
```

编辑 `your-subject-SKILL.md`，填入学科特有的教学策略、常见误解和练习设计。

---

## 注意事项

- ⚠️ 本 Skill 不替代专业教育。复杂学科建议结合正规课程使用。
- ⚠️ AI 可能产生知识幻觉。对关键信息建议回查原始资料。
- 所有教学数据仅本地存储，不会上传至任何服务器。
- 支持的资料格式：PDF、TXT、Markdown、HTML、DOCX、EPUB

---

## 社区生态

| 项目 | 描述 |
|------|------|
| [ex-skill](https://github.com/therealXiaomanChu/ex-skill) | 前任.skill — 灵感来源 |
| [colleague-skill](https://github.com/titanwings/colleague-skill) | 同事.skill — 职场关系蒸馏 |
| [awesome-persona-skills](https://github.com/tmstack/awesome-persona-skills) | 万物皆可 skill 合集 |
| [superpowers](https://github.com/obra/superpowers) | Claude Code 增强技能包 |

---

### 写在最后

教育的本质不是灌满一桶水，而是点燃一把火。

但现实中，大多数人的学习体验是：打开一本厚厚的教材，翻了两页就困了；看了一堆视频教程，关掉之后什么都没记住；问 AI 一个概念，它甩给你一段百科全书式的回答，看完更懵了。

这个 Skill 想做的事情很简单：**让 AI 像一个真正的好老师那样教你**。

不是因为它更聪明，而是因为它更有耐心。它会等你跟上，会换不同的方式解释同一个概念，会在你不懂的时候停下来而不是继续往下讲。它不假设你"应该知道"什么——因为好的老师从不这样。

如果你曾经因为"没人教"而放弃学某个东西，也许可以再试一次。
