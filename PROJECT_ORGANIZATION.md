# GUI Less Project Organization Guide

## Overview

This document outlines the organization of GUI Less project directories and best practices for avoiding confusion between current and legacy versions.

## Directory Structure

### Current Active Project
```
/home/juren/Projects/guiless/          ← CURRENT PROJECT
├── guiless.py                          # Main application (v1.1.0+)
├── requirements.txt                    # Dependencies
├── README.md                          # Current documentation
├── CHANGELOG.md                       # Version history
├── CONTRIBUTING.md                    # Development guide
├── LICENSE                            # MIT License
├── BUG_FIX_REPORT.md                 # Technical documentation
├── PROJECT_ORGANIZATION.md            # This file
├── sample.txt                         # Test file
└── run_guiless.sh                     # Launcher script
```

### Legacy Prototype (Deprecated)
```
/home/juren/Projects/guiless-old-prototype/   ← DEPRECATED
├── main.py                            # Old prototype code
├── file_handlers.py                   # Experimental handlers
├── DEPRECATED.md                      # Deprecation notice
├── README.md                          # Old documentation
└── [other legacy files]               # Historical files
```

### User Configuration
```
~/.guiless/
└── recent_files.json                 # Recent files (current project)
```

## Best Practices

### 1. ⚙️ Always Use Current Project

**For all GUI Less work, always navigate to:**
```bash
cd /home/juren/Projects/guiless
```

**Never use the deprecated directory for:**
- Running the application
- Development work
- Bug reports
- Feature development
- Documentation updates

### 2. 📁 Clear Directory Naming

- **`guiless/`**: Current, active project
- **`guiless-old-prototype/`**: Clearly marked as deprecated
- Naming convention prevents accidental usage

### 3. 📢 Documentation Strategy

- **Current project**: Complete, up-to-date documentation
- **Legacy project**: DEPRECATED.md notice explaining status
- **Cross-references**: Clear pointers to current project

### 4. 🔄 Version Control

- **Current project**: Active Git repository with proper versioning
- **Legacy project**: Archived Git history (no new commits)
- **Tags**: Use semantic versioning in current project

### 5. 🛡️ Environment Safety

```bash
# Safe aliases to prevent mistakes
alias guiless='cd /home/juren/Projects/guiless'
alias guiless-run='cd /home/juren/Projects/guiless && python guiless.py'

# Add to ~/.bashrc or ~/.zshrc for permanent usage
```

### 6. 📈 Development Workflow

**Before starting work:**
```bash
# 1. Ensure you're in the right directory
pwd
# Should show: /home/juren/Projects/guiless

# 2. Check Git status
git status
# Should show current branch (main)

# 3. Verify you have the current version
ls -la guiless.py
# Should show recent modification date
```

## Migration Actions Taken

### ✅ Completed Steps

1. **Directory Reorganization**:
   - Renamed `guiless/` → `guiless-old-prototype/`
   - Renamed `guiless2/` → `guiless/`

2. **Documentation Updates**:
   - Added `DEPRECATED.md` to old prototype
   - Updated README.md with project organization info
   - Created this PROJECT_ORGANIZATION.md guide

3. **Clear Naming Conventions**:
   - Current project has standard name (`guiless`)
   - Legacy project clearly marked as prototype

4. **Version Control Preservation**:
   - Both projects retain their Git histories
   - Current project has proper tagging (v1.0.0, v1.1.0)

## Warning Signs of Wrong Directory

⚠️ **You're in the wrong directory if you see:**

- `main.py` instead of `guiless.py`
- `file_handlers.py` file
- Missing recent features (recent files, fullscreen, etc.)
- Old Git commits without version tags
- Different file structure

✅ **You're in the right directory if you see:**

- `guiless.py` as main file
- Version tags (v1.0.0, v1.1.0)
- Recent commits with new features
- Complete documentation set
- PROJECT_ORGANIZATION.md (this file)

## Quick Reference Commands

```bash
# Navigate to current project
cd /home/juren/Projects/guiless

# Run the application
python guiless.py

# Check which version you're in
ls -la *.py
# Should show: guiless.py (not main.py)

# Verify Git status
git log --oneline -5
# Should show recent commits with v1.1.0 features

# Check for deprecation notice (should NOT exist in current)
ls DEPRECATED.md 2>/dev/null && echo "WARNING: You're in the deprecated directory!"
```

## If You Accidentally Use Wrong Directory

### 🚑 Emergency Recovery

1. **Stop what you're doing**
2. **Check current directory**: `pwd`
3. **Navigate to correct project**: `cd /home/juren/Projects/guiless`
4. **Verify you're in the right place**: `ls guiless.py`
5. **Continue work in correct directory**

### 🔄 File Recovery (if needed)

If you accidentally created files in the wrong directory:

```bash
# Move files from old to current directory
mv /home/juren/Projects/guiless-old-prototype/newfile.txt /home/juren/Projects/guiless/

# Or copy if you want to keep both
cp /home/juren/Projects/guiless-old-prototype/newfile.txt /home/juren/Projects/guiless/
```

---

## Summary

🎯 **Golden Rule**: Always work in `/home/juren/Projects/guiless/`

💡 **Quick Check**: If you see `guiless.py`, you're in the right place!

⚠️ **Red Flag**: If you see `main.py` or `DEPRECATED.md`, you're in the wrong directory!

---

*This guide ensures clean project organization and prevents development confusion between current and legacy versions.*

