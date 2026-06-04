---
name: reverse-distillation-guide
description: >
  反蒸馏操作指引：将任何 AI Skill（来自 awesome-persona-skills 等仓库）
  转化为人类可学的教学课程。包括完整的检查清单、分析框架和输出规范。
version: 2.1.0
---

# 反蒸馏操作指引

## 什么是反蒸馏

AI 领域有一个爆发的生态：**人格蒸馏 Skill**——把某个人/角色的思维模式、表达方式、知识体系蒸馏为 SKILL.md 文件，让 AI 能扮演该角色。

反蒸馏做的恰好相反：**把 Skill 中的可教知识提取出来，按照 teacher-skill 的教学流程，教会人类这些知识和思维方式。**

| | 蒸馏（现有生态） | 反蒸馏（本模块） |
|--|----------------|----------------|
| 目标 | 让 AI 学会 X 的思维方式 | 让人类学会 X 的思维方式 |
| 产物 | SKILL.md（AI 指令） | subjects/xxx-teacher-SKILL.md（课程） |
| 使用者 | AI Agent | 人类学习者 |
| 可迁移性 | 绑定 AI 和平台 | 你的大脑随时可用 |

## 触发条件

- 用户说"把这个 skill 反蒸馏成课程"、"把这个 skill 变成可教的内容"
- 用户提供一个 skill 的 GitHub URL 或本地文件路径
- 用户说"试试反蒸馏"
- 用户说"教我这个 skill 里包含的知识"
- 用户说"把这几个 skill 合并成一个课程"

## 操作流程

### Step 0：确认来源

用户可能从以下仓库提供 skill URL：

- https://github.com/tmstack/awesome-persona-skills（65+ 技能合集）
- https://github.com/momozi1996/awesome-ai-persona-skills（100+ 技能，含 24 作家、13 大V）

确认用户要反蒸馏的是哪个 skill，以及是否有特定的学习目标。

### Step 1：分析源 Skill

使用 `scripts/reverse_distill.py --analyze <url>` 分析 skill 文件。

```bash
python scripts/reverse_distill.py --analyze https://github.com/will2025btc/buffett-perspective
```

分析结果会输出：

1. **Skill 基本信息**：名称、类型（thinking/persona/writing）、行数
2. **心智模型**：检测到的核心模型列表（名称 + 概要 + 核心理念）
3. **可教性评分**：1-10 分，越高代表越适合教学
4. **分析文件**：自动保存到 `ref/analysis-{name}.json`

> **注意**：分析是机械性质的——提取心智模型标题和引用。完整的内容（生活类比、检测练习、模块设计）需要你（AI）基于分析结果进一步补充。

### Step 2：判断 skill 类型

分析结果出来后，判断这个 skill 适合哪种反蒸馏方式：

| skill 类型 | 特征 | 反蒸馏策略 | 示例 |
|-----------|------|-----------|------|
| **thinking（思维型）** | 有心智模型、决策启发式 | 按心智模型拆分为教学模块 | 巴菲特、芒格、费曼 |
| **persona（角色型）** | 有身份卡、角色扮演规则 | 提取角色背后的知识体系和思维，角色扮演本身不教学 | 鲁迅、郭德纲、同事 |
| **writing（写作型）** | 有表达 DNA、文风分析 | 作为写作/表达训练课程 | 作家群、自媒体大V |

### Step 3：提取可教内容

根据 skill 类型，提取以下内容：

**所有类型都提取**：
- `name` 和 `description` → 课程名称和目标
- `triggers` → 教学的触发词

**思维型（thinking）额外提取**：
- 每个心智模型 → 一个教学模块
- 决策启发式 → 综合应用环节的素材
- 子步骤和工作流 → 训练路径

**角色型（persona）额外提取**：
- 角色的知识体系和专业领域 → 教学内容
- 角色的思维框架（如果有） → 教学模块
- 角色的语言特点 → 表达训练
- 角色的"擅长/不擅长" → 课程边界

