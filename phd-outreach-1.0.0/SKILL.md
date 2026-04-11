---
name: phd-outreach
description: "全自动PhD套瓷助手：搜集北美导师、生成个性化套磁信、自动邮件发送。适用于计算机视觉/3D Vision方向博士申请。"
---

# PhD 套瓷助手技能

全自动PhD申请套瓷系统，帮助你完成从导师搜集到邮件发送的完整流程。

## 📋 功能特性

| 功能 | 说明 |
|------|------|
| 🔍 导师搜集 | 搜索北美符合条件的 3D Vision 方向教授 |
| 📝 套磁信生成 | 为每位教授生成个性化邮件（正式版+简洁版） |
| 📤 邮件发送 | 集成 QQ Mail Monitor，一键发送邮件 |
| 📊 进度管理 | 追踪已联系和待联系的教授 |
| 🎯 精准筛选 | 自动过滤top-tier学校，聚焦20-100排名 |

## 🎯 适用方向

- 3D Computer Vision
- Neural Rendering / 3D Gaussian Splatting
- 3D Reconstruction
- Novel View Synthesis
- Image Matching
- Geometry-based Vision

## 🛠️ 工具脚本

### 1. workflow.py - 完整工作流

**用途：** 整合所有功能的完整工作流

**使用方法：**
```bash
# 显示使用指南
python3 workflow.py

# 生成导师搜集提示词
python3 workflow.py search

# 生成套磁信提示词
python3 workflow.py email [教授姓名]

# 发送邮件指导
python3 workflow.py send
```

### 2. search_professors.py - 导师搜集

**用途：** 生成搜索提示词，帮助搜集符合条件的教授

**使用方法：**
```bash
python3 search_professors.py
```

**输出示例：**
```
🔍 PhD 导师搜集工具

此工具需要在 OpenClaw 环境中运行，使用系统的搜索能力。
搜索提示词已生成...
```

### 3. generate_email.py - 套磁信生成

**用途：** 生成个性化套磁信写作提示词

**使用方法：**
```bash
python3 generate_email.py
```

### 4. send_outreach.py - 邮件发送

**用途：** 生成邮件发送脚本，集成 QQ Mail Monitor

**使用方法：**
```bash
# 列出待发送邮件
python3 send_outreach.py

# 生成发送脚本后会显示详细指导
```

## ⚙️ 配置说明

### 1. 学生信息配置

创建 `config.json` 文件：

```json
{
  "studentInfo": {
    "name": "你的名字",
    "university": "当前学校",
    "major": "Computer Science",
    "year": "大四",
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

### 2. 搜索提示词配置

提示词会自动生成，覆盖以下要求：

- ✅ 北美学校（USA/Canada）
- ✅ 排除 MIT/Stanford/CMU/Berkeley/Caltech
- ✅ 聚焦 3D Vision / Neural Rendering / 3DGS
- ✅ 排除 Bioinformatics / Medical Imaging
- ✅ 15-25 位教授推荐
- ✅ 包含论文、主页、推荐理由

## 🔄 完整工作流程

### Step 1: 搜集导师

告诉 OpenClaw：
> "帮我搜集PhD导师"

系统会生成搜索提示词，你需要：
1. 复制提示词
2. 使用 Bing 搜索（WebSearch/Bing）功能搜索
3. 整理搜索结果到 `outreach/professors/`

### Step 2: 生成套磁信

选择目标教授后，告诉 OpenClaw：
> "为 [教授姓名] 写套磁信"

系统会生成写作提示词，你需要：
1. 填写匹配点和研究兴趣
2. 使用提示词生成邮件内容
3. 保存到 `outreach/emails/`

### Step 3: 发送邮件

确认邮件内容后，告诉 OpenClaw：
> "发送套磁信给 [教授姓名]"

系统会：
1. 生成发送脚本
2. 调用 QQ Mail Monitor
3. 发送邮件并标记状态

## 📁 文件结构

```
phd-outreach/
├── SKILL.md                    # 技能说明文档
├── README.md                   # 使用文档
├── _meta.json                  # 元数据
├── requirements.txt            # 依赖
├── config.example.json         # 配置示例
└── scripts/
    ├── workflow.py             # 完整工作流 ⭐
    ├── search_professors.py    # 导师搜集
    ├── generate_email.py       # 套磁信生成
    └── send_outreach.py        # 邮件发送
```

## 🎓 使用场景

### 场景 1：初次申请
```
目标：搜集15-25位导师，生成全套申请材料
流程：search → email (批量) → send (逐一确认)
```

### 场景 2：针对性套瓷
```
目标：对特定教授发送精心准备的邮件
流程：直接提供教授信息 → email → send
```

### 场景 3：跟进已有联系
```
目标：给已读未回的教授发跟进邮件
流程：使用简洁版邮件模板 → send
```

## ⚠️ 注意事项

1. **学校筛选**
   - 默认排除 top-tier 学校
   - 可在搜索提示词中修改

2. **邮件个性化**
   - 每封邮件必须手动确认
   - 必须提及具体论文/项目
   - 避免模板化表达

3. **发送频率**
   - 建议每天不超过 3-5 封
   - 避免同时发送给同一学校的多位教授

4. **附件管理**
   - 确保 CV PDF 路径正确
   - 建议 CV 文件大小 < 2MB

## 🆘 常见问题

**Q: 如何修改目标学校范围？**
A: 编辑 `workflow.py` 中的 `WORKFLOW_CONFIG` 字典

**Q: 可以搜索其他方向吗？**
A: 修改搜索提示词中的研究方向关键词

**Q: 如何批量生成多封邮件？**
A: 运行 `workflow.py email` 为每位教授单独生成

**Q: 发送失败了怎么办？**
A: 检查 QQ Mail Monitor 配置，确认授权码正确

---

**版本：** 1.0.0
**作者：** OpenClaw
**更新时间：** 2026-04-10
