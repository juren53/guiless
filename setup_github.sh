#!/bin/bash
# GitHub Setup Script for GUI Less Project
# Run this script after creating the GitHub repository

echo "🚀 GUI Less - GitHub Setup"
echo "=========================="
echo

# Check if we're in the right directory
if [ ! -f "guiless.py" ]; then
    echo "❌ Error: Not in GUI Less project directory"
    echo "Please run: cd /home/juren/Projects/guiless"
    exit 1
fi

echo "✅ In GUI Less project directory"
echo

# Check current git status
echo "📋 Current Git Status:"
git status --short
echo

# Show current commits
echo "📝 Recent Commits:"
git log --oneline -5
echo

# Show tags
echo "🏷️  Current Tags:"
git tag -l
echo

echo "⚠️  MANUAL STEPS REQUIRED:"
echo "1. Create a new repository on GitHub.com with these settings:"
echo "   - Name: guiless"
echo "   - Description: A GUI version of the less utility built with PyQt5"
echo "   - Visibility: Public"
echo "   - DO NOT initialize with README, .gitignore, or license"
echo
echo "2. Copy the repository URL (it will look like:)"
echo "   https://github.com/YOUR_USERNAME/guiless.git"
echo
echo "3. Run these commands (replace YOUR_USERNAME with actual username):"
echo
echo "   # Add the remote origin"
echo "   git remote add origin https://github.com/YOUR_USERNAME/guiless.git"
echo
echo "   # Push main branch and set upstream"
echo "   git push -u origin main"
echo
echo "   # Push all tags"
echo "   git push origin --tags"
echo
echo "   # Verify the setup"
echo "   git remote -v"
echo
echo "4. After pushing, your repository will be available at:"
echo "   https://github.com/YOUR_USERNAME/guiless"
echo
echo "🎯 Ready to push to GitHub!"

