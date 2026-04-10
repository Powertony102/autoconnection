#!/usr/bin/env python3
"""
PhD 套瓷完整工作流 - v1.0
整合导师搜集、邮件生成和发送流程
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, Any, List


# 工作流配置
WORKFLOW_CONFIG = {
    "search_keywords": [
        "3D Gaussian Splatting professor North America",
        "neural rendering research lab USA",
        "3D reconstruction PhD advisor Canada",
        "novel view synthesis research group",
        "3D computer vision professor university"
    ],
    "target_conferences": ["CVPR", "ICCV", "ECCV", "SIGGRAPH", "NeurIPS", "ICML", "ICLR"],
    "exclude_universities": ["MIT", "Stanford", "CMU", "UC Berkeley", "Caltech"],
    "prefer_universities": [
        "University of Toronto", "University of British Columbia",
        "University of Washington", "University of Wisconsin-Madison",
        "University of Michigan", "Georgia Tech", "UT Austin",
        "University of Maryland", "Purdue", "Ohio State"
    ]
}


def load_student_info(config_file: str = "./config.json") -> Dict[str, Any]:
    """加载学生信息"""
    default_info = {
        "name": "[Your Name]",
        "university": "[Your University]",
        "major": "Computer Science",
        "year": "Senior",
        "research_interests": "3D Computer Vision, Neural Rendering, 3D Gaussian Splatting",
        "research_experience": [
            "3D Gaussian Splatting acceleration",
            "Feed-forward 3D reconstruction",
            "Image matching and novel view synthesis"
        ],
        "publications": ["[Publication 1]", "[Publication 2]"],
        "skills": "PyTorch, CUDA, Python, C++",
        "target_degree": "PhD",
        "target_semester": "Fall 2026",
        "resume_path": "./docs/CV.pdf"
    }

    if os.path.exists(config_file):
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
            if 'studentInfo' in config:
                return {**default_info, **config['studentInfo']}
            return {**default_info, **config}

    return default_info


def check_setup() -> bool:
    """检查环境配置"""
    print("\n🔍 检查环境配置...\n")

    checks = {
        "config.json": os.path.exists("./config.json"),
        "QQ Mail Monitor": os.path.exists("../qq-mail-monitor-1.0.0"),
        "output directory": os.path.exists("./outreach") or os.makedirs("./outreach", exist_ok=True)
    }

    all_ok = True
    for name, exists in checks.items():
        status = "✅" if exists else "❌"
        print(f"  {status} {name}")
        if not exists:
            all_ok = False

    if not checks["config.json"]:
        print("\n⚠️ 未找到 config.json，请复制 config.example.json 并填写你的信息")

    return all_ok


def generate_search_prompt(student_info: Dict[str, Any]) -> str:
    """生成搜索提示词"""
    return f"""You are an academic research assistant helping a student identify potential PhD advisors.

Your task is to search for professors in **North America (USA and Canada)** whose research matches the student's interests in **3D Computer Vision**.

You MUST search using:
- Google Scholar
- X (Twitter) posts
- Lab pages
- Personal academic websites
- Conference publications (CVPR / ICCV / ECCV / NeurIPS / ICML / SIGGRAPH etc.)

Use **English search queries**, such as:
- "3D vision professor neural rendering lab"
- "Gaussian splatting research group"
- "3D reconstruction professor university"
- "novel view synthesis lab"
- "3D geometry deep learning professor"

However, your **final output MUST be written in Chinese**.

--------------------------------

Student background (very important):

The student is an undergraduate preparing to apply for **direct-entry PhD in Computer Science**.

Research interests:
- 3D Computer Vision
- 3D Reconstruction
- Neural Rendering
- 3D Gaussian Splatting
- Image Matching
- Geometry-based vision

The student already has research experience in:
- 3D Gaussian Splatting acceleration
- Feed-forward 3D reconstruction
- Image matching
- Novel view synthesis

The student previously had publications in medical image analysis and bioinformatics, but **future research should focus on 3D vision rather than biomedical areas**.

Therefore:
❌ DO NOT recommend professors mainly working in:
- Bioinformatics
- Medical imaging
- Biomedical engineering
- Computational biology

