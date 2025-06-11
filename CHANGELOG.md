# Changelog

All notable changes to the GUI Less project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Git repository initialization for version control
- Comprehensive .gitignore file for Python projects
- CHANGELOG.md for tracking project changes

## [1.0.0] - 2025-06-11

### Added
- Initial release of GUI Less application
- PyQt5-based graphical interface for text file viewing
- File viewing with read-only access
- Zoom control with Ctrl+Scroll wheel (web browser style)
- Menu bar with File, Edit, and Help menus
- Toolbar with quick access to common functions
- Status bar showing cursor position and file information
- Find/search functionality with dialog interface
- Line numbering toggle feature
- Two-page mode with proper book-style pagination
- Text flow from left page to right page (pages 1-2, 2-3, 3-4, etc.)
- Word wrap toggle feature (enabled by default)
- Keyboard shortcuts compatible with less utility:
  - `q` - Quit application
  - `Ctrl+C` - Alternative quit
  - `?` - Open find dialog
  - `Space` - Next pages (in two-page mode)
  - `b` - Previous pages (in two-page mode)
  - `w` - Toggle word wrap
- Standard GUI shortcuts (Ctrl+O, Ctrl+F, Ctrl+Q, zoom controls)
- Command-line file argument support
- Sample text file for testing features
- Comprehensive README.md with usage instructions
- Requirements.txt for dependency management
- Launcher script (run_guiless.sh)

### Fixed
- Console errors in word wrap pagination logic
- Complex QTextDocument processing replaced with simplified approach
- Improved performance and reliability of pagination system
- Eliminated crash-prone code paths in text layout processing

### Technical Details
- Built with Python 3.6+ and PyQt5
- Modular design with separate classes for main window and text editor
- Extensible architecture for future file format support
- Responsive design that adapts to window resizing
- Cross-platform compatibility (Linux, Windows, macOS)

### Documentation
- Complete user manual in README.md
- Technical bug fix report (BUG_FIX_REPORT.md)
- Inline code documentation and comments
- Installation and usage instructions

## [0.1.0] - 2025-06-11

### Added
- Initial project structure
- Basic GUI framework setup
- Core text viewing functionality

---

## Version History Summary

- **v1.0.0**: Full-featured GUI Less application with two-page mode, word wrap, and all requested features
- **v0.1.0**: Initial development version

## Future Roadmap

### Planned Features
- Enhanced find functionality (regex, case-insensitive)
- Syntax highlighting for code files
- Bookmark/navigation features
- Printing support
- Configuration/preferences system
- Better page break detection for natural pagination
- Advanced word wrap options (soft wrap, smart breaks)
- Performance optimization for very large files

### Potential Enhancements
- Plugin system for custom file format support
- Themes and customizable UI
- Multiple document tabs
- Split-screen comparison mode
- Export functionality (PDF, HTML)
- Search and replace capabilities
- Annotation and note-taking features

