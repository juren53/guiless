# Changelog

All notable changes to the GUI Less project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Enhanced find functionality (regex, case-insensitive)
- Syntax highlighting for code files
- Bookmark/navigation features

## [1.2.0] - 2025-06-11

### Added
- Two-page mode is now the default startup mode for enhanced reading experience
- Last directory memory - file dialogs remember the last directory accessed
- Navigation controls (Previous Pages/Next Pages) are visible by default
- Enhanced configuration system with backward compatibility for existing users

### Changed
- Default application startup mode changed from single-page to two-page view
- Configuration file format upgraded from `recent_files.json` to `config.json`
- File dialog now opens in the last directory where files were opened or browsed
- Menu "Two Page Mode" option is checked by default to reflect current state

### Enhanced
- Improved user experience with immediate access to two-page reading mode
- Better file navigation workflow with persistent directory memory
- Seamless upgrade path for existing users with automatic config migration
- More intuitive interface with visible navigation controls from startup

### Technical
- Added `last_directory` tracking in configuration management
- Implemented backward compatibility for old configuration format
- Updated file opening functions to persist and use last directory
- Enhanced configuration structure while maintaining existing functionality

## [1.1.0] - 2025-06-11

### Added
- Recent Files functionality with up to 10 file tracking
- Auto-load most recent file when no command-line argument provided
- Fullscreen mode by default for better viewing experience
- Recent Files submenu in File menu with keyboard shortcuts
- Configuration file storage in user's home directory (~/.guiless/)
- "Clear Recent Files" option with confirmation dialog
- Automatic removal of non-existent files from recent list
- Keyboard shortcuts Ctrl+1 through Ctrl+9 for recent file access
- JSON-based configuration storage system
- Improved startup behavior and user experience

### Enhanced
- File menu now includes Recent Files submenu
- Better file management with persistent recent file tracking
- Improved application startup with intelligent file loading
- Enhanced user interface with fullscreen default

### Technical
- Added JSON configuration management
- Implemented pathlib for cross-platform file handling
- Added proper error handling for configuration file operations
- Enhanced main() function with improved startup logic

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
- MIT License for open source distribution

## [0.1.0] - 2025-06-11

### Added
- Initial project structure
- Basic GUI framework setup
- Core text viewing functionality

---

## Version History Summary

- **v1.2.0**: Two-page mode as default, last directory memory, improved user experience
- **v1.1.0**: Added recent files, auto-load, and fullscreen features for enhanced user experience
- **v1.0.0**: Full-featured GUI Less application with two-page mode, word wrap, and core functionality
- **v0.1.0**: Initial development version

## Future Roadmap

### Planned Features
- Enhanced find functionality (regex, case-insensitive)
- Syntax highlighting for code files
- Bookmark/navigation features
- Printing support
- Expanded configuration/preferences system
- Better page break detection for natural pagination
- Advanced word wrap options (soft wrap, smart breaks)
- Performance optimization for very large files
- Recent files organization and management
- Configurable auto-load behavior
- Configurable default view mode (single vs two-page)
- Directory bookmarks and favorites

### Potential Enhancements
- Plugin system for custom file format support
- Themes and customizable UI
- Multiple document tabs
- Split-screen comparison mode
- Export functionality (PDF, HTML)
- Search and replace capabilities
- Annotation and note-taking features
- Smart file type detection and handling
- Advanced directory navigation features