--------------------------------

University filtering requirements:

DO NOT recommend extremely top-tier universities such as:

- MIT
- Stanford
- CMU
- UC Berkeley
- Caltech

Instead prefer:

- Good but not ultra-elite universities
- Strong CV/3D vision groups
- Universities ranked roughly 20–100 globally or strong regional research universities

--------------------------------

For each professor you recommend, you MUST include:

1. 教授姓名
2. 所在学校
3. 实验室 / 研究组名称
4. 研究方向
5. 最近3年代表论文（2–3篇）
6. Google Scholar链接
7. 个人主页 / 实验室主页
8. 是否活跃在X（如果有）
9. 推荐理由（为什么适合该学生）

--------------------------------

Additional requirements:

- Prioritize professors publishing in:
  - CVPR
  - ICCV
  - ECCV
  - SIGGRAPH
  - NeurIPS
  - ICLR
- Prefer **labs active in neural rendering / 3DGS / 3D reconstruction / geometry learning**.
- Try to find **young or mid-career professors** who are more likely to take PhD students.

--------------------------------

Output format (Chinese):

For each professor:

【教授姓名】

学校：
研究方向：
实验室：

近期代表论文：
1.
2.
3.

Google Scholar：
个人主页：

X（Twitter）：

推荐理由：

--------------------------------

Please recommend **15–25 professors**."""


def generate_email_prompt(student_info: Dict[str, Any], professor_info: Dict[str, Any]) -> str:
    """生成套磁信提示词"""

    prof_papers = "\n".join([f"- {p}" for p in professor_info.get('recent_papers', [])[:3]])

    research_exp = "\n".join([f"- {exp}" for exp in student_info.get('research_experience', [])])

    return f"""请你扮演一位顶级 PhD 套瓷邮件写作专家，帮我写一封高质量英文套瓷邮件，目标是提高教授回复率。

请严格遵循以下原则：
1. 邮件必须围绕"研究匹配度"展开，而不是单纯表达申请意愿；
2. 必须体现我认真了解过教授的研究，不得写成群发模板；
3. 要结合教授的具体论文、项目或研究议题，体现真实针对性；
4. 要突出我的相关背景、方法能力、研究经历和未来研究兴趣；
5. 语气必须礼貌、专业、真诚、不卑不亢；
6. 避免夸张赞美、乞求式表达、全大写、感叹号和空泛套话；
7. 邮件简洁高效，控制在 220–300 词；
8. 默认我会附上 CV 和其他必要材料，请自然提及；
9. 输出必须像真实申请者写给教授的邮件，而不是 AI 模板。

请按以下格式输出：
- 3个可选邮件标题
- 1封正式版英文套瓷邮件
- 1封更简洁的英文版本
- 最后用中文总结这封邮件的写作策略（3–5条）

我的信息：
- 姓名: {student_info.get('name', '[Your Name]')}
- 当前学校: {student_info.get('university', '[Your University]')}
- 专业: {student_info.get('major', 'Computer Science')}
- 年级: {student_info.get('year', 'Senior')}
- 研究经历:
{research_exp if research_exp else "- [请填写研究经历]"}
- 发表论文: {', '.join(student_info.get('publications', []))}
- 技术能力: {student_info.get('skills', 'PyTorch, CUDA, Python')}
- 目标学位: {student_info.get('target_degree', 'PhD')}
- 目标入学时间: {student_info.get('target_semester', 'Fall 2026')}

目标教授信息：
- 姓名: {professor_info.get('name', '[Professor Name]')}
- 学校: {professor_info.get('university', '[University]')}
- 实验室: {professor_info.get('lab', '[Lab Name]')}
- 研究方向: {professor_info.get('research_area', '[Research Area]')}

教授论文/项目/研究主题：
{prof_papers if prof_papers else "- [请填写具体论文或项目名称]"}

我与教授研究的匹配点：
[请填写：我在XX方面的研究经验与教授的XX工作高度相关...]

我未来想做的研究问题：
[请填写：我计划在博士期间研究XX问题...]

--------------------------------

## 输出格式要求

### 邮件标题选项
1. [标题1]
2. [标题2]
3. [标题3]

