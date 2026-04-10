#!/usr/bin/env python3
"""
PhD 导师搜集工具 - v1.0
搜索北美 3D Vision 方向的教授
"""

import json
import os
import sys
from datetime import datetime
from typing import List, Dict, Any

# 配置
SEARCH_KEYWORDS = [
    "3D Gaussian Splatting professor",
    "neural rendering research group",
    "3D reconstruction lab USA",
    "novel view synthesis professor",
    "3D vision geometry deep learning",
    "image matching computer vision professor",
    "3D computer vision PhD advisor"
]

# 目标学校列表（排名20-100或强校）
TARGET_UNIVERSITIES = [
    "University of Toronto", "University of British Columbia", "McGill University",
    "University of Washington", "University of Wisconsin-Madison", "University of Michigan",
    "University of Illinois Urbana-Champaign", "University of Maryland",
    "University of Texas at Austin", "University of North Carolina",
    "Purdue University", "Ohio State University", "Pennsylvania State University",
    "University of California San Diego", "University of California Irvine",
    "University of California Santa Barbara", "University of California Davis",
    "Georgia Institute of Technology", "University of Florida",
    "University of Minnesota", "University of Arizona",
    "Arizona State University", "Indiana University",
    "University of Utah", "University of Colorado Boulder",
    "Northeastern University", "Boston University",
    "University of Southern California", "University of Rochester",
    "Stony Brook University", "University of Virginia"
]

# 顶级会议
TOP_CONFERENCES = ["CVPR", "ICCV", "ECCV", "SIGGRAPH", "NeurIPS", "ICML", "ICLR"]


def search_professors_websearch(query: str, num_results: int = 10) -> List[Dict[str, Any]]:
    """
    使用 WebSearch 搜索教授信息
    注意：此函数需要在 OpenClaw 环境中运行，使用系统的 WebSearch 能力
    """
    # 这是一个模板函数，实际执行时由 OpenClaw 注入搜索能力
    # 返回格式化的搜索结果
    return []


def parse_professor_info(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """解析教授信息"""
    return {
        "name": raw_data.get("name", ""),
        "university": raw_data.get("university", ""),
        "lab": raw_data.get("lab", ""),
        "research_area": raw_data.get("research_area", ""),
        "recent_papers": raw_data.get("recent_papers", []),
        "google_scholar": raw_data.get("google_scholar", ""),
        "homepage": raw_data.get("homepage", ""),
        "twitter": raw_data.get("twitter", ""),
        "match_reason": raw_data.get("match_reason", "")
    }


def generate_search_prompt() -> str:
    """生成搜索提示词"""
    return """You are an academic research assistant helping a student identify potential PhD advisors.

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


def save_results(professors: List[Dict[str, Any]], output_dir: str = "./outreach"):
    """保存搜索结果"""
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(f"{output_dir}/professors", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/professors/search_result_{timestamp}.json"

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({
            "timestamp": timestamp,
            "total": len(professors),
            "professors": professors
        }, f, ensure_ascii=False, indent=2)

    print(f"✅ 搜索结果已保存到: {filename}")
    return filename


def print_professors(professors: List[Dict[str, Any]]):
    """打印教授列表"""
    print(f"\n📊 共找到 {len(professors)} 位潜在导师\n")
    print("=" * 60)

    for i, prof in enumerate(professors, 1):
        print(f"\n{i}. {prof.get('name', 'N/A')}")
        print(f"   学校: {prof.get('university', 'N/A')}")
        print(f"   研究方向: {prof.get('research_area', 'N/A')[:60]}...")
        print(f"   主页: {prof.get('homepage', 'N/A')}")


def main():
    """主函数 - 由 OpenClaw 调用"""
    print("=" * 60)
    print("🔍 PhD 导师搜集工具")
    print("=" * 60)
    print("\n此工具需要在 OpenClaw 环境中运行，使用系统的搜索能力。")
    print("搜索提示词已生成，请使用以下提示词进行搜索:\n")
    print(generate_search_prompt())
    print("\n" + "=" * 60)
    print("使用说明:")
    print("1. 复制上面的提示词")
    print("2. 在 OpenClaw 中使用 WebSearch 功能搜索")
    print("3. 将搜索结果保存到 outreach/professors/ 目录")


if __name__ == "__main__":
    main()
