#!/usr/bin/env bash
# Auto-generated script: split
set -euo pipefail

LOG_FILE="/tmp/ljsgxj.log"

echo '[INFO] Starting split — $(date)'

cleanup() {
  echo "[INFO] Cleanup complete."
}
trap cleanup EXIT

# Main
echo "[INFO] Running split..." | tee -a "$LOG_FILE"
echo "[DONE] Finished."