### 正式版邮件
```
Subject: [推荐标题]

Dear Professor {professor_info.get('name', 'XXX').split()[-1] if ' ' in professor_info.get('name', 'XXX') else professor_info.get('name', 'XXX')},

[正文 220-300词]

Best regards,
{student_info.get('name', '[Your Name]')}
```

### 简洁版邮件
```
Subject: [推荐标题]

Dear Professor {professor_info.get('name', 'XXX').split()[-1] if ' ' in professor_info.get('name', 'XXX') else professor_info.get('name', 'XXX')},

[精简版正文 150-200词]

Best,
{student_info.get('name', '[Your Name]')}
```

### 写作策略总结（中文）
1. [策略1]
2. [策略2]
3. [策略3]
4. [策略4]
5. [策略5]"""


def save_prompt_to_file(prompt: str, filename: str):
    """保存提示词到文件"""
    os.makedirs("./outreach/prompts", exist_ok=True)
    filepath = f"./outreach/prompts/{filename}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(prompt)

    print(f"✅ 提示词已保存到: {filepath}")
    return filepath


def print_usage_guide():
    """打印使用指南"""
    guide = """
╔══════════════════════════════════════════════════════════════════════════╗
║                     🎓 PhD 套瓷助手 - 使用指南                           ║
╚══════════════════════════════════════════════════════════════════════════╝

📋 准备工作:
   1. 复制 config.example.json 为 config.json
   2. 填写你的个人信息和简历路径
   3. 确保 QQ Mail Monitor 已配置

🔍 步骤1: 搜集导师
   运行: python3 workflow.py search
   或直接使用生成的搜索提示词在 OpenClaw 中搜索

✉️ 步骤2: 生成套磁信
   运行: python3 workflow.py email [教授姓名/编号]
   或直接使用生成的写作提示词

📤 步骤3: 发送邮件
   运行: python3 workflow.py send [邮件文件]

💡 提示: 你也可以直接告诉 OpenClaw:
   "帮我搜集PhD导师" 或 "为[教授名]写套磁信"

═══════════════════════════════════════════════════════════════════════════
"""
    print(guide)


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print_usage_guide()
        return

    command = sys.argv[1].lower()
    student_info = load_student_info()

    if command == "search":
        # 生成搜索提示词
        print("=" * 70)
        print("🔍 导师搜集模式")
        print("=" * 70)

        prompt = generate_search_prompt(student_info)
        filepath = save_prompt_to_file(prompt, "search_prompt.txt")

        print("\n已生成搜索提示词，请复制以下内容到 OpenClaw 中执行:\n")
        print("=" * 70)
        print(prompt)
        print("=" * 70)
        print("\n搜索完成后:")
        print(f"1. 将搜索结果整理并保存到 ./outreach/professors/")
        print(f"2. 格式: JSON 或 Markdown")

    elif command == "email":
        # 生成套磁信提示词
        print("=" * 70)
        print("✉️ 套磁信生成模式")
        print("=" * 70)

        # 尝试加载已搜集的教授列表
        professor = {
            "name": sys.argv[2] if len(sys.argv) > 2 else "[Professor Name]",
            "university": "[University]",
            "lab": "[Lab Name]",
            "research_area": "[Research Area]",
            "recent_papers": []
        }

        prompt = generate_email_prompt(student_info, professor)
        filepath = save_prompt_to_file(prompt, f"email_prompt_{professor['name'].replace(' ', '_')}.txt")

        print("\n已生成套磁信写作提示词，请:\n")
        print("1. 修改提示词中的 [请填写...] 部分")
        print("2. 复制到 OpenClaw 中生成邮件")
        print(f"3. 提示词已保存到: {filepath}")

    elif command == "send":
        # 发送邮件指导
        print("=" * 70)
        print("📤 邮件发送模式")
        print("=" * 70)
        print("\n请使用 QQ Mail Monitor 发送邮件:\n")
        print("1. 找到 QQ Mail Monitor 路径")
        print("2. 编辑 scripts/qq_mail_send.py")
        print("3. 修改收件人、主题和正文")
        print("4. 运行: python3 qq_mail_send.py")

    else:
        print_usage_guide()


if __name__ == "__main__":
    main()
