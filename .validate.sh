#!/bin/bash

echo "🔍 Running stealth validation..."

# Check Bash scripts
echo "→ Checking Bash scripts..."
find . -name "*.sh" -not -path "./node_modules/*" -exec bash -n {} \;

# Check Python scripts
echo "→ Checking Python scripts..."
find . -name "*.py" -not -path "./node_modules/*" -exec python -m py_compile {} \;

echo "✅ Validation complete."
