# 🎓 PhD 套瓷助手技能

> 全自动PhD申请套瓷系统：搜集北美导师、生成个性化套磁信、自动邮件发送

[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![Version](https://img.shields.io/badge/version-1.0.0-green)](https://clawhub.ai)

---

## ✨ 特性亮点

- 🔍 **智能导师搜集** - 自动筛选北美 3D Vision 方向教授
- 📝 **个性化套磁信** - 为每位教授生成针对性邮件（正式版+简洁版）
- 📤 **一键发送** - 集成 QQ Mail Monitor，简化发送流程
- 🎯 **精准筛选** - 自动过滤top-tier学校，聚焦合适目标
- 📊 **进度追踪** - 管理已联系和待联系的教授

---

## 🚀 快速开始

### 1. 安装技能

```bash
# 在 OpenClaw 中
openclaw skill install phd-outreach
```

### 2. 配置信息

```bash
# 复制配置模板
cp config.example.json config.json

# 编辑 config.json 填写你的信息
```

### 3. 开始使用

告诉 OpenClaw：

> "帮我搜集PhD导师"

或：

> "为 [教授姓名] 写套磁信"

---

## 📖 使用指南

### 完整工作流程

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  1. 搜集导师  │ → │  2. 写套磁信  │ → │  3. 发送邮件  │
└─────────────┘    └─────────────┘    └─────────────┘
```

#### Step 1: 搜集导师

```bash
python3 scripts/workflow.py search
```

系统生成搜索提示词，使用 OpenClaw 的 Bing 搜索（WebSearch/Bing）搜索符合条件的教授。

#### Step 2: 生成套磁信

```bash
python3 scripts/workflow.py email "Professor Name"
```

系统生成写作提示词，结合你的信息和教授研究方向生成个性化邮件。

#### Step 3: 发送邮件

```bash
python3 scripts/workflow.py send
```

系统生成发送脚本，调用 QQ Mail Monitor 发送邮件。

---

## 🎯 研究方向

本技能针对以下 PhD 申请方向优化：

- **3D Computer Vision**
- **Neural Rendering** / **3D Gaussian Splatting**
- **3D Reconstruction**
- **Novel View Synthesis**
- **Image Matching**
- **Geometry-based Vision**

---

## 🔧 配置说明

### 学生信息 (config.json)

```json
{
  "studentInfo": {
    "name": "你的名字",
    "university": "当前学校",
    "major": "Computer Science",
    "research_interests": "3D Computer Vision, Neural Rendering",
    "research_experience": [
      "3D Gaussian Splatting acceleration",
      "Feed-forward 3D reconstruction"
    ],
    "publications": ["论文1", "论文2"],
    "skills": "PyTorch, CUDA, Python",
    "target_degree": "PhD",
    "target_semester": "Fall 2026",
    "resume_path": "./docs/CV.pdf"
  }
}
```

### 搜索配置

默认配置：
- ✅ 北美学校（USA/Canada）
- ❌ 排除 MIT/Stanford/CMU/Berkeley/Caltech
- ✅ 聚焦排名 20-100 的学校
- ✅ 15-25 位教授推荐

---

## 📁 文件结构

```
phd-outreach-1.0.0/
├── _meta.json                  # 技能元数据
├── SKILL.md                    # 技能说明
├── README.md                   # 使用文档
├── requirements.txt            # 依赖
├── config.example.json         # 配置示例
└── scripts/
    ├── workflow.py             # 完整工作流 ⭐
    ├── search_professors.py    # 导师搜集
    ├── generate_email.py       # 套磁信生成
    └── send_outreach.py        # 邮件发送
```

---

## 💡 使用示例

### 示例 1：搜索导师

```
用户：帮我搜集PhD导师

助手：已生成搜索提示词，正在搜索符合条件的教授...

结果：找到20位潜在导师，信息已保存到 outreach/professors/
```

### 示例 2：生成套磁信

```
用户：为 Prof. John Smith 写套磁信

助手：已生成个性化套磁信（正式版 + 简洁版），包含：
- 3个可选标题
- 正式版邮件（280词）
- 简洁版邮件（180词）
- 写作策略总结

请确认后发送...
```

### 示例 3：发送邮件

```
用户：发送套磁信给 Prof. Smith

助手：邮件已发送！
- 收件人：jsmith@university.edu
- 主题：PhD Application - Research Interest in 3D Gaussian Splatting
- 附件：CV.pdf

已在发送记录中标记。
```

---

## ⚠️ 注意事项

1. **邮件个性化**
   - 每封邮件必须体现对教授研究的了解
   - 避免群发模板
   - 必须提及具体论文或项目

2. **发送策略**
   - 建议每天发送 3-5 封
   - 避免同时联系同一学校的多位教授
   - 跟进邮件间隔至少 1-2 周

3. **附件管理**
   - 确保 CV PDF 路径正确
   - CV 文件大小建议 < 2MB
   - 文件名使用英文

---

## 🆘 故障排查

### 问题：找不到教授信息

**解决：**
- 检查搜索提示词是否正确
- 尝试不同的搜索关键词
- 手动补充教授信息

### 问题：生成的邮件太模板化

**解决：**
- 在提示词中填写更多匹配点
- 提及教授的具体论文
- 详细描述你的相关研究经历

### 问题：邮件发送失败

**解决：**
- 检查 QQ Mail Monitor 是否已配置
- 确认授权码正确
- 检查网络连接

---

## 📄 许可证

MIT License

---

## 🙏 致谢

- [OpenClaw](https://openclaw.ai) - 技能框架
- [ClawHub](https://clawhub.ai) - 技能平台
- QQ Mail Monitor - 邮件发送

---

**版本：** 1.0.0
**更新时间：** 2026-04-10
**作者：** OpenClaw Community
