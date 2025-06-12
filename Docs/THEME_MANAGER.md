# GUI Less Custom Theme Manager

**Technical Documentation for the Built-in Theme Management System**

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Core Components](#core-components)
4. [Theme Data Structure](#theme-data-structure)
5. [CSS Generation System](#css-generation-system)
6. [Theme Dialog Interface](#theme-dialog-interface)
7. [Configuration Integration](#configuration-integration)
8. [Adding New Themes](#adding-new-themes)
9. [Customization Guide](#customization-guide)
10. [Technical Implementation](#technical-implementation)
11. [Best Practices](#best-practices)

---

## Overview

GUI Less employs a **custom-built theme management system** designed specifically for text viewing applications. Unlike external theming frameworks, this system provides complete control over the visual appearance while maintaining optimal performance for document reading.

### Key Features

- **8 Built-in Themes**: From classic light/dark to specialized themes like Terminal Green
- **Real-time Preview**: See theme changes instantly before applying
- **Persistent Preferences**: Theme choices are automatically saved and restored
- **CSS-based Styling**: Professional styling system for all UI components
- **Zero Dependencies**: No external theme libraries required
- **Cross-platform Consistency**: Identical appearance across operating systems

### Design Philosophy

1. **Simplicity**: Easy to understand and modify
2. **Performance**: Lightweight with minimal resource usage
3. **Consistency**: Uniform styling across all interface elements
4. **Extensibility**: Simple theme addition without code restructuring
5. **User Experience**: Intuitive selection with immediate feedback

---

## Architecture

```
GUI Less Application
├── ThemeManager (Core Engine)
│   ├── Theme Data Storage
│   ├── CSS Generation
│   └── Theme Validation
│
├── ThemeDialog (User Interface)
│   ├── Theme Selector
│   ├── Live Preview
│   └── Apply/Cancel Actions
│
└── Configuration System
    ├── Theme Persistence
    ├── Auto-restoration
    └── Cross-session Memory
```

### Component Relationships

- **ThemeManager**: Central hub managing all theme operations
- **ThemeDialog**: User interface for theme selection
- **GuiLess Main Window**: Applies themes and handles UI updates
- **Configuration System**: Handles theme persistence across sessions

---

## Core Components

### 1. ThemeManager Class

**Location**: `guiless.py`, lines 24-342

**Purpose**: Central theme management engine

**Key Methods**:
- `get_theme_names()`: Returns list of available themes
- `get_theme(theme_name)`: Retrieves theme data dictionary
- `generate_stylesheet(theme_name)`: Creates CSS for theme application

**Initialization**:
```python
class ThemeManager:
    def __init__(self):
        self.themes = {    # Dictionary of all available themes
            'Default': { ... },
            'Dark': { ... },
            # ... more themes
        }
        self.current_theme = 'Default'
```

### 2. ThemeDialog Class

**Location**: `guiless.py`, lines 345-399

**Purpose**: User interface for theme selection

**Features**:
- Dropdown selector with all available themes
- Real-time preview area showing theme colors
- OK/Cancel button handling
- Theme change detection and preview updates

### 3. Integration Points

**Main Application Integration**:
- Theme menu item: `View → Theme...`
- Theme application: `apply_theme()` method
- Configuration persistence: `save_config()` / `load_config()`
- Window title updates reflecting current theme

---

## Theme Data Structure

Each theme is defined as a Python dictionary with standardized color properties:

```python
'Theme Name': {
    'name': 'Theme Name',           # Display name in UI
    'background': '#ffffff',        # Main content background
    'text': '#000000',             # Primary text color
    'selection_bg': '#3399ff',      # Text selection background
    'selection_text': '#ffffff',    # Text selection foreground
    'menubar_bg': '#f0f0f0',       # Menu bar background
    'menubar_text': '#000000',     # Menu bar text
    'toolbar_bg': '#f5f5f5',       # Toolbar background
    'statusbar_bg': '#e0e0e0',     # Status bar background
    'statusbar_text': '#000000',   # Status bar text
    'button_bg': '#e1e1e1',        # Button background
    'button_text': '#000000',      # Button text
    'button_hover': '#d4d4d4',     # Button hover state
    'border': '#c0c0c0'            # Border and separator colors
}
```

### Color Property Definitions

| Property | Purpose | Usage |
|----------|---------|-------|
| `background` | Main text viewing area | Document background |
| `text` | Primary text color | Document content |
| `selection_bg` | Highlight background | Selected text background |
| `selection_text` | Highlight text | Selected text foreground |
| `menubar_bg` | Menu bar styling | Top menu background |
| `menubar_text` | Menu text | Menu item text |
| `toolbar_bg` | Toolbar styling | Toolbar background |
| `statusbar_bg` | Status bar styling | Bottom bar background |
| `statusbar_text` | Status text | Status messages |
| `button_bg` | Button styling | Button backgrounds |
| `button_text` | Button text | Button labels |
| `button_hover` | Interactive feedback | Button hover effects |
| `border` | Separators and borders | UI element boundaries |

---

## CSS Generation System

The theme manager dynamically generates complete CSS stylesheets for theme application.

### Generation Process

1. **Theme Selection**: User selects theme or system loads saved preference
2. **Data Retrieval**: `get_theme()` fetches theme color dictionary
3. **CSS Creation**: `generate_stylesheet()` builds complete CSS
4. **Application**: `setStyleSheet()` applies CSS to application

### CSS Structure

The generated stylesheet covers all PyQt5 components:

```css
/* Main Window */
QMainWindow {
    background-color: {theme['background']};
    color: {theme['text']};
}

/* Text Edit Areas */
QTextEdit {
    background-color: {theme['background']};
    color: {theme['text']};
    selection-background-color: {theme['selection_bg']};
    selection-color: {theme['selection_text']};
    font-family: 'Courier New', 'Consolas', monospace;
}

/* Menu Components */
QMenuBar {
    background-color: {theme['menubar_bg']};
    color: {theme['menubar_text']};
}

/* ... and many more components */
```

### Styled Components

- **QMainWindow**: Application window
- **QTextEdit**: Text viewing areas
- **QMenuBar / QMenu**: Menu system
- **QToolBar**: Toolbar components
- **QStatusBar**: Status information
- **QPushButton**: Interactive buttons
- **QComboBox**: Dropdown selectors
- **QDialog**: Dialog windows
- **QLineEdit**: Text input fields
- **QLabel**: Text labels
- **QSplitter**: Resizable dividers

---

## Theme Dialog Interface

### User Experience Flow

1. **Access**: User clicks `View → Theme...`
2. **Selection**: Dropdown shows all available themes
3. **Preview**: Real-time preview updates as user browses
4. **Application**: Click "OK" to apply, "Cancel" to abort
5. **Persistence**: Applied theme is automatically saved

### Technical Implementation

```python
class ThemeDialog(QDialog):
    def __init__(self, current_theme, theme_manager, parent=None):
        # Initialize dialog with current theme selected
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(self.theme_manager.get_theme_names())
        self.theme_combo.currentTextChanged.connect(self.on_theme_changed)
        
        # Preview label with live updates
        self.preview_label = QLabel("Preview: This is how text will look")
        
    def update_preview(self):
        # Apply theme colors to preview area
        theme = self.theme_manager.get_theme(self.selected_theme)
        self.preview_label.setStyleSheet(f"""
            background-color: {theme['background']};
            color: {theme['text']};
            border: 1px solid {theme['border']};
        """)
```

### Dialog Features

- **Fixed Size**: `400x200` pixels for consistent appearance
- **Live Preview**: Immediate visual feedback
- **Theme List**: All themes in alphabetical order
- **Current Selection**: Highlights currently active theme
- **Responsive**: Updates instantly on selection change

---

## Configuration Integration

### Storage Location

- **Config Directory**: `~/.guiless/`
- **Config File**: `config.json`
- **Theme Key**: `"theme": "Theme Name"`

### Persistence Mechanism

```python
def save_config(self):
    config_data = {
        'recent_files': self.recent_files,
        'last_directory': self.last_directory,
        'theme': self.current_theme,           # Theme persistence
        'sliding_window_mode': self.sliding_window_mode
    }
    with open(self.config_file, 'w') as f:
        json.dump(config_data, f, indent=2)

def load_config(self):
    # Load configuration and restore theme
    self.current_theme = config_data.get('theme', 'Default')
```

### Auto-restoration

1. **Application Start**: `load_config()` reads saved theme preference
2. **Theme Application**: `apply_theme()` restores visual appearance
3. **Session Continuity**: User sees same theme as last session
4. **Fallback**: Defaults to 'Default' theme if config is corrupted

---

## Adding New Themes

### Step-by-Step Process

#### 1. Define Theme Dictionary

```python
'Your Theme Name': {
    'name': 'Your Theme Name',
    'background': '#your_bg_color',
    'text': '#your_text_color',
    'selection_bg': '#your_selection_bg',
    'selection_text': '#your_selection_text',
    'menubar_bg': '#your_menubar_bg',
    'menubar_text': '#your_menubar_text',
    'toolbar_bg': '#your_toolbar_bg',
    'statusbar_bg': '#your_statusbar_bg',
    'statusbar_text': '#your_statusbar_text',
    'button_bg': '#your_button_bg',
    'button_text': '#your_button_text',
    'button_hover': '#your_button_hover',
    'border': '#your_border_color'
}
```

#### 2. Add to ThemeManager

Insert the theme dictionary into the `self.themes` dictionary in `ThemeManager.__init__()`:

```python
self.themes = {
    'Default': { ... },
    'Dark': { ... },
    # ... existing themes ...
    'Your Theme Name': {
        # Your theme definition here
    }
}
```

#### 3. Test the Theme

1. Save the file
2. Restart GUI Less
3. Go to `View → Theme...`
4. Select your new theme
5. Verify all UI elements look correct

### Theme Design Guidelines

- **Contrast**: Ensure sufficient contrast between text and background
- **Consistency**: Use related colors for a cohesive appearance
- **Accessibility**: Consider users with visual impairments
- **Testing**: Test with actual documents to verify readability
- **Naming**: Use descriptive, memorable theme names

---

## Customization Guide

### Modifying Existing Themes

1. **Locate Theme**: Find theme in `ThemeManager.__init__()`
2. **Edit Colors**: Change hex color values
3. **Test Changes**: Restart application and verify appearance
4. **Document Changes**: Update any relevant documentation

### Color Selection Tips

- **Hex Format**: Use `#RRGGBB` format (e.g., `#ff0000` for red)
- **Online Tools**: Use color palette generators for inspiration
- **Contrast Checkers**: Verify accessibility with contrast checking tools
- **Theme Consistency**: Maintain color relationships across properties

### Advanced Customization

#### Adding New Color Properties

1. **Extend Theme Dictionary**: Add new color keys
2. **Update CSS Generation**: Include new properties in stylesheet
3. **Apply to Components**: Target specific UI elements

#### Custom CSS Rules

Modify `generate_stylesheet()` to add custom styling:

```python
def generate_stylesheet(self, theme_name):
    theme = self.get_theme(theme_name)
    return f"""
    /* Existing rules */
    QTextEdit {{
        background-color: {theme['background']};
        /* Your custom properties */
        border-radius: 5px;
        padding: 10px;
    }}
    """
```

---

## Technical Implementation

### Memory Management

- **Theme Storage**: Themes stored as lightweight dictionaries
- **CSS Caching**: Stylesheets generated on-demand
- **Minimal Overhead**: No persistent CSS files or external resources

### Performance Characteristics

- **Instant Application**: Themes apply immediately via `setStyleSheet()`
- **No File I/O**: All theme data in memory
- **Minimal CPU Usage**: Simple string formatting for CSS generation
- **Cross-platform**: Identical performance on all operating systems

### Error Handling

```python
def get_theme(self, theme_name):
    """Get theme data by name with fallback"""
    return self.themes.get(theme_name, self.themes['Default'])
```

- **Graceful Fallback**: Unknown themes default to 'Default'
- **Config Corruption**: Handles malformed configuration files
- **Missing Themes**: Automatic fallback prevents crashes

---

## Best Practices

### For Theme Developers

1. **Test Thoroughly**: Verify theme with various document types
2. **Consider Accessibility**: Ensure adequate contrast ratios
3. **Maintain Consistency**: Use harmonious color palettes
4. **Document Purpose**: Clearly name themes with descriptive titles
5. **Version Control**: Track theme changes in commit messages

### For Application Developers

1. **Extend Gradually**: Add new UI components to CSS systematically
2. **Maintain Backwards Compatibility**: Ensure old themes still work
3. **Performance First**: Keep CSS generation lightweight
4. **User Experience**: Provide immediate visual feedback
5. **Documentation**: Keep theme documentation current

### For Users

1. **Experiment**: Try different themes for different use cases
2. **Environment Matching**: Choose themes appropriate for lighting conditions
3. **Accessibility**: Use High Contrast theme if needed
4. **Feedback**: Report theme issues or suggestions

---

## Current Theme Catalog

### Built-in Themes (8 Total)

1. **Default** - Clean light theme with high contrast
2. **Dark** - Modern dark theme for reduced eye strain
3. **Solarized Light** - Warm, easy-on-the-eyes light theme
4. **Solarized Dark** - Popular dark theme with excellent contrast
5. **High Contrast** - Accessibility-focused black and white
6. **Monokai** - Popular editor theme with rich colors
7. **Purple Night** - Custom purple-themed dark mode
8. **Terminal Green** - Classic green-on-black terminal aesthetic

### Theme Categories

- **Light Themes**: Default, Solarized Light
- **Dark Themes**: Dark, Solarized Dark, Purple Night, Terminal Green
- **Accessibility**: High Contrast
- **Developer Themes**: Monokai, Terminal Green
- **Specialized**: Purple Night (custom aesthetic)

---

## Future Enhancements

### Potential Improvements

1. **Theme Import/Export**: Allow users to share custom themes
2. **Color Picker Interface**: Visual color selection tools
3. **Theme Categories**: Organize themes by type or use case
4. **Dynamic Themes**: Time-based or environment-responsive themes
5. **Plugin System**: Allow external theme modules

### Technical Roadmap

- **Configuration UI**: Graphical theme editing interface
- **Theme Validation**: Automatic contrast and accessibility checking
- **Advanced CSS**: Support for gradients, shadows, and animations
- **Theme Inheritance**: Base themes with variations
- **Online Sharing**: Community theme repository

---

*This documentation covers GUI Less Theme Manager v1.2.6. For the latest updates and theme additions, check the [project repository](https://github.com/juren53/guiless) and [changelog](https://github.com/juren53/guiless/blob/main/CHANGELOG.md).*

