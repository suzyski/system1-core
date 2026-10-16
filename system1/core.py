import sys
import json
import urllib.request
import urllib.error
from typing import List, Dict, Any, Optional

from .config import (
    OPENROUTER_API_KEY,
    OPENROUTER_DECISIONS_URL,
    JEV_MODEL,
    SCALEDOWN_API_KEY,
    SCALEDOWN_BASE_URL,
    validate_credentials,
)


def classify_jev(text: str, options: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Evaluates text against options using TypeSafe Jev via OpenRouter Decisions API.
    Sub-15ms fast reflexive inference.
    """
    if not OPENROUTER_API_KEY:
        raise ValueError("OPENROUTER_API_KEY is not configured.")

    url = OPENROUTER_DECISIONS_URL
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/blackdarkknight1122-gif/system1-core",
        "X-Title": "System 1 Engine",
    }
    criteria = {opt["name"]: opt.get("rubric", opt["name"]) for opt in options}
    payload = {
        "model": JEV_MODEL,
        "state": text,
        "questions": {
            "decision": {
                "type": "choice",
                "instructions": "Select the best matching category for the input state.",
                "criteria": criteria,
            }
        },
    }
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST"
    )
    with urllib.request.urlopen(req, timeout=12) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        ans = res.get("answers", {}).get("decision", {})
        top_label = ans.get("choice")
        scores = ans.get("probabilities", {})
        confidence = ans.get("confidence", 1.0)
        return {
            "top_label": top_label,
            "scores": scores,
            "confidence": confidence,
            "reasoning": f"Evaluated via TypeSafe Jev (confidence: {confidence})",
            "cost": res.get("usage", {}).get("cost", 0.0),
            "engine": f"jev ({res.get('model', JEV_MODEL)})",
        }


def classify_scaledown(text: str, options: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Evaluates text against options using ScaleDown /classify/ API.
    Zero-token-waste fast reflexive fallback.
    """
    if not SCALEDOWN_API_KEY:
        raise ValueError("SCALEDOWN_API_KEY is not configured.")

    url = f"{SCALEDOWN_BASE_URL}/classify/"
    payload = {"text": text, "labels": options}
    headers = {"x-api-key": SCALEDOWN_API_KEY, "Content-Type": "application/json"}
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST"
    )
    with urllib.request.urlopen(req, timeout=12) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        return {
            "top_label": data.get("top_label"),
            "scores": data.get("scores", {}),
            "reasoning": data.get("reasoning", ""),
            "engine": "scaledown",
        }


def classify(text: str, options: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Dual-engine reflexive classification:
    Tries TypeSafe Jev first; falls back smoothly to ScaleDown.
    """
    valid, msg = validate_credentials()
    if not valid:
        return {"error": msg}

    if OPENROUTER_API_KEY:
        try:
            return classify_jev(text, options)
        except Exception as e:
            if SCALEDOWN_API_KEY:
                sys.stderr.write(f"[Notice] Jev classification fallback triggered ({e})\n")
            else:
                return {"error": f"TypeSafe Jev request failed: {e}"}

    if SCALEDOWN_API_KEY:
        try:
            return classify_scaledown(text, options)
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8")
            return {"error": f"HTTP {e.code}: {error_body}"}
        except Exception as e:
            return {"error": str(e)}

    return {"error": "No viable classification engine available."}


def compress_context(
    context: str,
    prompt: str = "Retain only critical technical facts, errors, line numbers, and parameters",
) -> Dict[str, Any]:
    """
    Compresses large context/logs via ScaleDown while preserving core technical meaning.
    """
    if not SCALEDOWN_API_KEY:
        return {
            "error": (
                "[System 1 Error] SCALEDOWN_API_KEY is required for context compression.\n"
                "Please run: export SCALEDOWN_API_KEY=\"your_key_here\""
            )
        }

    url = f"{SCALEDOWN_BASE_URL}/compress/raw/"
    payload = {
        "context": context,
        "prompt": prompt,
        "scaledown": {"rate": "auto"},
    }
    headers = {"x-api-key": SCALEDOWN_API_KEY, "Content-Type": "application/json"}

    req = urllib.request.Request(
        url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            results = data.get("results", {})
            return {
                "compressed_text": results.get("compressed_prompt", ""),
                "original_tokens": results.get("original_prompt_tokens", 0),
                "compressed_tokens": results.get("compressed_prompt_tokens", 0),
                "ratio": results.get("compression_ratio", 1.0),
            }
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        return {"error": f"HTTP {e.code}: {error_body}"}
    except Exception as e:
        return {"error": str(e)}
