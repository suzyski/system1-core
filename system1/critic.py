from typing import Dict, Any
from .core import classify


def verify_output(task_goal: str, output_summary: str) -> Dict[str, Any]:
    """
    Validates if a completed task satisfied the goal without regressions.
    Deterministic System 1 critic before an agent declares "DONE".
    """
    text = f"Goal: {task_goal}\n\nOutcome Summary: {output_summary}"
    labels = [
        {
            "name": "fully_satisfied",
            "rubric": "The outcome completely satisfies all stated requirements cleanly with proof",
        },
        {
            "name": "partially_satisfied",
            "rubric": "Some requirements met but missing key components or unverified",
        },
        {
            "name": "failed_or_regression",
            "rubric": "Failed to achieve the goal, introduced syntax/breaking errors, or drifted off task",
        },
    ]
    return classify(text, labels)
