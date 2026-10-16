#!/usr/bin/env python3
import sys
import os
import json
import argparse

from .config import VERSION
from .router import route_skill
from .gate import gate_action
from .core import compress_context
from .critic import verify_output


def main():
    parser = argparse.ArgumentParser(
        prog="system1",
        description="Dual-Engine System 1 Co-Processor for Autonomous AI Agents (TypeSafe Jev + ScaleDown)",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")

    subparsers = parser.add_subparsers(dest="command", help="Available System 1 commands")

    # 1. Route Skill
    p_route = subparsers.add_parser(
        "route",
        aliases=["route-skill"],
        help="Instant runbook discovery across specialized skills (<15ms)",
    )
    p_route.add_argument("query", help="User request or topic to route")

    # 2. Gate Action
    p_gate = subparsers.add_parser(
        "gate",
        aliases=["gate-action"],
        help="Deterministic safety risk gate for destructive actions",
    )
    p_gate.add_argument("action", help="Bash command or proposed action to evaluate")

    # 3. Compress Context
    p_compress = subparsers.add_parser(
        "compress",
        help="ScaleDown context & log compressor (-30%% to -70%% token savings)",
    )
    p_compress.add_argument("context", help="Large terminal output, logs, or prompt text")
    p_compress.add_argument(
        "--prompt",
        default="Retain only critical technical facts, errors, line numbers, and parameters",
        help="Compression extraction prompt",
    )

    # 4. Verify Output Critic
    p_verify = subparsers.add_parser(
        "verify",
        help="Deterministic System 1 critic evaluating task completion",
    )
    p_verify.add_argument("goal", help="Original user task goal")
    p_verify.add_argument("outcome", help="Outcome summary and verification proof")

    # Handle legacy argv where commands are passed directly like 'system1 route-skill ...'
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    cmd = args.command
    if cmd in ("route", "route-skill"):
        res = route_skill(args.query)
    elif cmd in ("gate", "gate-action"):
        res = gate_action(args.action)
    elif cmd == "compress":
        res = compress_context(args.context, prompt=args.prompt)
    elif cmd == "verify":
        res = verify_output(args.goal, args.outcome)
    else:
        res = {"error": f"Unknown command: {cmd}"}

    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
