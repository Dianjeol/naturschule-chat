#!/usr/bin/env bash
# Launcher wrapper for Linux systems with Wayland or NVIDIA GPUs where
# WebKitGTK hardware compositing can cause a white/blank window.
set -euo pipefail

export WEBKIT_DISABLE_COMPOSITING_MODE=1

if command -v campai-chat >/dev/null 2>&1; then
  exec campai-chat "$@"
elif [[ -x "./campai-chat.AppImage" ]]; then
  exec ./campai-chat.AppImage "$@"
else
  echo "campai-chat binary or ./campai-chat.AppImage not found." >&2
  exit 1
fi
