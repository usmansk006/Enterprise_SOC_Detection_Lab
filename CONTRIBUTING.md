# .gitignore

# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
.venv/
venv/
.pytest_cache/
.mypy_cache/
.ruff_cache/
coverage.xml
htmlcov/

# OS files
.DS_Store
Thumbs.db

# Generated output
*.log
*.tmp
*.bak
*.orig
*.rej

# Local lab artifacts
*.evtx
*.pcap
*.zip
*.rar
*.7z
*.csv~
*.json~
*.xml~

# Sensitive evidence and private artifacts
screenshots/private/
artifacts/private/
results/private/
logs/private/

# Editor settings
.vscode/
.idea/

# Local tooling or generated reports
build/
dist/
output/
