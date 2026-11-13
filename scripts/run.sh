
#!/bin/bash

# OS ResourceX - Application Launcher

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$PROJECT_DIR" || exit 1

echo "=========================================="
echo "       Starting OS ResourceX"
echo " Operating System Resource Management"
echo "=========================================="

python3 main.py
