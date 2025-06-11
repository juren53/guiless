# GUI Less - A GUI Version of the Less Utility

A modern graphical interface version of the Unix `less` command-line utility, built with Python and PyQt5.

## Features

### Core Functionality
- **File Viewing**: Open and view ASCII text files with read-only access
- **Less-like Navigation**: Familiar keyboard shortcuts from the `less` utility
- **Zoom Control**: Ctrl+Scroll wheel zooming (web browser style)
- **Find/Search**: Built-in text search functionality
- **Line Numbers**: Toggle line numbering on/off
- **Two-Page Mode**: Proper book-style pagination with text flow from left to right page
- **Word Wrap**: Toggle word wrapping for long lines (enabled by default)
- **Recent Files**: Track and quickly access recently opened files
- **Auto-Load**: Automatically loads the most recent file on startup
- **Fullscreen Mode**: Launches in fullscreen by default for optimal viewing

### GUI Features
- **Menu Bar**: File, Edit, and Help menus
- **Toolbar**: Quick access to common functions
- **Status Bar**: Shows cursor position and file information
- **Modern Interface**: Clean, user-friendly design

## Installation

### Prerequisites
- Python 3.6 or higher
- PyQt5

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

**Without a file (auto-loads most recent):**
```bash
python guiless.py
```

**With a file argument:**
```bash
python guiless.py filename.txt
```

### Keyboard Shortcuts

#### Less-compatible shortcuts:
- `q` - Quit application
- `Ctrl+C` - Alternative quit
- `?` - Open find dialog
- `n` - Find next (planned)
- `N` - Find previous (planned)
- `Space` - Next pages (in two-page mode)
- `b` - Previous pages (in two-page mode)
- `w` - Toggle word wrap
- `Ctrl+1` to `Ctrl+9` - Open recent files (1st to 9th most recent)

#### Standard GUI shortcuts:
- `Ctrl+O` - Open file
- `Ctrl+F` - Find text
- `Ctrl+Q` - Quit
- `Ctrl++` / `Ctrl+=` - Zoom in
- `Ctrl+-` - Zoom out
- `Ctrl+0` - Reset zoom

### Menu Options

#### File Menu
- **Open...** - Open a text file
- **Recent Files** - Submenu with recently opened files
- **Exit** - Close the application

#### Edit Menu
- **Find...** - Search for text in the current file
- **Show Line Numbers** - Toggle line numbering
- **Two Page Mode** - Switch to book-style facing page view with proper text flow
- **Word Wrap** - Toggle word wrapping for long lines

#### Help Menu
- **About** - Application information

## Features in Detail

### Zoom Control
- Use `Ctrl+Scroll Wheel` to zoom in and out
- Toolbar buttons for zoom in, zoom out, and reset
- Maintains fixed-width font for proper text alignment

### Two-Page Mode
- Toggle between single page and facing page view
- Text flows from left page to right page like a real book
- Navigation shows pages 1-2, then 2-3, then 3-4, etc.
- Both pages maintain synchronized zoom levels
- Page navigation buttons and status display
- Use Space/b keys for next/previous page pairs

### Word Wrap
- Toggle word wrapping on/off for long lines
- Enabled by default for better readability
- Works in both single and two-page modes
- Automatically recalculates pagination when toggled
- Accessible via menu, toolbar, or 'w' keyboard shortcut

### Recent Files
- Automatically tracks up to 10 most recently opened files
- Accessible via File → Recent Files menu
- Keyboard shortcuts Ctrl+1 through Ctrl+9 for quick access
- Files that no longer exist are automatically removed from the list
- "Clear Recent Files" option to reset the list
- Most recent file is automatically loaded when no file is specified

### Fullscreen Mode
- Application launches in fullscreen (maximized) mode by default
- Provides optimal viewing area for text content
- Can be toggled using standard window controls
- Maintains fullscreen preference for consistent experience

### Line Numbers
- Optional line numbering that can be toggled on/off
- Right-aligned line numbers with consistent spacing
- Automatically adjusts width based on total line count
- Works correctly with word wrap enabled or disabled

### Find Functionality
- Search dialog accessible via menu or keyboard shortcut
- Case-sensitive text searching
- Status bar feedback for search results

## File Format Support

### Currently Supported
- ASCII text files (.txt)
- UTF-8 encoded text files
- All file types (with fallback encoding)
- Automatic word wrapping for improved readability
- Recent files tracking and auto-loading
- Configuration storage in user's home directory (~/.guiless/)

### Future Support (Extensible)
The application is designed to easily add support for:
- Syntax highlighting for code files
- Markdown rendering
- Rich text formats
- Binary file viewing (hex mode)
- Custom word wrap options (character limits, smart breaks)

## Project Organization

### Current vs Legacy
⚗ **Important**: This is the current, active GUI Less project.

- **Current Project**: `/home/juren/Projects/guiless/` (this directory)
- **Legacy Prototype**: `/home/juren/Projects/guiless-old-prototype/` (deprecated)

**Always use this directory** (`/home/juren/Projects/guiless/`) for:
- Running the application
- Development work
- Bug reports and features
- Documentation updates

## Development

### Project Structure
```
guiless/
├── guiless.py          # Main application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── sample.txt         # Sample text file for testing
└── run_guiless.sh     # Launcher script

# User Configuration
~/.guiless/
└── recent_files.json  # Recent files list (auto-created)
```

### Key Classes
- `GuiLess`: Main application window and controller
- `LessTextEdit`: Custom text editor with zoom, word wrap, and less-like features
- `FindDialog`: Search dialog for text finding

### Extending the Application
The modular design makes it easy to add new features:
- Text formatting engines can be added to `LessTextEdit`
- New view modes can be implemented in the main window
- Additional file format support through pluggable readers
- Word wrap algorithms can be customized or extended

## License

This project is open source. Feel free to modify and distribute.

## Contributing

Contributions are welcome! Areas for improvement:
- Enhanced find functionality (regex, case-insensitive)
- Syntax highlighting for code files
- Bookmark/navigation features
- Printing support
- Configuration/preferences system
- Better page break detection for natural pagination
- Customizable lines per page settings
- Advanced word wrap options (soft wrap, smart breaks)
- Performance optimization for very large files
- Recent files management and organization
- Configurable auto-load behavior
- Custom fullscreen and window preferences

