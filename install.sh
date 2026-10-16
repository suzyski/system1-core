#!/usr/bin/env bash
# System 1 Core One-Line Installer
# Installs system1 and jev CLI into ~/.local/bin

set -e

CYAN='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${CYAN}=====================================================${NC}"
echo -e "${CYAN}   ⚡ Installing System 1 Core Engine               ${NC}"
echo -e "${CYAN}   Fast Reflexive Co-Processor for AI Agents        ${NC}"
echo -e "${CYAN}=====================================================${NC}"

# 1. Verify Python
if ! command -v python3 &>/dev/null; then
    echo -e "${RED}[Error] python3 is required but not found in PATH.${NC}"
    exit 1
fi

BIN_DIR="$HOME/.local/bin"
CONFIG_DIR="$HOME/.config/system1"
mkdir -p "$BIN_DIR" "$CONFIG_DIR"

# 2. Install Python Package
echo -e "\n${CYAN}📦 Installing system1-core CLI...${NC}"
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"

if [ -f "$REPO_DIR/pyproject.toml" ]; then
    # Local installation from cloned repo
    python3 -m pip install -e "$REPO_DIR" --quiet --upgrade
else
    # Direct remote install
    python3 -m pip install git+https://github.com/suzyski/system1-core.git --quiet --upgrade
fi

# 3. Ensure ~/.local/bin is in PATH
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    SHELL_RC=""
    if [ -n "$ZSH_VERSION" ] || [ "$SHELL" = "/bin/zsh" ]; then
        SHELL_RC="$HOME/.zshrc"
    elif [ -n "$BASH_VERSION" ] || [ "$SHELL" = "/bin/bash" ]; then
        SHELL_RC="$HOME/.bashrc"
    fi

    if [ -n "$SHELL_RC" ] && [ -f "$SHELL_RC" ]; then
        if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$SHELL_RC"; then
            echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_RC"
            echo -e "${GREEN}✓ Added ~/.local/bin to PATH in $SHELL_RC${NC}"
        fi
    fi
fi

echo -e "\n${GREEN}✓ System 1 Core successfully installed!${NC}"
echo -e "Available commands:"
echo -e "  - ${CYAN}system1 route \"<topic>\"${NC}   (Instant skill/runbook matching)"
echo -e "  - ${CYAN}system1 gate \"<cmd>\"${NC}       (Destructive command risk gating)"
echo -e "  - ${CYAN}system1 compress \"<logs>\"${NC}   (ScaleDown context compression)"
echo -e "  - ${CYAN}system1 verify \"<goal>\" \"<outcome>\"${NC} (Completion critic)"
echo -e "Alias: ${CYAN}jev <command>${NC}"
echo -e "\nTo equip your agent, drop the rules from ${CYAN}templates/AGENTS.md${NC} into your project."