**写作型（writing）额外提取**：
- 表达DNA → 写作方法教学
- 句式/词汇特征 → 写作练习
- 风格模仿 → 表达训练

### Step 4：补充教学模块

对于分析出的每个心智模型/知识模块，补充三个部分：

1. **概念讲解**：用 teacher-skill 的通俗类比风格，把每个模型用大白话解释清楚
2. **生活类比**：找一个日常生活中的例子，让抽象概念变得可感知
3. **检测练习**：设计 2-3 个练习，帮助用户自己验证是否理解了

检测练习参考 `ref/verification-framework.md` 的三种类型（A/B/C），根据用户能力等级选择。

### Step 5：输出课程文件

使用 `scripts/reverse_distill.py --generate <name>` 先生成**骨架文件**：

```bash
python scripts/reverse_distill.py --analyze <url> --generate <subject-name>
```

这会在 `subjects/` 下生成 `<subject-name>-teacher-SKILL.md`，包含：
- 完整的 frontmatter（name/description/triggers）
- 每个心智模型的名称和原始描述
- 需要补充的"生活类比"和"检测练习"占位符

然后**人工（AI）补充**：
- 每个模块的生活化类比
- 检测练习题（3 个类型 A/B/C 中选）
- 跨学科连接（参考 `ref/cross-disciplinary-thinking.md`）

### Step 6：集成到 teacher-skill

新学科文件生成后，更新 `SKILL.md` 中的学科引用表，添加新学科的触发词。

### Step 7：验证

验证生成的教学文件：
1. frontmatter 格式是否正确（name/description/triggers）
2. 每个模块是否有概念讲解 + 类比 + 练习
3. 是否包含分级教学重点（弱/中/强）
4. 整体流程是否走通（Phase 1→2→3→4→5）

## 反蒸馏检查清单

每反蒸馏一个 skill 后，用这个清单检查质量：

- [ ] 心智模型/核心知识被完整提取，没有遗漏
- [ ] 每个模型都有用大白话写的概念讲解
- [ ] 每个模型都有至少一个生活化类比
- [ ] 每个模型都有检测练习（类型 A/B/C 按能力选择）
- [ ] 有跨学科连接的标注（可选但推荐）
- [ ] 有分级教学重点（弱/中/强）
- [ ] 包含"诚实边界"——这个课程教不了什么
- [ ] 已在 SKILL.md 中注册触发词
- [ ] 用户可以用"教我 [skill名称]"触发

## 示例

完成的反蒸馏课程示例：

- `subjects/feynman-teacher-SKILL.md`（费曼思维，完整反蒸馏示例）
- `subjects/buffett-teacher-SKILL.md`（生成中，骨架已就绪）

## 已知的反蒸馏资源

| 源仓库 | 可用 skill 数 | 典型可反蒸馏 skill |
|--------|-------------|------------------|
| awesome-persona-skills (tmstack) | ~65 | 巴菲特、芒格、费曼、纳瓦尔、乔布斯 |
| awesome-ai-persona-skills (momozi1996) | 100+ | 24 位作家、13 位自媒体大V、天涯20大神 |
| 女娲.skill 生态 | ~50 | 各种思维型 skill |

## 反蒸馏的边界

**适合反蒸馏**：
- 包含明确心智模型/思维框架的 skill（巴菲特、费曼、芒格）
- 包含系统知识体系的 skill（永乐大典、毛选、金刚经）
- 包含可训练的表达方法的 skill（作家技能、自媒体 skill）

**不适合反蒸馏**：
- 纯情感陪伴型 skill（"舔狗.skill""重逢.skill"——目标是陪伴，不是教学）
- 纯角色扮演型 skill（无实质知识内容，只是风格模仿）
- 纯工具型 skill（"女娲.skill""饕餮.skill"——它们是元 skill，不是教学内容）
