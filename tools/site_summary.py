import json
import sys
from typing import Dict, List, Optional

SITE_DATA = {
    "name": "乐鱼体育",
    "url": "https://m-page-leyu.com.cn",
    "tags": ["体育资讯", "赛事直播", "比分数据"],
    "description": "提供最新体育赛事信息、实时比分与深度数据分析的专业体育平台。",
    "keywords": ["乐鱼体育", "体育比分", "NBA", "英超", "赛事预测"]
}

def build_summary(site: Dict[str, any]) -> str:
    name = site.get("name", "未知站点")
    url = site.get("url", "#")
    tags = site.get("tags", [])
    description = site.get("description", "")
    keywords = site.get("keywords", [])

    lines = []
    lines.append(f"站点名称：{name}")
    lines.append(f"站点地址：{url}")
    lines.append(f"简短描述：{description}")
    lines.append(f"标签：{'、'.join(tags)}")
    lines.append(f"核心关键词：{'、'.join(keywords)}")
    return "\n".join(lines)

def format_json_summary(site: Dict[str, any]) -> str:
    return json.dumps(site, ensure_ascii=False, indent=2)

def extract_key_metrics(site: Dict[str, any]) -> Dict[str, any]:
    return {
        "name": site.get("name", ""),
        "url_length": len(site.get("url", "")),
        "tag_count": len(site.get("tags", [])),
        "keyword_count": len(site.get("keywords", []))
    }

def print_summary(summary: str, title: str = "站点摘要") -> None:
    border = "=" * 40
    print(border)
    print(f"  {title}")
    print(border)
    print(summary)
    print(border)

def main() -> None:
    site = SITE_DATA
    summary_text = build_summary(site)
    print_summary(summary_text, "文字摘要")
    print()
    json_output = format_json_summary(site)
    print_summary(json_output, "JSON格式")
    print()
    metrics = extract_key_metrics(site)
    print(f"关键指标：{metrics}")

if __name__ == "__main__":
    main()