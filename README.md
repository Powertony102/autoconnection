# OpenClaw - 全自动PhD套瓷助手

OpenClaw 是一个全自动PhD申请套瓷系统，帮助用户完成从导师搜集到套磁信发送的完整流程。

## 项目结构

```
autoconnection/
├── phd-outreach-1.0.0/         # 🎓 PhD套瓷技能 (主要功能)
│   ├── _meta.json
│   ├── SKILL.md
│   ├── README.md
│   ├── config.example.json
│   ├── requirements.txt
│   └── scripts/
│       ├── workflow.py         # 完整工作流
│       ├── search_professors.py
│       ├── generate_email.py
│       └── send_outreach.py
│
├── qq-mail-monitor-1.0.0/      # 📧 QQ邮箱监控技能 (依赖)
│   ├── _meta.json
│   ├── SKILL.md
│   └── scripts/
│       ├── qq_mail_send.py
│       ├── qq_mail_check.py
│       └── qq_mail_auto_check.py
│
├── .claude/                    # Claude Code 配置 (可选)
│   ├── settings.local.json
│   └── prompts/
│       ├── professor_search.md
│       └── email_writing.md
│
├── config.example.json         # 学生信息配置示例
└── README.md                   # 本文件
```

## 快速开始

### 1. 配置学生信息

```bash
cd phd-outreach-1.0.0
cp config.example.json config.json
# 编辑 config.json 填写你的信息
```

### 2. 使用 OpenClaw 命令

```bash
# 搜集导师
告诉 OpenClaw: "帮我搜集PhD导师"

# 生成套磁信
告诉 OpenClaw: "为 [教授姓名] 写套磁信"

# 发送邮件
告诉 OpenClaw: "发送套磁信给 [教授邮箱]"
```

### 3. 使用脚本

```bash
cd phd-outreach-1.0.0/scripts

# 生成搜索提示词
python3 workflow.py search

# 生成套磁信提示词
python3 workflow.py email "Professor Name"

# 查看发送指导
python3 workflow.py send
```

## 功能流程

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  配置信息   │  →  │  搜集导师   │  →  │ 生成套磁信  │  →  │  发送邮件   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
     │                    │                   │                   │
     ▼                    ▼                   ▼                   ▼
 config.json       15-25位教授        正式版+简洁版      QQ Mail Monitor
                 信息+论文+主页      个性化邮件内容         一键发送
```

## 核心技能

### phd-outreach-1.0.0

全自动PhD套瓷助手：
- 🔍 **导师搜集** - 搜索北美 3D Vision 方向教授
- 📝 **套磁信生成** - 个性化邮件（正式版+简洁版）
- 📤 **邮件发送** - 集成 QQ Mail Monitor
- 🎯 **精准筛选** - 自动排除top-tier学校

详见 [phd-outreach-1.0.0/README.md](phd-outreach-1.0.0/README.md)

### qq-mail-monitor-1.0.0

QQ邮箱监控和发送：
- 📧 邮件发送
- 📨 收件箱检查
- 📎 附件支持
- ⏰ 定时任务

详见 [qq-mail-monitor-1.0.0/README.md](qq-mail-monitor-1.0.0/README.md)

## 研究方向配置

默认针对以下方向优化：

- 3D Computer Vision
- Neural Rendering / 3D Gaussian Splatting
- 3D Reconstruction
- Novel View Synthesis
- Image Matching
- Geometry-based Vision

## 学校筛选策略

### 默认排除（太顶尖）
- MIT
- Stanford
- CMU
- UC Berkeley
- Caltech

### 优先推荐（排名20-100）
- University of Toronto
- University of Washington
- Georgia Tech
- UT Austin
- University of Michigan
- ...

## 输出目录

```
outreach/
├── professors/           # 搜集的导师信息
│   └── search_result_*.json
├── emails/              # 生成的套磁信
│   └── email_*.md
├── prompts/             # 生成的提示词
│   └── *.txt
└── scripts/             # 生成的发送脚本
    └── send_*.py
```

## 使用提示

### 最佳实践

1. **个性化每封邮件** - 不要群发，每封信都要体现对教授研究的了解
2. **控制发送频率** - 每天3-5封，避免同时联系同一学校多位教授
3. **准备好CV** - 确保简历PDF在配置的路径中
4. **跟进有度** - 1-2周后无回复可以跟进一次

### OpenClaw 指令示例

```
用户：帮我搜索做 Gaussian Splatting 的教授
OpenClaw：正在生成搜索提示词...
       [生成提示词用于WebSearch]

用户：为 University of Toronto 的 John Smith 写套磁信
OpenClaw：已生成写作提示词，包含：
       - 正式版邮件
       - 简洁版邮件
       - 写作策略

用户：发送刚才那封邮件
OpenClaw：已生成发送脚本，请确认教授邮箱地址...
```

## 配置说明

### config.json 结构

```json
{
  "studentInfo": {
    "name": "你的名字",
    "university": "当前学校",
    "major": "Computer Science",
    "research_experience": [
      "3DGS acceleration",
      "Feed-forward 3D reconstruction"
    ],
    "publications": [...],
    "skills": "PyTorch, CUDA",
    "target_semester": "Fall 2026",
    "resume_path": "./docs/CV.pdf"
  }
}
```

## License

MIT

## 更新日志

- **2026-04-10** - 创建 phd-outreach-1.0.0 技能
- **2026-03-02** - 添加 qq-mail-monitor-1.0.0 技能
