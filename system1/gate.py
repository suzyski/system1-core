from typing import Dict, Any
from .core import classify


def gate_action(action_text: str) -> Dict[str, Any]:
    """
    Evaluates the safety and risk profile of a proposed bash command or tool call.
    Returns whether the action is safe or high_risk_destructive.
    """
    labels = [
        {
            "name": "safe_read_or_test",
            "rubric": "Read-only inspection, file viewing, test execution, linters, harmless status checks",
        },
        {
            "name": "standard_edit",
            "rubric": "Reversible code edits, creating new safe files, installing standard project dependencies",
        },
        {
            "name": "high_risk_destructive",
            "rubric": "Permanently deleting files (rm -rf), destructive git (reset --hard, push -f), dropping databases, killing system processes, exposing credentials",
        },
    ]
    return classify(action_text, labels)
