# GUI Less Help Guide

**Version 1.2.5** - A modern graphical interface for text file viewing

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [User Interface Overview](#user-interface-overview)
3. [Opening and Managing Files](#opening-and-managing-files)
4. [Navigation and Viewing](#navigation-and-viewing)
5. [Text Display Options](#text-display-options)
6. [Search and Find](#search-and-find)
7. [Keyboard Shortcuts](#keyboard-shortcuts)
8. [Themes and Appearance](#themes-and-appearance)
9. [Customization and Settings](#customization-and-settings)
10. [Troubleshooting](#troubleshooting)
11. [Advanced Features](#advanced-features)

---

## Getting Started

### What is GUI Less?

GUI Less is a graphical version of the traditional Unix `less` command-line utility. It provides a modern, user-friendly interface for viewing text files with enhanced features like two-page mode, zoom control, and recent file management.

### First Time Launch

1. **Starting the application:**
   ```bash
   python guiless.py
   ```

2. **Opening a specific file:**
   ```bash
   python guiless.py filename.txt
   ```

3. **First launch behavior:**
   - The application opens in fullscreen mode by default
   - If no file is specified, it will try to load the most recently opened file
   - Two-page mode is enabled by default for a book-like reading experience

---

## User Interface Overview

### Main Window Components

#### Menu Bar
- **File Menu**: Open files, access recent files, exit application
- **Edit Menu**: Find text, toggle display options (line numbers, word wrap, two-page mode)
- **View Menu**: Theme selection, zoom controls, two-page navigation modes
- **Help Menu**: User guide and about information

#### Toolbar
- **Open**: Quick file opening (streamlined interface)

#### Content Area
- **Single Page Mode**: One large text viewing area
- **Two-Page Mode**: Side-by-side pages with intelligent navigation controls
- **Page Navigation**: Previous/Next buttons with mode-specific behavior
- **Navigation Modes**: Choose between Sliding Window or Spread View

#### Status Bar
- **Cursor Position**: Shows current line and column numbers
- **Page Information**: Displays current page numbers and total pages
- **Status Messages**: Temporary messages about operations

---

## Opening and Managing Files

### Opening Files

1. **Using the Menu:**
   - Go to `File` → `Open...` or press `Ctrl+O`
   - Browse and select your text file
   - The file will open immediately

2. **Using Recent Files:**
   - Go to `File` → `Recent Files`
   - Select from up to 10 recently opened files
   - Use keyboard shortcuts `Ctrl+1` through `Ctrl+9` for quick access

3. **Command Line:**
   - Pass the filename as an argument when starting the application
   - Example: `python guiless.py document.txt`

### Supported File Types

- **Text files** (`.txt`)
- **UTF-8 encoded** files
- **Any file type** (with automatic encoding fallback)
- **Large files** (efficiently handled with pagination)

### Recent Files Management

- **Automatic tracking**: Files are automatically added to the recent files list
- **Smart cleanup**: Non-existent files are automatically removed
- **Quick access**: Use `Ctrl+1-9` to open the 1st through 9th most recent files
- **Clear list**: Use `File` → `Recent Files` → `Clear Recent Files` to reset

---

## Navigation and Viewing

### Single Page Mode

- **Scrolling**: Use the mouse wheel or scrollbars to navigate
- **Zoom**: `Ctrl+Scroll wheel` to zoom in/out
- **Full document**: See entire file content in one scrollable view

### Two-Page Mode (Default)

- **Book-style layout**: Content flows from left page to right page
- **Navigation modes**: Choose between two different page progression styles
- **Page navigation**: 
  - Click navigation buttons or press `Space`/`b` to navigate
  - Button labels change based on selected mode
- **Page display**: Shows page numbers with mode indicator (e.g., "Pages 1-2 of 50 (Sliding)")
- **Synchronized features**: Both pages share zoom level and display settings

#### Navigation Modes

**Sliding Window View (Default)**
- **Pattern**: 1-2, 2-3, 3-4, 4-5...
- **Behavior**: Overlapping progression for continuous reading
- **Use case**: Best for documents where context continuity is important
- **Button labels**: "Previous Page" / "Next Page"

**Spread View**
- **Pattern**: 1-2, 3-4, 5-6, 7-8...
- **Behavior**: Distinct page spreads like a traditional book
- **Use case**: Best for book-like reading with clear chapter boundaries
- **Button labels**: "Previous Spread" / "Next Spread"

**Changing Navigation Mode**
- **Menu**: Go to `View` → `Two-Page Navigation`
- **Options**: Select either "Sliding Window View" or "Spread View"
- **Persistence**: Your choice is saved and restored between sessions

### Switching Between Modes

- **Menu**: Go to `Edit` → `Two Page Mode` to toggle
- **Default behavior**: Two-page mode is enabled by default
- **Automatic adjustment**: Content automatically reflows when switching modes

---

## Text Display Options

### Zoom Control

1. **Mouse wheel zooming:**
   - Hold `Ctrl` and scroll up to zoom in
   - Hold `Ctrl` and scroll down to zoom out

2. **Menu-based controls:**
   - Go to `View` → `Zoom` → "Zoom In" or press `Ctrl+=`
   - Go to `View` → `Zoom` → "Zoom Out" or press `Ctrl+-`
   - Go to `View` → `Zoom` → "Reset Zoom" or press `Ctrl+0`

3. **Features:**
   - Maintains fixed-width font for proper text alignment
   - Both pages zoom together in two-page mode
   - Zoom level persists while the file is open
   - Clean interface with zoom controls organized in View menu

### Line Numbers

- **Toggle**: Go to `Edit` → `Show Line Numbers`
- **Format**: Right-aligned with consistent spacing
- **Smart width**: Automatically adjusts based on total line count
- **Compatibility**: Works with both word wrap modes

### Word Wrap

1. **Enabling/Disabling:**
   - Menu: `Edit` → `Word Wrap`
   - **Default**: Word wrap is enabled by default for optimal reading

2. **Behavior:**
   - **Enabled** (default): Long lines wrap to fit the window width
   - **Disabled**: Long lines extend horizontally with scrolling
   - **Automatic reflow**: Pagination recalculates when toggled

---

## Search and Find

### Basic Text Search

1. **Opening search:**
   - Menu: `Edit` → `Find...`
   - Keyboard: `Ctrl+F` or `?` (less-style)

2. **Search behavior:**
   - Case-sensitive matching
   - Highlights found text
   - Shows status message with results

3. **Navigation** (planned features):
   - Press `n` for the next occurrence
   - Press `N` for the previous occurrence

### Search Tips

- **Empty search**: Closes find mode
- **No matches**: Status bar shows "No matches found"
- **Success**: Status bar shows "Found: [search term]"

---

## Keyboard Shortcuts

### Less-Compatible Shortcuts

| Key       | Action         | Description                      |
|-----------|----------------|----------------------------------|
| `q`       | Quit           | Close the application            |
| `Ctrl+C`  | Quit           | Alternative quit command         |
| `?`       | Find           | Open search dialog               |
| `n`       | Find Next      | Next search result (planned)     |
| `N`       | Find Previous  | Previous search result (planned) |
| `Space`   | Next Pages     | Advance to the next page pair    |
| `b`       | Previous Pages | Go back to the previous page pair|

### Standard GUI Shortcuts

| Key        | Action       | Description             |
|------------|--------------|-------------------------|
| `Ctrl+O`   | Open         | Open file dialog        |
| `Ctrl+F`   | Find         | Open search dialog      |
| `Ctrl+Q`   | Quit         | Close application       |
| `Ctrl+=`   | Zoom In      | Increase text size      |
| `Ctrl+-`   | Zoom Out     | Decrease text size      |
| `Ctrl+0`   | Reset Zoom   | Return to default text size |

### Recent Files Shortcuts

| Key        | Action                            |
|------------|-----------------------------------|
| `Ctrl+1`   | Open 1st most recent file         |
| `Ctrl+2`   | Open 2nd most recent file         |
| ...        | ...                               |
| `Ctrl+9`   | Open 9th most recent file         |

---

## Themes and Appearance

### Theme Selection

**GUI Less v1.2.5** includes a comprehensive theming system with 6 beautiful themes to enhance your reading experience.

#### Available Themes

1. **Default**
   - Clean, standard light theme
   - High contrast black text on white background
   - Perfect for general document reading

2. **Dark**
   - Modern dark theme for reduced eye strain
   - White text on dark background
   - Ideal for low-light environments and extended reading sessions

3. **Solarized Light**
   - Warm, easy-on-the-eyes light theme
   - Carefully selected color palette for optimal readability
   - Popular among developers and writers

4. **Solarized Dark**
   - Dark version of the acclaimed Solarized color scheme
   - Excellent contrast with reduced brightness
   - Perfect balance of functionality and aesthetics

5. **High Contrast**
   - Maximum contrast theme for accessibility
   - Black background with bright white text
   - Excellent for users with visual impairments

6. **Monokai**
   - Popular editor theme with rich, vibrant colors
   - Dark background with excellent syntax highlighting colors
   - Favored by developers and programmers

#### Changing Themes

1. **Access theme selection:**
   - Go to `View` → `Theme...`
   - Theme dialog opens with current selection highlighted

2. **Preview themes:**
   - Select any theme from the dropdown
   - Preview area shows real-time sample of how text will appear
   - Try different themes to find your preference

3. **Apply theme:**
   - Click "OK" to apply the selected theme
   - Theme is immediately applied to the entire interface
   - Status bar confirms the theme change

4. **Persistence:**
   - Your theme choice is automatically saved
   - Theme is restored when you restart the application
   - Each theme styles all UI elements consistently

#### Theme Features

- **Comprehensive styling**: Themes affect all interface elements
- **Consistent design**: Menus, buttons, text areas, and dialogs all match
- **Window title indicator**: Non-default themes show in window title
- **Real-time preview**: See exactly how themes will look before applying
- **Instant switching**: No restart required to change themes

---

## Customization and Settings

### Configuration Storage

- **Location**: `~/.guiless/config.json`
- **Automatic creation**: Created on first use
- **Content**: Recent files, last used directory, theme preference, and navigation mode

### Default Settings

- **Display mode**: Two-page mode enabled
- **Navigation mode**: Sliding Window View
- **Theme**: Default (light theme)
- **Word wrap**: Enabled
- **Window state**: Fullscreen/maximized
- **Font**: Courier New, 10pt (fixed-width)
- **Recent files**: Up to 10 files tracked

### Persistence

- **Recent files**: Automatically saved and restored
- **Last directory**: Remembers the last browsed folder
- **Theme preference**: Selected theme is saved and restored
- **Navigation mode**: Two-page navigation preference is remembered
- **File cleanup**: Non-existent files automatically removed

---

## Troubleshooting

### Common Issues

#### File Won't Open
- **Check file exists**: Verify the file path is correct
- **Check permissions**: Ensure you have read access to the file
- **Check encoding**: GUI Less handles UTF-8 and falls back for other encodings

#### Display Problems
- **Text too small/large**: Use zoom controls (`Ctrl+Scroll` or View → Zoom menu)
- **Lines too long**: Enable word wrap (Edit menu)
- **Can't see line numbers**: Toggle line numbers in the Edit menu
- **Theme issues**: Try switching themes via View → Theme menu
- **Interface looks wrong**: Reset to Default theme if custom themes cause issues

#### Navigation Issues
- **Pages don't advance**: Check if you're at the end of the document
- **Unexpected page progression**: Check navigation mode (View → Two-Page Navigation)
- **Two-page mode problems**: Try toggling two-page mode off and on
- **Keyboard shortcuts not working**: Ensure the main window has focus
- **Wrong button labels**: Navigation mode affects button text (Page vs Spread)

#### Performance Issues
- **Large files**: GUI Less uses pagination to handle large files efficiently
- **Slow scrolling**: Try disabling word wrap for very wide content
- **Memory usage**: Close and reopen files if experiencing memory issues

### Error Messages

- **"Failed to open file"**: File doesn't exist or no read permission
- **"File not found"**: Recent file no longer exists (will be removed from list)
- **"No matches found"**: Search term not found in the current document

---

## Advanced Features

### Two-Page Pagination System

- **Smart text flow**: Content properly flows from left to right page
- **Efficient calculation**: Pagination calculated based on window size and font
- **Dynamic adjustment**: Recalculates when window resizes or zoom changes
- **Line-based approach**: Uses text lines rather than visual lines for reliability

### Configuration Management

- **JSON format**: Human-readable configuration file
- **Backward compatibility**: Handles both old and new config formats
- **Error handling**: Graceful fallback if config file is corrupted
- **Directory memory**: Remembers last used directory for file browsing

### Memory Management

- **Efficient loading**: Loads entire file once, then paginates for display
- **Content preservation**: Original content kept for accurate pagination
- **Zoom handling**: Font changes don't require file reloading
- **Mode switching**: Efficient transitions between single and two-page modes

### File Encoding Support

- **UTF-8 primary**: Native UTF-8 support
- **Automatic fallback**: Uses 'replace' error handling for unsupported characters
- **Cross-platform**: Works consistently across different operating systems

---

## Tips and Best Practices

### Optimal Usage

1. **For reading books/documents**: Use two-page mode with Spread View navigation and word wrap enabled
2. **For continuous documents**: Use Sliding Window View for overlapping context
3. **For code files**: Disable word wrap, enable line numbers, consider Monokai theme
4. **For large files**: Use page navigation instead of scrolling
5. **For small text**: Use `Ctrl+Scroll` zoom instead of changing system font
6. **For eye strain**: Try Dark or Solarized Dark themes
7. **For accessibility**: Use High Contrast theme

### Workflow Recommendations

1. **Start with defaults**: Two-page mode with Sliding Window navigation works well for most content
2. **Customize your experience**: Choose a theme that's comfortable for your eyes and environment
3. **Use recent files**: Quick access to frequently viewed documents
4. **Learn keyboard shortcuts**: Especially `Space`/`b` for page navigation
5. **Experiment with navigation modes**: Try both Sliding Window and Spread View to see which you prefer
6. **Utilize fullscreen**: Default fullscreen mode maximizes reading area
7. **Set up your environment**: Choose appropriate theme for your lighting conditions

### Performance Tips

1. **Very large files**: Consider disabling word wrap for better performance
2. **Multiple files**: Close unused files and use the recent files menu
3. **Window resizing**: Pagination automatically recalculates, which may cause a brief delay

---

## Getting Help

### Built-in Help
- **About dialog**: `Help` → `About` for version and feature information
- **Status bar**: Watch for helpful messages during operations
- **Tooltips**: Hover over toolbar buttons for quick descriptions

### Additional Resources
- **GitHub Repository**: [Link to your GitHub repo when published]
- **Issue Tracking**: Report bugs and request features on GitHub
- **Documentation**: This help file and README.md for detailed information

### Contact and Support
- **Project maintainer**: [Your contact information]
- **Bug reports**: Use GitHub issues for bug reports
- **Feature requests**: Submit enhancement requests via GitHub

---

*This help guide covers GUI Less version 1.2.5. For the latest updates and features, check the project's GitHub repository and [changelog](https://github.com/juren53/guiless/blob/main/CHANGELOG.md).*

