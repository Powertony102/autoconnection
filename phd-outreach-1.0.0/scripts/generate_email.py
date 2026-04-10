#!/usr/bin/env python3
"""
套磁信生成工具 - v1.0
为指定教授生成个性化套磁信
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, Any, List


def generate_email_prompt(
    student_info: Dict[str, Any],
    professor_info: Dict[str, Any],
    match_points: str,
    future_research: str
) -> str:
    """生成套磁信写作提示词"""

    prof_papers = "\n".join([f"- {p}" for p in professor_info.get('recent_papers', [])[:3]])

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
- 研究经历: {student_info.get('research_experience', '3D Gaussian Splatting acceleration, feed-forward 3D reconstruction')}
- 发表论文: {student_info.get('publications', '[Your Publications]')}
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
{match_points}

我未来想做的研究问题：
{future_research}

--------------------------------

## 输出格式要求

### 邮件标题选项
1. [标题1]
2. [标题2]
3. [标题3]

### 正式版邮件
```
Subject: [推荐标题]

Dear Professor {professor_info.get('name', 'XXX').split()[-1]},

[正文 220-300词]

Best regards,
{student_info.get('name', '[Your Name]')}
```

### 简洁版邮件
```
Subject: [推荐标题]

Dear Professor {professor_info.get('name', 'XXX').split()[-1]},

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


def parse_professor_selection(selection_str: str, professors: List[Dict[str, Any]]) -> Dict[str, Any]:
    """解析用户选择的教授"""
    try:
        # 尝试解析为索引
        idx = int(selection_str) - 1
        if 0 <= idx < len(professors):
            return professors[idx]
    except ValueError:
        pass

    # 尝试按名字匹配
    for prof in professors:
        if selection_str.lower() in prof.get('name', '').lower():
            return prof

    return None


def save_email(
    professor_name: str,
    email_content: str,
    output_dir: str = "./outreach"
) -> str:
    """保存生成的套磁信"""
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(f"{output_dir}/emails", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = professor_name.replace(" ", "_").replace(".", "")
    filename = f"{output_dir}/emails/email_{safe_name}_{timestamp}.md"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(email_content)

    print(f"✅ 套磁信已保存到: {filename}")
    return filename


def generate_email_summary(professor_info: Dict[str, Any], student_info: Dict[str, Any]) -> str:
    """生成邮件摘要用于展示"""
    return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📧 套瓷信生成摘要
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

目标教授: {professor_info.get('name', 'N/A')}
学校: {professor_info.get('university', 'N/A')}
实验室: {professor_info.get('lab', 'N/A')}

研究方向匹配:
- 教授: {professor_info.get('research_area', 'N/A')[:80]}...
- 学生: {student_info.get('research_interests', '3D Computer Vision')}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
提示词已生成，请使用 OpenClaw 生成邮件内容。
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


def main():
    """主函数"""
    print("=" * 60)
    print("✉️ 套磁信生成工具")
    print("=" * 60)
    print("\n此工具帮助生成个性化套磁信写作提示词。\n")
    print("使用方法:")
    print("1. 先运行 search_professors 获取导师列表")
    print("2. 选择目标教授")
    print("3. 填写匹配点和研究兴趣")
    print("4. 使用生成的提示词在 OpenClaw 中生成邮件\n")


if __name__ == "__main__":
    main()
