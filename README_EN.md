# Teacher.skill

> A good teacher isn't someone who gives you answers — it's someone who helps you find them.

[中文](README.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)
[![Version](https://img.shields.io/badge/version-2.7.0-blue)]()
[![Subjects](https://img.shields.io/badge/subjects-10-orange)]()
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Multi-Platform](https://img.shields.io/badge/Multi--Platform-5%20Platforms-orange)]()

---

Throw a document, book, or course at an AI — it will teach you like a patient teacher. First it assesses your level, then it explains concepts in ways you can actually understand, step by step.

It never assumes you "should know" something, never jumps to the answer, and never skips a step. After each concept, it checks that you truly understand before moving on.

**v2.7 core capabilities**: Say "teach me how Buffett thinks" — auto-search skills from open-source repos, extract mental models, generate curriculum, and start teaching. Supports learning progress persistence, deliberate practice loops, Ebbinghaus spaced repetition, progressive learning paths, and teaching error correction.

Now supports **10 subjects**: Math, Programming, Chinese, English, Physics, Chemistry, History, Biology, AI, and Feynman Thinking.

---

## Installation

### Claude Code

```bash
# Project-level (current project only)
mkdir -p .claude/skills
git clone https://github.com/chentao326/teacher-skill .claude/skills/teacher-skills

# Global (available to all projects)
git clone https://github.com/chentao326/teacher-skill ~/.claude/skills/teacher-skills
```

> **Important**: Claude Code scans `.claude/skills/` from the git repo root. Make sure the directory structure is correct.

### OpenAI Codex CLI

```bash
# Enable skills feature
codex --enable skills

# Project-level
mkdir -p .codex/skills
git clone https://github.com/chentao326/teacher-skill .codex/skills/teacher-skills

# Global
git clone https://github.com/chentao326/teacher-skill ~/.codex/skills/teacher-skills
```

### OpenCode

```bash
# Project-level
mkdir -p .opencode/skills
git clone https://github.com/chentao326/teacher-skill .opencode/skills/teacher-skills

# User-level
git clone https://github.com/chentao326/teacher-skill ~/.config/opencode/skills/teacher-skills
```

### OpenClaw

```bash
git clone https://github.com/chentao326/teacher-skill ~/.openclaw/workspace/skills/teacher-skills
# Restart Gateway to apply
```

### TRAE

TRAE uses Rules system instead of Skills directory. Copy `SKILL.md` as a rule file:

```bash
mkdir -p .trae/rules
cp teacher-skills/SKILL.md .trae/rules/teacher.md
```

Add TRAE metadata at the top of the rule file:

```yaml
---
description: "AI teacher: teaches any given material with personalized pace and style"
alwaysApply: false
priority: 2
---
```

In chat, reference with `#teacher`.

---

## Requirements

- Node.js 18+ (for Claude Code / Codex CLI)
- Claude Pro/Max subscription or Anthropic API Key (Claude Code)
- OpenAI API Key (Codex CLI)
- Python 3.9+ (optional, only needed for progress tracking scripts)

---

## Usage

After installation, just tell your AI:

```
teach me this document
```

Then paste or upload your material. The AI will automatically enter the teaching workflow.

You can also specify a topic directly:

```
/teacher machine learning
```

### Imitating a Teacher's Style

Want the AI to teach in a specific instructor's style?

```
teach me linear algebra in this style
```

Then upload course subtitle files (SRT/VTT/TXT), or provide a video link (YouTube/Bilibili).

The AI will analyze the instructor's teaching style (sentence structure, vocabulary, pacing, interaction patterns, etc.) and teach in that style.

```
❯ 用这个风格教我（上传某名师的课程字幕）

   I'm analyzing this teaching material...

   Style analysis complete. This teacher's style is:
   "Uses dense short sentences and everyday analogies to break down complex concepts,
    confirms understanding with rhetorical questions after each point,
    catchphrases are 'right?' and 'it's simple'."

   I'll teach you in this style from now on.
   If it doesn't feel right, provide more material and I'll adjust.
```

### Management Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/teacher status` | View current progress | `/teacher status` |
| `/teacher reset` | Reset teaching session | `/teacher reset` |
| `/teacher level` | Manually set ability level | `/teacher level advanced` |
| `/teacher skip` | Skip current unit | `/teacher skip` |
| `/teacher review` | Review learned content | `/teacher review` |
| `/teacher quit` | End current session | `/teacher quit` |
| `/teacher style` | View current style profile | `/teacher style` |
| `/teacher style off` | Disable style imitation | `/teacher style off` |
| `/teacher style more` | Intensify style imitation | `/teacher style more` |
| `/update-teacher {slug}` | Append material to evolve profile | `/update-teacher prof-wang` |
| `/list-teachers` | List all created teaching profiles | `/list-teachers` |
| `/teacher rollback {v}` | Rollback to a specific version | `/teacher rollback v3` |

---

## Features

### Student Assessment

Assess the learner's ability through natural conversation, without making them feel like they're being "tested".

| Level | Indicators | Teaching Strategy |
|-------|-----------|------------------|
| 🔴 Beginner | No prior knowledge, unfamiliar with domain terms | Lecture + heavy analogies + small steps |
| 🟡 Intermediate | Vague familiarity, concepts not clear | Scaffolded instruction + progressive exercises |
| 🟢 Advanced | Can accurately describe core concepts | Inquiry-based + challenging exercises |

Assessment is not one-time. The AI continuously adjusts its diagnosis based on learner performance during the session.

### Three-Level Teaching Strategy

| | 🔴 Beginner | 🟡 Intermediate | 🟢 Advanced |
|---|-------------|-----------------|-------------|
| **Method** | Lecture + heavy analogies | Scaffolded instruction | Inquiry-based |
| **Lecture/Practice** | 70% / 30% | 50% / 50% | 30% / 70% |
| **Check method** | Multiple choice / True-false | Retell / Application | Analysis / Design |
| **Pacing** | Slow, check every step | Medium, check per concept | Fast, check every 2-3 concepts |

### Plain Language Teaching

Built-in analogy library that translates abstract concepts into everyday language:

| Abstract Concept | Analogy |
|-----------------|---------|
| Algorithm | Recipe |
| Cache | Refrigerator |
| Recursion | Russian nesting dolls |
| API | Restaurant waiter |
| Container (Docker) | Shipping container |
| Version Control (Git) | Game save points |

### Evolution Mechanism

Teaching profiles support three ways to evolve:

- **Append Material**: Provide new course material, incrementally merged into existing profile — never overwrites existing conclusions
- **Conversation Correction**: Say "that's not right" / "the teacher wouldn't say that" — takes effect immediately and records a Correction
- **Version Management**: Auto-archive before each update, keep up to 10 historical versions, supports rollback

### Style Imitation

Upload course subtitles or provide a video link — the AI automatically extracts the teacher's style and imitates it:

| Input Method | Description |
|-------------|-------------|
| Subtitles (SRT/VTT/TXT) | Best quality, upload file directly |
| Video link (YouTube/Bilibili) | Auto-extract subtitles (requires yt-dlp) |
| Transcript/Article | Paste teaching text directly |

Style analysis covers six dimensions: sentence structure, vocabulary, teaching pacing, interaction patterns, content organization, and emotional tone.

> **Dependency**: Video subtitle extraction requires `yt-dlp` (`pip install yt-dlp`). If the video lacks subtitles, please upload subtitle files directly.

### Cross-Disciplinary Thinking (v2.0 New)

No longer teaching subjects in isolation — networked knowledge connections are woven into the entire teaching workflow, helping learners build cross-disciplinary thinking habits.

| Capability | Description | When |
|-----------|-------------|------|
| **Knowledge Networking** | 12 core concepts mapped across 6+ disciplines (e.g. "feedback" in biology=homeostasis, in electronics=circuit, in programming=recursion) | Naturally woven into concept explanations |
| **Analogical Transfer** | Structured 3-step analogy: extract pattern from familiar domain → apply to new concept → verify understanding | When introducing new concepts |
| **Association Spark** | 3-sentence association exercise + cross-domain 5-questions + 10 cross-pollination cards (e.g. "If this concept were a product...") | Post-lesson review / periodic review |

Cross-disciplinary connections aren't extra burden — good cross-disciplinary teaching gives every concept "one more dimension." When you learn math and see echoes of physics, learn physics and catch hints of chemistry — knowledge comes alive.

See `ref/cross-disciplinary-thinking.md` for details.

---

## Project Structure

```
teacher-skills/
├── SKILL.md                              # Main entry: teaching orchestrator + full SOP
├── README.md                             # Chinese documentation
├── README_EN.md                          # English documentation
├── LICENSE                               # MIT License
│
├── config/
│   └── skill-config.json                 # Project configuration
│
├── prompts/
│   ├── intake.md                       # Teacher info intake (3 questions + tag library)
│   ├── style-extractor.md              # Teaching style 6-dimension extraction guide
│   ├── style-profile-template.md       # Teaching style profile template
│   ├── teaching_analyzer.md            # Teaching style analysis prompt
│   ├── teaching_builder.md             # Teaching profile generation template (Layer 0-5)
│   ├── merger.md                       # Incremental merge prompt
│   └── correction_handler.md           # Conversation correction handler
│
├── scripts/
│   ├── generate_quiz.py                # Quiz generator
│   ├── evaluate_answer.py              # Answer evaluation
│   ├── track_progress.py               # Progress tracker
│   ├── learning_state.py               # Learning state persistence (v2.1)
│   ├── reverse_distill.py              # Reverse-distillation tool (v2.1)
│   ├── extract_subtitle.py             # Subtitle extraction
│   └── skill_writer.py                 # Teaching profile manager
│
├── ref/
│   ├── learner-diagnosis.md              # Student assessment guide
│   ├── teaching-strategies.md            # Three-level teaching strategies
│   ├── teaching-techniques.md            # Plain language techniques + analogy library
│   ├── question-templates.md             # Question template library
│   ├── teaching-sop.md                   # Teaching SOP (main workflow Phase 0-5)
│   ├── management-commands.md            # Management commands
│   ├── verification-framework.md         # Teaching verification framework
│   ├── extraction-framework.md           # Unified extraction framework (v2.4)
│   ├── skill-to-curriculum-guide.md      # Skill-to-curriculum guide
│   ├── cross-disciplinary-thinking.md   # Cross-disciplinary thinking module (v2.0)
│   ├── deliberate-practice-research.md   # Deliberate practice research (v2.5)
│   ├── forgetting-curve-research.md      # Forgetting curve research (v2.6)
│   ├── nuwa-absorption.md               # Nuwa.skill absorption report
│   ├── reverse-distillation-report.md   # Reverse distillation research report
│   ├── unified-extraction-research.md    # Unified extraction research
│   └── improvement-roadmap.md            # Improvement roadmap
│
├── adapters/
│   └── trae-teacher.md                   # TRAE platform adapter
│
└── subjects/
    ├── _template-SKILL.md                # Subject skill template (reusable)
    ├── math-teacher-SKILL.md             # Math teaching strategy
    ├── programming-teacher-SKILL.md      # Programming teaching strategy
    ├── chinese-teacher-SKILL.md          # Chinese teaching strategy
    ├── english-teacher-SKILL.md          # English teaching strategy
    ├── physics-teacher-SKILL.md          # Physics teaching strategy
    ├── chemistry-teacher-SKILL.md        # Chemistry teaching strategy
    ├── history-teacher-SKILL.md          # History teaching strategy
    ├── biology-teacher-SKILL.md          # Biology teaching strategy
    ├── ai-teacher-SKILL.md               # AI / Artificial Intelligence
    └── feynman-teacher-SKILL.md          # Feynman Thinking (reverse-distilled) teaching strategy
```

---

## Available Subjects

| Subject | File | Coverage |
|---------|------|----------|
| Math | `subjects/math-teacher-SKILL.md` | Formula intuition, geometry visualization, proof strategies |
| Programming | `subjects/programming-teacher-SKILL.md` | Code thinking, debugging skills, project-driven learning |
| Chinese | `subjects/chinese-teacher-SKILL.md` | Classical Chinese, reading comprehension, writing |
| English | `subjects/english-teacher-SKILL.md` | Grammar, vocabulary, speaking, listening, test prep |
| Physics | `subjects/physics-teacher-SKILL.md` | Concept understanding, formulas, experimental thinking |
| Chemistry | `subjects/chemistry-teacher-SKILL.md` | Reactions, equations, lab skills, calculations |
| History | `subjects/history-teacher-SKILL.md` | Timelines, causal analysis, source interpretation |
| Biology | `subjects/biology-teacher-SKILL.md` | Cells, genetics, physiology, evolution, ecology |
| AI / AI时代 | `subjects/ai-teacher-SKILL.md` | LLM fundamentals, Prompt engineering, Agents, AI ethics |
| Feynman Thinking (reverse-distilled) | `subjects/feynman-teacher-SKILL.md` | Don't fool yourself, naming≠understanding, concrete thinking, deep play |

## Creating New Subjects

Copy the template and create a new subject skill:

```bash
cp subjects/_template-SKILL.md subjects/your-subject-SKILL.md
```

Edit `your-subject-SKILL.md` with your subject's unique teaching strategies, common misconceptions, and exercise design. PRs for new subjects are welcome!

---

## Notes

- ⚠️ This Skill does not replace professional education. Use with formal curricula for complex subjects.
- ⚠️ AI may produce hallucinations. Cross-reference critical information against original sources.
- All teaching data is stored locally. Nothing is uploaded to any server.
- Supported formats: PDF, TXT, Markdown, HTML, DOCX, EPUB

---

## Community

| Project | Description |
|---------|-------------|
| [ex-skill](https://github.com/therealXiaomanChu/ex-skill) | Ex.skill — inspiration source |
| [colleague-skill](https://github.com/titanwings/colleague-skill) | Colleague.skill — workplace relationship distillation |
| [awesome-persona-skills](https://github.com/tmstack/awesome-persona-skills) | Curated collection of persona skills |
| [superpowers](https://github.com/obra/superpowers) | Claude Code enhancement skill pack |

---

### A Final Word

The essence of education is not filling a bucket, but lighting a fire.

In reality, most people's learning experience looks like this: opening a thick textbook, dozing off after two pages; binge-watching tutorial videos, remembering nothing after closing them; asking an AI a question, getting an encyclopedia-length answer that leaves you more confused than before.

This Skill exists to do one simple thing: **make AI teach you like a real, good teacher.**

Not because it's smarter, but because it's more patient. It will wait for you. It will explain the same concept in different ways. It will pause when you're lost instead of barreling ahead. It never assumes you "should know" something — because good teachers never do.

If you've ever given up on learning something because "no one was there to teach you" — maybe try again.
