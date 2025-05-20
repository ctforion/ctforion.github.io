#!/bin/bash

# ====================================================================
# 🛡️ Safe Shell Config
# ====================================================================
set -euo pipefail

# ====================================================================
# 🧾 Logging Helpers (No Color)
# ====================================================================
info()    { echo "[i] $1"; }
warn()    { echo "[w] $1"; }
error()   { echo "[!] $1"; }
success() { echo "[✓] $1"; }
timestamp() { echo "★[$(date '+%Y-%m-%d %H:%M:%S')] $1"; }

# ====================================================================
# 📌 Config
# ====================================================================
REPO_URL="https://github.com/ctforion/ctforion.github.io.git"
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STATIC_DIR="$BASE_DIR/statics"
TEMP_DIR="$BASE_DIR/temp"
AUTO_RESET=true  # Auto-reset dirty repos before pulling

# ====================================================================
# 🔧 Git Check
# ====================================================================
if ! command -v git &>/dev/null; then
    warn "Git not found. Attempting to install..."
    if command -v apt-get &>/dev/null; then
        sudo apt-get update && sudo apt-get install -y git
    elif command -v yum &>/dev/null; then
        sudo yum install -y git
    else
        error "Unsupported OS. Install git manually."
        exit 1
    fi
else
    success "git is installed."
fi

# ====================================================================
# 📁 Prepare Directories
# ====================================================================
info "Ensuring directories..."
mkdir -p "$STATIC_DIR" "$TEMP_DIR"
info "STATIC_DIR: $STATIC_DIR"
info "TEMP_DIR  : $TEMP_DIR"

# ====================================================================
# ⬇️ Clone or Pull Repo
# ====================================================================
if [ -d "$TEMP_DIR/.git" ]; then
    info "Repo already exists. Pulling latest changes..."
    cd "$TEMP_DIR"
    
    if ! git diff --quiet; then
        if [ "$AUTO_RESET" = true ]; then
            warn "Unstaged changes found. Resetting..."
            git reset --hard HEAD && git clean -fd
        else
            error "Unstaged changes detected. Skipping pull."
            exit 1
        fi
    fi

    if git pull --rebase --autostash; then
        success "Repository updated."
    else
        error "Pull failed."
        exit 1
    fi
else
    info "Cloning repository..."
    if git clone "$REPO_URL" "$TEMP_DIR"; then
        success "Clone successful."
    else
        error "Clone failed."
        exit 1
    fi
fi

# ====================================================================
# 🔍 Check Differences
# ====================================================================
check_changes() {
    info "Checking for differences between TEMP and STATICS..."

    if [ ! -d "$STATIC_DIR" ] || [ -z "$(ls -A "$STATIC_DIR")" ]; then
        warn "STATIC_DIR is empty. Likely first run."
        return
    fi

    changes=$(rsync -aun --delete "$TEMP_DIR/" "$STATIC_DIR/" | grep -v '^\.')
    if [ -z "$changes" ]; then
        success "No differences found."
    else
        echo "$changes"
        warn "Differences detected."
    fi
}

check_changes

# ====================================================================
# ✅ Final Summary Block
# ====================================================================
echo "----------------------------------------------------------------------------"
timestamp "Successful"
echo "----------------------------------------------------------------------------"
