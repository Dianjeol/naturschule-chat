#!/usr/bin/env bash
# Launcher wrapper for Linux systems with Wayland or NVIDIA GPUs where
# WebKitGTK hardware compositing can cause a white/blank window.
set -euo pipefail

export WEBKIT_DISABLE_COMPOSITING_MODE=1

if command -v naturschule-chat >/dev/null 2>&1; then
  exec naturschule-chat "$@"
elif [[ -x "./naturschule-chat.AppImage" ]]; then
  exec ./naturschule-chat.AppImage "$@"
else
  echo "naturschule-chat binary or ./naturschule-chat.AppImage not found." >&2
  exit 1
fi
