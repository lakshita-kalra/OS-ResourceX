
#!/bin/bash

# OS ResourceX - Cleanup Script

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "=========================================="
echo "       OS ResourceX Cleanup"
echo "=========================================="

find "$PROJECT_DIR" -type d -name "__pycache__" -prune -exec rm -rf {} +

find "$PROJECT_DIR" -type f -name "*.pyc" -delete

echo "Temporary Python cache files cleaned successfully."
echo "Activity logs and source files are preserved."
