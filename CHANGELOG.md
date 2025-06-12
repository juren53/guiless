# Changelog

All notable changes to the GUI Less project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Enhanced find functionality (regex, case-insensitive)
- Syntax highlighting for code files
- Bookmark/navigation features

## [1.2.5] - 2025-06-12

### Added
- **Comprehensive UI Themes System** with 6 beautiful themes:
  - Default (clean light theme)
  - Dark (modern dark theme for reduced eye strain)
  - Solarized Light (warm, easy-on-the-eyes light theme)
  - Solarized Dark (popular dark theme with excellent contrast)
  - High Contrast (black background with bright text for accessibility)
  - Monokai (popular editor theme with rich colors)
- **ThemeDialog** with real-time preview for easy theme selection
- **Two-Page Navigation Modes** for enhanced reading control:
  - **Sliding Window View** (1-2, 2-3, 3-4...) - continuous overlapping navigation
  - **Spread View** (1-2, 3-4, 5-6...) - book-style distinct page spreads
- **View Menu** reorganization with logical grouping:
  - Theme selection submenu
  - Zoom controls submenu (Zoom In, Zoom Out, Reset Zoom)
  - Two-Page Navigation mode selection
- Navigation mode indicators in page counter display
- Dynamic button labels that change based on navigation mode
- Persistent theme and navigation mode preferences in configuration

### Changed
- **Moved Zoom controls** from toolbar to View → Zoom submenu for cleaner UI
- **Removed Word Wrap button** from toolbar (still available in Edit menu)
- **Simplified toolbar** to only essential "Open" button for reduced clutter
- Updated About dialog to reflect new features and capabilities
- Enhanced status bar messages for better user feedback

### Enhanced
- **Theme persistence** - selected theme is saved and restored between sessions
- **Navigation mode persistence** - preferred navigation style is remembered
- **Comprehensive CSS styling** - all UI elements consistently themed
- **Improved user experience** with organized menu structure
- **Real-time theme preview** in selection dialog
- **Smart navigation button states** based on current mode and position
- **Window title updates** to reflect current theme (when not Default)

### Technical
- Added `ThemeManager` class for centralized theme management
- Implemented CSS stylesheet generation system
- Added `ThemeDialog` class with live preview functionality
- Enhanced configuration system to include theme and navigation preferences
- Updated navigation logic to support both sliding and spread modes
- Improved UI organization with logical menu grouping
- Added comprehensive styling for all Qt widgets
- Enhanced keyboard shortcut integration for zoom controls

## [1.2.0] - 2025-06-11

### Added
- Two-page mode is now the default startup mode for enhanced reading experience
- Last directory memory - file dialogs remember the last directory accessed
- Navigation controls (Previous Pages/Next Pages) are visible by default
- Enhanced configuration system with backward compatibility for existing users
- **User Guide menu item** in Help menu linking to comprehensive GitHub documentation
- **Comprehensive help documentation** (HELP.md) in Docs/ directory with:
  - Complete user interface overview
  - Step-by-step usage instructions
  - Keyboard shortcuts reference
  - Troubleshooting guide
  - Advanced features documentation
  - Tips and best practices
- Web browser integration for opening GitHub-hosted documentation
- Error handling and fallback instructions if browser fails to open

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

- **v1.2.5**: Comprehensive UI themes, two-page navigation modes, and streamlined interface
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
- ~~Themes and customizable UI~~ ✅ **Completed in v1.2.5**
- Multiple document tabs
- Split-screen comparison mode
- Export functionality (PDF, HTML)
- Search and replace capabilities
- Annotation and note-taking features
- Smart file type detection and handling
- Advanced directory navigation features

