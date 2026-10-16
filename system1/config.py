import os
from typing import List

VERSION = "1.0.0"

# Dual-Engine API configuration
# Read strictly from environment variables or .env file (NO hardcoded personal secrets)
SCALEDOWN_API_KEY = os.environ.get("SCALEDOWN_API_KEY", "").strip()
SCALEDOWN_BASE_URL = os.environ.get("SCALEDOWN_BASE_URL", "https://api.scaledown.xyz").strip()

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "").strip()
OPENROUTER_DECISIONS_URL = os.environ.get(
    "OPENROUTER_DECISIONS_URL", "https://openrouter.ai/api/alpha/decisions"
).strip()
JEV_MODEL = os.environ.get("JEV_MODEL", "typesafe/jev-1.14").strip()

# Standard portable skills & runbook search paths
SKILLS_SEARCH_PATHS: List[str] = [
    p
    for p in [
        os.environ.get("SYSTEM1_SKILLS_PATH", "").strip(),
        os.path.expanduser("~/.config/system1/skills"),
        os.path.join(os.getcwd(), "skills"),
        os.path.join(os.getcwd(), "skills-library"),
    ]
    if p
]


def validate_credentials() -> tuple[bool, str]:
    """
    Validates if at least one engine credential is provided.
    """
    if not OPENROUTER_API_KEY and not SCALEDOWN_API_KEY:
        msg = (
            "[System 1 Error] No API credentials found.\n"
            "Please configure your environment:\n"
            "  export OPENROUTER_API_KEY=\"your_key_here\"  # for TypeSafe Jev\n"
            "  or\n"
            "  export SCALEDOWN_API_KEY=\"your_key_here\"   # for ScaleDown\n"
            "See .env.example for configuration details."
        )
        return False, msg
    return True, ""
