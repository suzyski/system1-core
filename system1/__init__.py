"""
System 1 Core: Dual-Engine Co-Processor for AI Agents
Powered by TypeSafe Jev & ScaleDown
"""

from .config import VERSION
from .router import route_skill
from .gate import gate_action
from .core import compress_context, classify
from .critic import verify_output

__version__ = VERSION
__all__ = [
    "route_skill",
    "gate_action",
    "compress_context",
    "verify_output",
    "classify",
    "VERSION",
]
