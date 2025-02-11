#!/bin/bash

# Remove Python compiled files from git tracking
git rm -r --cached "*.pyc"
git rm -r --cached "__pycache__"
git rm -r --cached "*.so"
git rm -r --cached "*.egg-info"
git rm -r --cached "dist"
git rm -r --cached "build"
git rm -r --cached "venv"
git rm -r --cached "env"
git rm -r --cached "health_connect_venv"
git rm -r --cached ".vscode"
git rm -r --cached ".idea"
git rm -r --cached "*.sqlite3"
git rm -r --cached "*.db"
git rm -r --cached ".env"
git rm -r --cached ".env.local"
git rm -r --cached "*.log"
git rm -r --cached "logs"
git rm -r --cached "htmlcov"
git rm -r --cached ".coverage"
git rm -r --cached ".pytest_cache"
git rm -r --cached ".tox"
git rm -r --cached "local_settings.py"

# Commit the changes
git add .gitignore
git commit -m "Untrack files that are now in .gitignore"
