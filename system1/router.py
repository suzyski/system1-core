import os
import json
import re
from typing import Dict, Any, List, Optional, Tuple

from .config import SKILLS_SEARCH_PATHS
from .core import classify


def find_skills_library() -> tuple[Optional[str], Optional[str]]:
    """
    Locates the skills index and skills directory from search paths.
    """
    for base in SKILLS_SEARCH_PATHS:
        index_file = os.path.join(base, "skills_index.json")
        skills_dir = os.path.join(base, "skills")
        if not os.path.exists(skills_dir) and os.path.isdir(base):
            skills_dir = base
        if os.path.exists(index_file):
            return index_file, skills_dir
    return None, None


def route_skill(user_query: str) -> Dict[str, Any]:
    """
    Fast candidate filter across runbooks -> System 1 reflexive classification.
    Returns the exact matching skill and path to SKILL.md.
    """
    index_path, skills_dir = find_skills_library()
    if not index_path or not os.path.exists(index_path):
        return {
            "matched": False,
            "error": "No skills index found in standard paths (~/.config/system1/skills, etc.)",
        }

    with open(index_path, "r", encoding="utf-8") as f:
        skills = json.load(f)

    # Tokenize user query for fast lexical scoring
    query_tokens = set(re.findall(r"\w+", user_query.lower()))

    scored_candidates = []
    for s in skills:
        name = s.get("name", "")
        desc = s.get("description", "")
        text = f"{name} {desc}".lower()
        score = sum(1 for token in query_tokens if token in text and len(token) > 2)
        if score > 0:
            scored_candidates.append((score, s))

    scored_candidates.sort(key=lambda x: x[0], reverse=True)
    top_candidates = [item[1] for item in scored_candidates[:8]]

    if not top_candidates:
        return {"matched": False, "message": "No matching skills found in library"}

    # Build options for reflexive classifier
    labels = []
    for s in top_candidates:
        labels.append({
            "name": s["name"],
            "rubric": s.get("description", s["name"])[:200],
        })
    labels.append({
        "name": "none_of_above",
        "rubric": "None of these skills apply to the user query",
    })

    res = classify(user_query, labels)
    if "error" in res:
        return {"matched": False, "error": res["error"]}
    top_name = res.get("top_label")
    if top_name and top_name != "none_of_above":
        skill_path = os.path.join(skills_dir, top_name, "SKILL.md") if skills_dir else None
        return {
            "matched": True,
            "skill_name": top_name,
            "score": res.get("scores", {}).get(top_name, 0.0),
            "reasoning": res.get("reasoning", ""),
            "engine": res.get("engine", "system1"),
            "skill_file": skill_path if skill_path and os.path.exists(skill_path) else None,
        }
    return {"matched": False, "reasoning": res.get("reasoning", "")}
