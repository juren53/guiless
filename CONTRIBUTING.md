# Contributing to GUI Less

Thank you for your interest in contributing to GUI Less! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Release Process](#release-process)

## Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please be respectful and professional in all interactions.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- PyQt5
- Git
- Basic knowledge of Python and Qt/PyQt5

### Repository Structure

```
guiless2/
├── .git/                   # Git repository data
├── .gitignore             # Git ignore patterns
├── guiless.py             # Main application code
├── requirements.txt       # Python dependencies
├── README.md             # User documentation
├── CHANGELOG.md          # Version history
├── CONTRIBUTING.md       # This file
├── LICENSE               # MIT License
├── BUG_FIX_REPORT.md    # Technical documentation
├── sample.txt            # Test file
└── run_guiless.sh        # Launcher script
```

## Development Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd guiless2
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Test the installation:**
   ```bash
   python guiless.py sample.txt
   ```

## Making Changes

### Branching Strategy

- `main` - Stable release branch
- `develop` - Development integration branch (create if needed)
- `feature/feature-name` - Feature development branches
- `bugfix/bug-description` - Bug fix branches
- `hotfix/critical-fix` - Critical production fixes

### Creating a Feature Branch

```bash
git checkout main
git pull origin main
git checkout -b feature/your-feature-name
```

### Development Workflow

1. **Create a branch** for your feature or bugfix
2. **Make your changes** following coding standards
3. **Test thoroughly** to ensure no regressions
4. **Update documentation** as needed
5. **Commit your changes** with clear messages
6. **Submit a pull request** for review

## Coding Standards

### Python Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings for classes and functions
- Keep functions focused and reasonably sized
- Use type hints where appropriate

### Code Example

```python
def calculate_pagination(self) -> None:
    """Calculate how many lines fit per page.
    
    This method determines the number of lines that can be displayed
    per page based on the current viewport size and font metrics.
    """
    if not self.original_content:
        return
        
    viewport_height = self.viewport().height()
    font_metrics = self.fontMetrics()
    line_height = font_metrics.lineSpacing()
    
    self.lines_per_page = max(1, (viewport_height - 20) // line_height)
```

### Git Commit Messages

Use clear, descriptive commit messages:

```
type(scope): brief description

Longer explanation if needed.

Types: feat, fix, docs, style, refactor, test, chore
Scope: ui, pagination, search, etc.
```

Examples:
- `feat(ui): add dark theme support`
- `fix(pagination): resolve word wrap calculation error`
- `docs(readme): update installation instructions`

## Testing

### Manual Testing

1. **Basic functionality:**
   - File opening and viewing
   - Zoom in/out controls
   - Word wrap toggle
   - Line number toggle

2. **Two-page mode:**
   - Page navigation
   - Text flow verification
   - Synchronization of settings

3. **Edge cases:**
   - Very large files
   - Files with long lines
   - Empty files
   - Binary files

### Automated Testing

When adding new features, consider adding simple tests:

```python
# Example test structure
def test_word_wrap_toggle():
    """Test word wrap functionality."""
    app = QApplication([])
    editor = LessTextEdit()
    
    # Test initial state
    assert editor.word_wrap_enabled == True
    
    # Test toggle
    editor.toggle_word_wrap(False)
    assert editor.word_wrap_enabled == False
    assert editor.lineWrapMode() == QTextEdit.NoWrap
```

## Submitting Changes

### Pull Request Process

1. **Ensure your branch is up to date:**
   ```bash
   git checkout main
   git pull origin main
   git checkout your-branch
   git rebase main
   ```

2. **Create a pull request with:**
   - Clear title and description
   - List of changes made
   - Testing performed
   - Screenshots if UI changes
   - Reference to related issues

3. **Pull request template:**
   ```markdown
   ## Description
   Brief description of changes
   
   ## Changes Made
   - List of specific changes
   - Another change
   
   ## Testing
   - [ ] Manual testing performed
   - [ ] No regressions found
   - [ ] Documentation updated
   
   ## Screenshots
   (If applicable)
   ```

### Review Process

- All changes require review before merging
- Address feedback promptly and professionally
- Update documentation as needed
- Ensure all tests pass

## Release Process

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- `MAJOR.MINOR.PATCH`
- Major: Breaking changes
- Minor: New features (backward compatible)
- Patch: Bug fixes (backward compatible)

### Creating a Release

1. **Update CHANGELOG.md:**
   - Move items from "Unreleased" to new version
   - Add release date
   - Include all significant changes

2. **Update version in code:**
   - Update version strings in application
   - Update documentation references

3. **Create release commit:**
   ```bash
   git add .
   git commit -m "chore: prepare release v1.1.0"
   ```

4. **Create and push tag:**
   ```bash
   git tag -a v1.1.0 -m "Release v1.1.0"
   git push origin main --tags
   ```

## Areas for Contribution

### High Priority
- Enhanced find functionality (regex, case-insensitive)
- Syntax highlighting for code files
- Performance optimization for large files
- Better error handling and user feedback

### Medium Priority
- Bookmark/navigation features
- Printing support
- Configuration/preferences system
- Themes and customization

### Future Enhancements
- Plugin system
- Multiple document tabs
- Export functionality
- Annotation features

## Getting Help

If you need help with development:

1. Check existing documentation
2. Review similar implementations in the codebase
3. Create an issue for discussion
4. Ask questions in pull request comments

## Recognition

Contributors will be recognized in:
- CHANGELOG.md for their contributions
- README.md contributors section (when created)
- Release notes for significant contributions

Thank you for contributing to GUI Less!

