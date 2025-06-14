#!/usr/bin/env python3
"""
GUI Less v1.2.6 - A GUI version of the less utility
Built with PyQt5 for enhanced text viewing with modern interface features

For version history and detailed changelog, see:
https://github.com/juren53/guiless/blob/main/CHANGELOG.md
"""

import sys
import os
import json
import webbrowser
import re
import textwrap
from pathlib import Path
try:
    import markdown
    MARKDOWN_AVAILABLE = True
except ImportError:
    MARKDOWN_AVAILABLE = False
from PyQt5.QtWidgets import (QDialog, QLineEdit, QPushButton, QDialogButtonBox,
    QApplication, QMainWindow, QTextEdit, QVBoxLayout, QHBoxLayout,
    QWidget, QMenuBar, QAction, QFileDialog, QMessageBox, QSplitter,
    QCheckBox, QLabel, QToolBar, QStatusBar, QComboBox
)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QSizeF
from PyQt5.QtGui import QFont, QKeySequence, QTextCursor, QTextDocument, QTextCharFormat, QColor


class ThemeManager:
    """Manages application themes and styling"""
    
    def __init__(self):
        self.themes = {
            'Default': {
                'name': 'Default',
                'background': '#ffffff',
                'text': '#000000',
                'selection_bg': '#3399ff',
                'selection_text': '#ffffff',
                'menubar_bg': '#f0f0f0',
                'menubar_text': '#000000',
                'toolbar_bg': '#f5f5f5',
                'statusbar_bg': '#e0e0e0',
                'statusbar_text': '#000000',
                'button_bg': '#e1e1e1',
                'button_text': '#000000',
                'button_hover': '#d4d4d4',
                'border': '#c0c0c0'
            },
            'Dark': {
                'name': 'Dark',
                'background': '#2b2b2b',
                'text': '#ffffff',
                'selection_bg': '#4a9eff',
                'selection_text': '#ffffff',
                'menubar_bg': '#3c3c3c',
                'menubar_text': '#ffffff',
                'toolbar_bg': '#404040',
                'statusbar_bg': '#333333',
                'statusbar_text': '#ffffff',
                'button_bg': '#454545',
                'button_text': '#ffffff',
                'button_hover': '#555555',
                'border': '#555555'
            },
            'Solarized Light': {
                'name': 'Solarized Light',
                'background': '#fdf6e3',
                'text': '#657b83',
                'selection_bg': '#268bd2',
                'selection_text': '#fdf6e3',
                'menubar_bg': '#eee8d5',
                'menubar_text': '#657b83',
                'toolbar_bg': '#f5f0e7',
                'statusbar_bg': '#eee8d5',
                'statusbar_text': '#657b83',
                'button_bg': '#eee8d5',
                'button_text': '#657b83',
                'button_hover': '#e8e2d4',
                'border': '#d3cbb7'
            },
            'Solarized Dark': {
                'name': 'Solarized Dark',
                'background': '#002b36',
                'text': '#839496',
                'selection_bg': '#268bd2',
                'selection_text': '#002b36',
                'menubar_bg': '#073642',
                'menubar_text': '#839496',
                'toolbar_bg': '#0a3c47',
                'statusbar_bg': '#073642',
                'statusbar_text': '#839496',
                'button_bg': '#073642',
                'button_text': '#839496',
                'button_hover': '#0c4956',
                'border': '#586e75'
            },
            'High Contrast': {
                'name': 'High Contrast',
                'background': '#000000',
                'text': '#ffffff',
                'selection_bg': '#ffff00',
                'selection_text': '#000000',
                'menubar_bg': '#000000',
                'menubar_text': '#ffffff',
                'toolbar_bg': '#000000',
                'statusbar_bg': '#000000',
                'statusbar_text': '#ffffff',
                'button_bg': '#333333',
                'button_text': '#ffffff',
                'button_hover': '#555555',
                'border': '#ffffff'
            },
            'Monokai': {
                'name': 'Monokai',
                'background': '#272822',
                'text': '#f8f8f2',
                'selection_bg': '#49483e',
                'selection_text': '#f8f8f2',
                'menubar_bg': '#3e3d32',
                'menubar_text': '#f8f8f2',
                'toolbar_bg': '#414339',
                'statusbar_bg': '#3e3d32',
                'statusbar_text': '#f8f8f2',
                'button_bg': '#49483e',
                'button_text': '#f8f8f2',
                'button_hover': '#5a594d',
                'border': '#75715e'
            },
            'Purple Night': {
                'name': 'Purple Night',
                'background': '#1e1e2e',
                'text': '#cdd6f4',
                'selection_bg': '#7c3aed',
                'selection_text': '#ffffff',
                'menubar_bg': '#2a2a40',
                'menubar_text': '#cdd6f4',
                'toolbar_bg': '#313244',
                'statusbar_bg': '#2a2a40',
                'statusbar_text': '#cdd6f4',
                'button_bg': '#45475a',
                'button_text': '#cdd6f4',
                'button_hover': '#585b70',
                'border': '#6c7086'
            },
            'Terminal Green': {
                'name': 'Terminal Green',
                'background': '#000000',
                'text': '#00ff00',
                'selection_bg': '#008000',
                'selection_text': '#000000',
                'menubar_bg': '#001100',
                'menubar_text': '#00ff00',
                'toolbar_bg': '#002200',
                'statusbar_bg': '#001100',
                'statusbar_text': '#00ff00',
                'button_bg': '#003300',
                'button_text': '#00ff00',
                'button_hover': '#004400',
                'border': '#008000'
            }
        }
        self.current_theme = 'Default'
    
    def get_theme_names(self):
        """Get list of available theme names"""
        return list(self.themes.keys())
    
    def get_theme(self, theme_name):
        """Get theme data by name"""
        return self.themes.get(theme_name, self.themes['Default'])
    
    def generate_stylesheet(self, theme_name):
        """Generate CSS stylesheet for the given theme"""
        theme = self.get_theme(theme_name)
        
        return f"""
        /* Main Window */
        QMainWindow {{
            background-color: {theme['background']};
            color: {theme['text']};
        }}
        
        /* Text Edit Areas */
        QTextEdit {{
            background-color: {theme['background']};
            color: {theme['text']};
            selection-background-color: {theme['selection_bg']};
            selection-color: {theme['selection_text']};
            border: 1px solid {theme['border']};
            font-family: 'Courier New', 'Consolas', monospace;
        }}
        
        /* Menu Bar */
        QMenuBar {{
            background-color: {theme['menubar_bg']};
            color: {theme['menubar_text']};
            border-bottom: 1px solid {theme['border']};
        }}
        
        QMenuBar::item {{
            background-color: transparent;
            padding: 4px 8px;
        }}
        
        QMenuBar::item:selected {{
            background-color: {theme['selection_bg']};
            color: {theme['selection_text']};
        }}
        
        QMenu {{
            background-color: {theme['menubar_bg']};
            color: {theme['menubar_text']};
            border: 1px solid {theme['border']};
        }}
        
        QMenu::item {{
            background-color: transparent;
            padding: 6px 12px;
        }}
        
        QMenu::item:selected {{
            background-color: {theme['selection_bg']};
            color: {theme['selection_text']};
        }}
        
        QMenu::separator {{
            height: 1px;
            background-color: {theme['border']};
            margin: 2px 0;
        }}
        
        /* Tool Bar */
        QToolBar {{
            background-color: {theme['toolbar_bg']};
            color: {theme['text']};
            border: 1px solid {theme['border']};
            spacing: 2px;
        }}
        
        QToolBar::separator {{
            background-color: {theme['border']};
            width: 1px;
            margin: 2px;
        }}
        
        /* Status Bar */
        QStatusBar {{
            background-color: {theme['statusbar_bg']};
            color: {theme['statusbar_text']};
            border-top: 1px solid {theme['border']};
        }}
        
        /* Buttons */
        QPushButton {{
            background-color: {theme['button_bg']};
            color: {theme['button_text']};
            border: 1px solid {theme['border']};
            border-radius: 3px;
            padding: 6px 12px;
            min-width: 80px;
        }}
        
        QPushButton:hover {{
            background-color: {theme['button_hover']};
        }}
        
        QPushButton:pressed {{
            background-color: {theme['selection_bg']};
            color: {theme['selection_text']};
        }}
        
        QPushButton:disabled {{
            background-color: {theme['border']};
            color: {theme['statusbar_text']};
        }}
        
        /* Combo Box */
        QComboBox {{
            background-color: {theme['button_bg']};
            color: {theme['button_text']};
            border: 1px solid {theme['border']};
            border-radius: 3px;
            padding: 4px 8px;
            min-width: 100px;
        }}
        
        QComboBox:hover {{
            background-color: {theme['button_hover']};
        }}
        
        QComboBox::drop-down {{
            border: none;
            width: 20px;
        }}
        
        QComboBox::down-arrow {{
            border-left: 5px solid transparent;
            border-right: 5px solid transparent;
            border-top: 5px solid {theme['text']};
        }}
        
        QComboBox QAbstractItemView {{
            background-color: {theme['menubar_bg']};
            color: {theme['menubar_text']};
            selection-background-color: {theme['selection_bg']};
            selection-color: {theme['selection_text']};
            border: 1px solid {theme['border']};
        }}
        
        /* Labels */
        QLabel {{
            background-color: transparent;
            color: {theme['text']};
        }}
        
        /* Line Edit */
        QLineEdit {{
            background-color: {theme['background']};
            color: {theme['text']};
            border: 1px solid {theme['border']};
            border-radius: 3px;
            padding: 4px;
            selection-background-color: {theme['selection_bg']};
            selection-color: {theme['selection_text']};
        }}
        
        /* Dialog */
        QDialog {{
            background-color: {theme['background']};
            color: {theme['text']};
        }}
        
        QDialogButtonBox QPushButton {{
            min-width: 70px;
        }}
        
        /* Splitter */
        QSplitter::handle {{
            background-color: {theme['border']};
            width: 2px;
        }}
        
        QSplitter::handle:hover {{
            background-color: {theme['selection_bg']};
        }}
        """


class ThemeDialog(QDialog):
    """Dialog for selecting application theme"""
    
    def __init__(self, current_theme, theme_manager, parent=None):
        super().__init__(parent)
        self.theme_manager = theme_manager
        self.selected_theme = current_theme
        
        self.setWindowTitle("Select Theme")
        self.setFixedSize(400, 200)
        
        layout = QVBoxLayout(self)
        
        # Theme selection
        layout.addWidget(QLabel("Choose a theme:"))
        
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(self.theme_manager.get_theme_names())
        self.theme_combo.setCurrentText(current_theme)
        self.theme_combo.currentTextChanged.connect(self.on_theme_changed)
        layout.addWidget(self.theme_combo)
        
        # Preview label
        self.preview_label = QLabel("Preview: This is how text will look with the selected theme")
        self.preview_label.setStyleSheet("padding: 15px; border: 1px solid gray; min-height: 40px;")
        self.preview_label.setWordWrap(True)
        layout.addWidget(self.preview_label)
        
        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
        # Set initial preview
        self.update_preview()
    
    def on_theme_changed(self, theme_name):
        """Handle theme selection change"""
        self.selected_theme = theme_name
        self.update_preview()
    
    def update_preview(self):
        """Update the preview with selected theme colors"""
        theme = self.theme_manager.get_theme(self.selected_theme)
        self.preview_label.setStyleSheet(f"""
            background-color: {theme['background']};
            color: {theme['text']};
            padding: 10px;
            border: 1px solid {theme['border']};
        """)
    
    def get_selected_theme(self):
        """Get the selected theme name"""
        return self.selected_theme


class FindDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Find")
        self.setFixedSize(300, 100)

        self.layout = QVBoxLayout(self)
        self.find_input = QLineEdit(self)
        self.layout.addWidget(self.find_input)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    def text(self):
        return self.find_input.text()

class LessTextEdit(QTextEdit):
    """Custom QTextEdit with less-like functionality and zoom support"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        # Line wrap will be set after word_wrap_enabled is initialized
        
        # Set up font
        font = QFont("Courier New", 10)
        font.setFixedPitch(True)
        self.setFont(font)
        
        # Track original font size for zooming
        self.base_font_size = 10
        self.zoom_factor = 1.0
        
        # Line numbering state
        self.show_line_numbers = False
        
        # Word wrap state
        self.word_wrap_enabled = True  # Enable word wrap by default
        self.setLineWrapMode(QTextEdit.WidgetWidth if self.word_wrap_enabled else QTextEdit.NoWrap)
        
        # Pagination support
        self.original_content = ""
        self.current_page = 1
        self.lines_per_page = 0
        self.total_pages = 0
        
    def wheelEvent(self, event):
        """Handle Ctrl+Scroll wheel for zooming"""
        if event.modifiers() & Qt.ControlModifier:
            # Zoom in/out with Ctrl+Scroll
            delta = event.angleDelta().y()
            if delta > 0:
                self.zoom_in()
            else:
                self.zoom_out()
            event.accept()
        else:
            # Normal scrolling
            super().wheelEvent(event)
    
    def zoom_in(self):
        """Increase font size"""
        self.zoom_factor *= 1.1
        self.update_font_size()
    
    def zoom_out(self):
        """Decrease font size"""
        self.zoom_factor /= 1.1
        self.update_font_size()
    
    def reset_zoom(self):
        """Reset zoom to default"""
        self.zoom_factor = 1.0
        self.update_font_size()
    
    def update_font_size(self):
        """Update font size based on zoom factor"""
        new_size = int(self.base_font_size * self.zoom_factor)
        font = self.font()
        font.setPointSize(new_size)
        self.setFont(font)
    
    def load_file(self, file_path):
        """Load and display a text file"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
                content = file.read()
                self.original_content = content
                self.setPlainText(content)
                self.calculate_pagination()
                return True
        except Exception as e:
            QMessageBox.critical(self.parent(), "Error", f"Failed to open file: {str(e)}")
            return False
    
    def calculate_pagination(self):
        """Calculate pagination using viewport-based content fitting"""
        if not self.original_content:
            return
        
        # Use direct viewport-based pagination for consistent page filling
        self.calculate_viewport_pagination()
    
    def calculate_viewport_pagination(self):
        """Calculate pagination using visual lines for perfect viewport fitting"""
        if not self.original_content:
            return
        
        lines = self.original_content.split('\n')
        
        if not self.word_wrap_enabled:
            # No-wrap mode: simple line-based pagination
            viewport_height = self.viewport().height()
            font_metrics = self.fontMetrics()
            line_height = font_metrics.lineSpacing()
            self.lines_per_page = max(1, (viewport_height - 40) // line_height)
            total_lines = len(lines)
            self.total_pages = max(1, (total_lines + self.lines_per_page - 1) // self.lines_per_page)
            return
        
        # For word wrap mode, use visual line-based pagination
        self.calculate_visual_line_pagination(lines)
    
    def calculate_visual_line_pagination(self, lines):
        """Calculate pagination using visual lines with proper line breaking"""
        # Get viewport metrics
        viewport_height = self.viewport().height() - 40  # Leave margin
        font_metrics = self.fontMetrics()
        line_height = font_metrics.lineSpacing()
        char_width = font_metrics.averageCharWidth()
        
        # Calculate how many visual lines fit per page
        visual_lines_per_page = max(1, viewport_height // line_height)
        
        # Calculate viewport width in characters
        viewport_width = self.viewport().width() - 40  # Account for margins
        chars_per_line = max(1, viewport_width // char_width)
        
        # Convert all text lines to visual lines using textwrap
        all_visual_lines = []
        visual_to_text_line_map = []  # Track which text line each visual line came from
        
        for text_line_num, text_line in enumerate(lines):
            if not text_line.strip():  # Empty line
                all_visual_lines.append('')
                visual_to_text_line_map.append(text_line_num + 1)  # 1-based line numbers
            else:
                # Use textwrap to break long lines properly
                wrapped_lines = textwrap.wrap(
                    text_line, 
                    width=chars_per_line,
                    break_long_words=True,
                    break_on_hyphens=True
                )
                if wrapped_lines:
                    all_visual_lines.extend(wrapped_lines)
                    # Map each visual line to its original text line
                    for _ in wrapped_lines:
                        visual_to_text_line_map.append(text_line_num + 1)
                else:
                    all_visual_lines.append('')  # Empty wrapped line
                    visual_to_text_line_map.append(text_line_num + 1)
        
        # Create page breaks based on visual lines
        total_visual_lines = len(all_visual_lines)
        self.total_pages = max(1, (total_visual_lines + visual_lines_per_page - 1) // visual_lines_per_page)
        
        # Store visual lines and pagination info
        self.visual_lines = all_visual_lines
        self.visual_lines_per_page = visual_lines_per_page
        self.visual_to_text_line_map = visual_to_text_line_map
        self.use_visual_line_pagination = True
    
    def calculate_dynamic_page_breaks(self, lines):
        """Calculate page breaks by measuring actual content height in viewport"""
        viewport_height = self.viewport().height() - 60  # Leave margin for safety
        
        page_breaks = []
        current_page_start = 0
        
        while current_page_start < len(lines):
            # Find how many lines fit in one viewport
            lines_that_fit = self.find_lines_that_fit_viewport(lines, current_page_start, viewport_height)
            
            if lines_that_fit == 0:
                lines_that_fit = 1  # Always include at least one line
            
            page_end = min(current_page_start + lines_that_fit - 1, len(lines) - 1)
            page_breaks.append((current_page_start, page_end))
            
            current_page_start = page_end + 1
        
        self.page_breaks = page_breaks
        self.total_pages = len(page_breaks)
        self.use_dynamic_breaks = True
    
    def find_lines_that_fit_viewport(self, lines, start_line, max_height):
        """Find how many lines fit in viewport without scrolling"""
        # Start with a reasonable guess and adjust
        test_line_count = 1
        max_test_count = min(50, len(lines) - start_line)  # Don't test too many
        
        while test_line_count <= max_test_count:
            # Test content with current line count
            end_line = min(start_line + test_line_count, len(lines))
            test_lines = lines[start_line:end_line]
            test_content = '\n'.join(test_lines)
            
            # Measure actual height this content would take
            content_height = self.measure_content_height(test_content)
            
            if content_height > max_height:
                # Too much content, return previous count
                return max(1, test_line_count - 1)
            
            test_line_count += 1
        
        # All remaining lines fit
        return max_test_count
    
    def measure_content_height(self, content):
        """Measure the actual height content would take in the viewport"""
        # Create a temporary QTextDocument to measure content
        temp_doc = QTextDocument()
        temp_doc.setPlainText(content)
        temp_doc.setDefaultFont(self.font())
        temp_doc.setTextWidth(self.viewport().width() - 20)
        
        # Return the actual height needed
        return temp_doc.documentLayout().documentSize().height()
    
    def calculate_fallback_pagination(self):
        """Fallback pagination calculation when HTML method fails"""
        if not self.original_content:
            return
            
        # Get viewport height and font metrics
        viewport_height = self.viewport().height()
        font_metrics = self.fontMetrics()
        line_height = font_metrics.lineSpacing()
        
        # Calculate lines per page (subtract some for margins)
        self.lines_per_page = max(1, (viewport_height - 20) // line_height)
        
        # Calculate total pages based on word wrap mode
        if self.word_wrap_enabled:
            # For word wrap, use aggressive reduction for long-line documents
            lines = self.original_content.split('\n')
            total_lines = len(lines)
            
            # Analyze line lengths for wrapping estimation
            long_line_count = sum(1 for line in lines if len(line) > 100)
            long_line_ratio = long_line_count / max(total_lines, 1) if total_lines > 0 else 0
            
            if long_line_ratio > 0.4:  # More than 40% of lines are very long
                # Extremely conservative - assume 8x wrapping for news articles
                effective_lines_per_page = max(1, self.lines_per_page // 8)
            elif long_line_ratio > 0.2:  # 20-40% of lines are long
                # Very conservative pagination - assume 6x wrapping
                effective_lines_per_page = max(1, self.lines_per_page // 6)
            else:
                # Normal text - assume 4x wrapping
                effective_lines_per_page = max(1, self.lines_per_page // 4)
            
            self.total_pages = max(1, (total_lines + effective_lines_per_page - 1) // effective_lines_per_page)
            self.effective_lines_per_page = effective_lines_per_page
        else:
            # Simple line-based pagination for no-wrap mode
            total_lines = len(self.original_content.split('\n'))
            self.total_pages = max(1, (total_lines + self.lines_per_page - 1) // self.lines_per_page)
    
    def calculate_wrapped_pagination(self):
        """Calculate pagination when word wrap is enabled - content-density-based approach"""
        lines = self.original_content.split('\n')
        total_lines = len(lines)
        
        # Use content-density-based pagination for more consistent page sizes
        # Target: ~800-1200 characters per page for comfortable reading
        target_chars_per_page = 1000
        
        # Calculate page breaks based on content density
        self.page_breaks = self.calculate_content_based_breaks(lines, target_chars_per_page)
        self.total_pages = len(self.page_breaks)
        
        # Store for content setting
        self.content_based_pagination = True
    
    def convert_text_to_html(self, text_content):
        """Convert plain text to HTML for better pagination control"""
        # Detect if this might be markdown
        is_markdown = (
            MARKDOWN_AVAILABLE and 
            (
                '# ' in text_content or 
                '## ' in text_content or 
                '**' in text_content or 
                '*' in text_content or 
                '[' in text_content and '](' in text_content
            )
        )
        
        if is_markdown:
            # Convert markdown to HTML
            try:
                html_content = markdown.markdown(text_content)
                return f"<html><body style='font-family: Courier New, monospace; font-size: 10pt;'>{html_content}</body></html>"
            except Exception:
                # Fallback to plain text processing
                pass
        
        # Convert plain text to HTML with proper paragraph structure
        lines = text_content.split('\n')
        html_lines = []
        in_paragraph = False
        
        for line in lines:
            line = line.strip()
            if not line:  # Empty line
                if in_paragraph:
                    html_lines.append('</p>')
                    in_paragraph = False
                html_lines.append('<br>')
            else:
                if not in_paragraph:
                    html_lines.append('<p>')
                    in_paragraph = True
                # Escape HTML characters
                line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                html_lines.append(line + ' ')
        
        if in_paragraph:
            html_lines.append('</p>')
        
        html_content = ''.join(html_lines)
        return f"<html><body style='font-family: Courier New, monospace; font-size: 10pt;'>{html_content}</body></html>"
    
    def calculate_html_pagination(self):
        """Calculate pagination using QTextDocument with HTML content"""
        if not self.original_content:
            return
        
        # Convert text to HTML
        html_content = self.convert_text_to_html(self.original_content)
        
        # Create a temporary QTextDocument for pagination calculation
        temp_doc = QTextDocument()
        temp_doc.setHtml(html_content)
        temp_doc.setDefaultFont(self.font())
        
        # Set the page size based on viewport
        viewport_height = self.viewport().height() - 40  # Leave margin
        temp_doc.setPageSize(QSizeF(self.viewport().size()))
        
        # Calculate total pages
        self.total_pages = max(1, temp_doc.pageCount())
        
        # Store HTML content and document for later use
        self.html_content = html_content
        self.html_pagination = True
        
        return self.total_pages
    
    def calculate_content_based_breaks(self, lines, target_chars_per_page):
        """Calculate page breaks based on content density rather than line count"""
        page_breaks = []
        current_page_chars = 0
        current_page_start = 0
        
        for i, line in enumerate(lines):
            line_length = len(line)
            
            # Check if adding this line would exceed target
            if current_page_chars + line_length > target_chars_per_page and current_page_chars > 0:
                # Create page break
                page_breaks.append((current_page_start, i - 1))
                current_page_start = i
                current_page_chars = line_length
            else:
                current_page_chars += line_length + 1  # +1 for newline
        
        # Add final page if there's remaining content
        if current_page_start < len(lines):
            page_breaks.append((current_page_start, len(lines) - 1))
        
        return page_breaks if page_breaks else [(0, len(lines) - 1)]
    
    def set_page_content(self, page_number):
        """Set content for a specific page"""
        if not self.original_content or page_number < 1:
            return
            
        self.current_page = page_number
        
        if self.word_wrap_enabled:
            self.set_wrapped_page_content(page_number)
        else:
            self.set_nowrap_page_content(page_number)
    
    def set_nowrap_page_content(self, page_number):
        """Set page content for no-wrap mode"""
        lines = self.original_content.split('\n')
        
        # Calculate start and end lines for this page
        start_line = (page_number - 1) * self.lines_per_page
        end_line = min(start_line + self.lines_per_page, len(lines))
        
        # Get page content
        if start_line < len(lines):
            page_lines = lines[start_line:end_line]
            page_content = '\n'.join(page_lines)
        else:
            page_content = ""  # Beyond end of document
        
        # Apply line numbers if enabled
        if self.show_line_numbers and page_content:
            numbered_lines = []
            total_lines = len(lines)
            width = len(str(total_lines))
            
            for i, line in enumerate(page_lines, start_line + 1):
                line_num = str(i).rjust(width)
                numbered_lines.append(f"{line_num}: {line}")
            
            page_content = '\n'.join(numbered_lines)
        
        self.setPlainText(page_content)
        # Ensure cursor and scroll position are at the top of the page
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.Start)
        self.setTextCursor(cursor)
        self.ensureCursorVisible()
    
    def set_wrapped_page_content(self, page_number):
        """Set page content for word wrap mode using visual line pagination"""
        # Check if we have visual line pagination (perfect page filling)
        if hasattr(self, 'use_visual_line_pagination') and hasattr(self, 'visual_lines'):
            # Use the visual lines that perfectly fill pages
            visual_lines_per_page = getattr(self, 'visual_lines_per_page', 25)
            
            start_visual_line = (page_number - 1) * visual_lines_per_page
            end_visual_line = min(start_visual_line + visual_lines_per_page, len(self.visual_lines))
            
            if start_visual_line < len(self.visual_lines):
                page_visual_lines = self.visual_lines[start_visual_line:end_visual_line]
                page_content = '\n'.join(page_visual_lines)
                
                # Apply line numbers if enabled
                if self.show_line_numbers and hasattr(self, 'visual_to_text_line_map'):
                    numbered_lines = []
                    total_text_lines = len(self.original_content.split('\n'))
                    width = len(str(total_text_lines))
                    
                    for i, visual_line in enumerate(page_visual_lines):
                        visual_line_index = start_visual_line + i
                        if visual_line_index < len(self.visual_to_text_line_map):
                            text_line_num = self.visual_to_text_line_map[visual_line_index]
                            line_num = str(text_line_num).rjust(width)
                            numbered_lines.append(f"{line_num}: {visual_line}")
                        else:
                            # Fallback if mapping is incomplete
                            numbered_lines.append(f"{'?'.rjust(width)}: {visual_line}")
                    
                    page_content = '\n'.join(numbered_lines)
                
                self.setPlainText(page_content)
            else:
                self.setPlainText("")
        else:
            # Fallback to line-based pagination
            lines = self.original_content.split('\n')
            effective_lines_per_page = getattr(self, 'effective_lines_per_page', max(1, self.lines_per_page // 3))
            
            start_line = (page_number - 1) * effective_lines_per_page
            end_line = min(start_line + effective_lines_per_page, len(lines))
            
            if start_line < len(lines):
                page_lines = lines[start_line:end_line]
                page_content = '\n'.join(page_lines)
                
                # Apply line numbers if enabled
                if self.show_line_numbers:
                    numbered_lines = []
                    total_lines = len(lines)
                    width = len(str(total_lines))
                    
                    for i, line in enumerate(page_lines, start_line + 1):
                        line_num = str(i).rjust(width)
                        numbered_lines.append(f"{line_num}: {line}")
                    
                    page_content = '\n'.join(numbered_lines)
                
                self.setPlainText(page_content)
            else:
                self.setPlainText("")
        
        # Ensure cursor and scroll position are at the top of the page
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.Start)
        self.setTextCursor(cursor)
        self.ensureCursorVisible()
    
    def set_html_page_content(self, page_number):
        """Set page content using HTML-based pagination for perfect viewport fitting"""
        if not hasattr(self, 'html_content') or not self.html_content:
            # Fallback if HTML content not available
            self.set_wrapped_page_content_fallback(page_number)
            return
        
        # Create a QTextDocument for page extraction
        temp_doc = QTextDocument()
        temp_doc.setHtml(self.html_content)
        temp_doc.setDefaultFont(self.font())
        temp_doc.setPageSize(QSizeF(self.viewport().size()))
        
        # Calculate page content bounds
        page_height = self.viewport().height() - 40  # Leave margin
        start_y = (page_number - 1) * page_height
        end_y = start_y + page_height
        
        # Extract text that fits in the page bounds
        cursor = QTextCursor(temp_doc)
        cursor.movePosition(QTextCursor.Start)
        
        # Move to start position for this page
        while cursor.position() < temp_doc.characterCount() - 1:
            rect = temp_doc.documentLayout().blockBoundingRect(cursor.block())
            if rect.y() >= start_y:
                break
            cursor.movePosition(QTextCursor.NextBlock)
        
        page_start_pos = cursor.position()
        
        # Find end position for this page
        while cursor.position() < temp_doc.characterCount() - 1:
            rect = temp_doc.documentLayout().blockBoundingRect(cursor.block())
            if rect.y() + rect.height() > end_y:
                break
            cursor.movePosition(QTextCursor.NextBlock)
        
        page_end_pos = cursor.position()
        
        # Extract the page content
        page_cursor = QTextCursor(temp_doc)
        page_cursor.setPosition(page_start_pos)
        page_cursor.setPosition(page_end_pos, QTextCursor.KeepAnchor)
        page_text = page_cursor.selectedText()
        
        # Apply line numbers if enabled
        if self.show_line_numbers and page_text:
            lines = page_text.split('\n')
            numbered_lines = []
            total_lines = len(self.original_content.split('\n'))
            width = len(str(total_lines))
            
            # Estimate starting line number based on position
            start_line = max(1, (page_number - 1) * 10)  # Rough estimate
            
            for i, line in enumerate(lines, start_line):
                line_num = str(i).rjust(width)
                numbered_lines.append(f"{line_num}: {line}")
            
            page_text = '\n'.join(numbered_lines)
        
        # Set the page content
        if page_text.strip():
            self.setPlainText(page_text)
        else:
            self.setPlainText("")
    
    def set_wrapped_page_content_fallback(self, page_number):
        """Fallback method for wrapped content pagination"""
        # Use smaller chunks for better visual line approximation
        lines = self.original_content.split('\n')
        
        # Use the effective_lines_per_page calculated in calculate_wrapped_pagination
        effective_lines_per_page = getattr(self, 'effective_lines_per_page', max(1, self.lines_per_page // 3))
        
        start_line = (page_number - 1) * effective_lines_per_page
        end_line = min(start_line + effective_lines_per_page, len(lines))
        
        if start_line < len(lines):
            page_lines = lines[start_line:end_line]
            page_content = '\n'.join(page_lines)
            
            # Apply line numbers if enabled
            if self.show_line_numbers:
                numbered_lines = []
                total_lines = len(lines)
                width = len(str(total_lines))
                
                for i, line in enumerate(page_lines, start_line + 1):
                    line_num = str(i).rjust(width)
                    numbered_lines.append(f"{line_num}: {line}")
                
                page_content = '\n'.join(numbered_lines)
            
            self.setPlainText(page_content)
        else:
            self.setPlainText("")
        
        # Ensure cursor and scroll position are at the top of the page
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.Start)
        self.setTextCursor(cursor)
        self.ensureCursorVisible()
    
    def resizeEvent(self, event):
        """Recalculate pagination when window is resized"""
        super().resizeEvent(event)
        if hasattr(self, 'original_content') and self.original_content:
            self.calculate_pagination()
            # Re-display current page with new pagination
            self.set_page_content(self.current_page)
    
    def toggle_line_numbers(self, show):
        """Toggle line number display"""
        self.show_line_numbers = show
        # Re-display current page to apply/remove line numbers
        self.set_page_content(self.current_page)
    
    def toggle_word_wrap(self, enable):
        """Toggle word wrap mode"""
        self.word_wrap_enabled = enable
        self.setLineWrapMode(QTextEdit.WidgetWidth if enable else QTextEdit.NoWrap)
        
        # Recalculate pagination and refresh display
        if hasattr(self, 'original_content') and self.original_content:
            self.calculate_pagination()
            self.set_page_content(self.current_page)


class GuiLess(QMainWindow):
    """Main GUI Less application window"""
    
    def __init__(self):
        super().__init__()
        self.current_file = None
        self.two_page_mode = True  # Default to two page mode
        self.current_left_page = 1
        
        # Recent files management
        self.max_recent_files = 10
        self.recent_files = []
        self.last_directory = str(Path.home())  # Default to home directory
        self.config_dir = Path.home() / '.guiless'
        self.config_file = self.config_dir / 'config.json'
        
        # Theme management
        self.theme_manager = ThemeManager()
        self.current_theme = 'Default'
        
        # Two-page navigation mode
        self.sliding_window_mode = True  # True for sliding (1-2, 2-3), False for spread (1-2, 3-4)
        
        # Load configuration and initialize UI
        self.load_config()
        self.init_ui()
        self.apply_theme(self.current_theme)
    
        # Update navigation mode UI after loading config
        self.update_navigation_mode_ui()
        
        # Set fullscreen mode by default
        self.showMaximized()
    
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("GUI Less - Text Viewer")
        self.setGeometry(100, 100, 1000, 700)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create layout
        layout = QVBoxLayout(central_widget)
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create toolbar
        self.create_toolbar()
        
        # Create main content area
        self.create_content_area(layout)
        
        # Create status bar
        self.create_status_bar()
        
        # Set up keyboard shortcuts
        self.setup_shortcuts()
    
    def create_menu_bar(self):
        """Create the menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu('File')
        
        open_action = QAction('Open...', self)
        open_action.setShortcut(QKeySequence.Open)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        # Recent files submenu
        self.recent_menu = file_menu.addMenu('Recent Files')
        self.update_recent_menu()
        
        file_menu.addSeparator()
        
        exit_action = QAction('Exit', self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Edit menu
        edit_menu = menubar.addMenu('Edit')
        
        find_action = QAction('Find...', self)
        find_action.setShortcut(QKeySequence.Find)
        find_action.triggered.connect(self.find_text)
        edit_menu.addAction(find_action)
        
        edit_menu.addSeparator()
        
        # View options
        self.line_numbers_action = QAction('Show Line Numbers', self)
        self.line_numbers_action.setCheckable(True)
        self.line_numbers_action.triggered.connect(self.toggle_line_numbers)
        edit_menu.addAction(self.line_numbers_action)
        
        self.two_page_action = QAction('Two Page Mode', self)
        self.two_page_action.setCheckable(True)
        self.two_page_action.setChecked(True)  # Default to checked
        self.two_page_action.triggered.connect(self.toggle_two_page_mode)
        edit_menu.addAction(self.two_page_action)
        
        edit_menu.addSeparator()
        
        self.word_wrap_action = QAction('Word Wrap', self)
        self.word_wrap_action.setCheckable(True)
        self.word_wrap_action.setChecked(True)  # Default to enabled
        self.word_wrap_action.triggered.connect(self.toggle_word_wrap)
        edit_menu.addAction(self.word_wrap_action)
        
        # View menu
        view_menu = menubar.addMenu('View')
        
        theme_action = QAction('Theme...', self)
        theme_action.triggered.connect(self.change_theme)
        view_menu.addAction(theme_action)
        
        view_menu.addSeparator()
        
        # Zoom submenu
        zoom_menu = view_menu.addMenu('Zoom')
        
        zoom_in_action = QAction('Zoom In', self)
        zoom_in_action.setShortcut('Ctrl+=')
        zoom_in_action.triggered.connect(self.zoom_in)
        zoom_menu.addAction(zoom_in_action)
        
        zoom_out_action = QAction('Zoom Out', self)
        zoom_out_action.setShortcut('Ctrl+-')
        zoom_out_action.triggered.connect(self.zoom_out)
        zoom_menu.addAction(zoom_out_action)
        
        zoom_reset_action = QAction('Reset Zoom', self)
        zoom_reset_action.setShortcut('Ctrl+0')
        zoom_reset_action.triggered.connect(self.reset_zoom)
        zoom_menu.addAction(zoom_reset_action)
        
        view_menu.addSeparator()
        
        # Two-page navigation mode submenu
        nav_mode_menu = view_menu.addMenu('Two-Page Navigation')
        
        self.sliding_window_action = QAction('Sliding Window View (1-2, 2-3, 3-4...)', self)
        self.sliding_window_action.setCheckable(True)
        self.sliding_window_action.setChecked(True)  # Default
        self.sliding_window_action.triggered.connect(self.set_sliding_window_mode)
        nav_mode_menu.addAction(self.sliding_window_action)
        
        self.spread_view_action = QAction('Spread View (1-2, 3-4, 5-6...)', self)
        self.spread_view_action.setCheckable(True)
        self.spread_view_action.triggered.connect(self.set_spread_view_mode)
        nav_mode_menu.addAction(self.spread_view_action)
        
        # Help menu
        help_menu = menubar.addMenu('Help')
        
        user_guide_action = QAction('User Guide', self)
        user_guide_action.triggered.connect(self.open_user_guide)
        help_menu.addAction(user_guide_action)
        
        help_menu.addSeparator()
        
        about_action = QAction('About', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def create_toolbar(self):
        """Create the toolbar"""
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        # Open file button
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        toolbar.addAction(open_action)
    
    def create_content_area(self, layout):
        """Create the main content viewing area"""
        # Create splitter for potential two-page mode
        self.splitter = QSplitter(Qt.Horizontal)
        
        # Create text editors
        self.text_edit_1 = LessTextEdit()  # Left page
        self.text_edit_2 = LessTextEdit()  # Right page
        
        # Add first text editor
        self.splitter.addWidget(self.text_edit_1)
        
        # Add second editor for two-page mode (default)
        self.splitter.addWidget(self.text_edit_2)
        
        layout.addWidget(self.splitter)
        
        # Create navigation controls for two-page mode
        nav_layout = QHBoxLayout()
        
        # Button text will be set based on navigation mode
        self.prev_page_btn = QPushButton("Previous Page")
        self.prev_page_btn.clicked.connect(self.previous_pages)
        self.prev_page_btn.hide()
    
        self.next_page_btn = QPushButton("Next Page")
        self.next_page_btn.clicked.connect(self.next_pages)
        self.next_page_btn.hide()
        
        self.page_info_label = QLabel("")
        self.page_info_label.hide()
        
        nav_layout.addWidget(self.prev_page_btn)
        nav_layout.addStretch()
        nav_layout.addWidget(self.page_info_label)
        nav_layout.addStretch()
        nav_layout.addWidget(self.next_page_btn)
        
        # Show navigation controls by default (two-page mode)
        self.prev_page_btn.show()
        self.next_page_btn.show()
        self.page_info_label.show()
    
        # Set initial button text based on navigation mode
        self.update_navigation_button_text()
        
        layout.addLayout(nav_layout)
    
    def create_status_bar(self):
        """Create the status bar"""
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        # Add permanent widgets to status bar
        self.line_col_label = QLabel("Line: 1, Col: 1")
        self.status_bar.addPermanentWidget(self.line_col_label)
        
        # Connect cursor position updates
        self.text_edit_1.cursorPositionChanged.connect(self.update_cursor_position)
    
    def setup_shortcuts(self):
        """Set up keyboard shortcuts similar to less"""
        # Navigation shortcuts (less-like)
        shortcuts = {
            'q': self.close,  # Quit
            'Ctrl+C': self.close,  # Alternative quit
            '?': self.find_text,  # Search
            'n': self.find_next,  # Find next
            'N': self.find_previous,  # Find previous
            'Space': self.next_pages,  # Next pages (like less)
            'b': self.previous_pages,  # Previous pages (like less)
        }
        
        for key, func in shortcuts.items():
            action = QAction(self)
            action.setShortcut(key)
            action.triggered.connect(func)
            self.addAction(action)
    
    def load_config(self):
        """Load configuration including recent files, last directory, and theme"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    config_data = json.load(f)
                    
                # Handle both old format (list) and new format (dict)
                if isinstance(config_data, list):
                    # Old format - just recent files
                    self.recent_files = config_data
                    self.last_directory = str(Path.home())  # Default
                    self.current_theme = 'Default'  # Default theme
                    self.sliding_window_mode = True  # Default navigation mode
                else:
                    # New format - dict with all settings
                    self.recent_files = config_data.get('recent_files', [])
                    self.last_directory = config_data.get('last_directory', str(Path.home()))
                    self.current_theme = config_data.get('theme', 'Default')
                    self.sliding_window_mode = config_data.get('sliding_window_mode', True)
                    
                # Remove files that no longer exist
                self.recent_files = [f for f in self.recent_files if os.path.exists(f)]
            else:
                self.recent_files = []
                self.last_directory = str(Path.home())
                self.current_theme = 'Default'
                self.sliding_window_mode = True
        except (json.JSONDecodeError, IOError):
            self.recent_files = []
            self.last_directory = str(Path.home())
            self.current_theme = 'Default'
            self.sliding_window_mode = True
    
    def save_config(self):
        """Save configuration including recent files, last directory, and theme"""
        try:
            # Create config directory if it doesn't exist
            self.config_dir.mkdir(exist_ok=True)
            
            config_data = {
                'recent_files': self.recent_files,
                'last_directory': self.last_directory,
                'theme': self.current_theme,
                'sliding_window_mode': self.sliding_window_mode
            }
            
            with open(self.config_file, 'w') as f:
                json.dump(config_data, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save config: {e}")
    
    def add_recent_file(self, file_path):
        """Add a file to the recent files list"""
        file_path = os.path.abspath(file_path)
        
        # Remove if already in list
        if file_path in self.recent_files:
            self.recent_files.remove(file_path)
        
        # Add to beginning of list
        self.recent_files.insert(0, file_path)
        
        # Limit list size
        self.recent_files = self.recent_files[:self.max_recent_files]
        
        # Save and update menu
        self.save_config()
        self.update_recent_menu()
    
    def update_recent_menu(self):
        """Update the recent files menu"""
        self.recent_menu.clear()
        
        if not self.recent_files:
            no_recent = QAction('No recent files', self)
            no_recent.setEnabled(False)
            self.recent_menu.addAction(no_recent)
            return
        
        for i, file_path in enumerate(self.recent_files):
            if os.path.exists(file_path):
                # Create action with filename and shortcut
                filename = os.path.basename(file_path)
                action = QAction(f"{i + 1}. {filename}", self)
                action.setToolTip(file_path)
                
                # Add keyboard shortcut for first 9 files
                if i < 9:
                    action.setShortcut(f"Ctrl+{i + 1}")
                
                # Connect to open function
                action.triggered.connect(lambda checked, path=file_path: self.open_recent_file(path))
                self.recent_menu.addAction(action)
        
        # Add separator and clear option
        self.recent_menu.addSeparator()
        clear_action = QAction('Clear Recent Files', self)
        clear_action.triggered.connect(self.clear_recent_files)
        self.recent_menu.addAction(clear_action)
    
    def open_recent_file(self, file_path):
        """Open a file from the recent files list"""
        if os.path.exists(file_path):
            if self.text_edit_1.load_file(file_path):
                self.current_file = file_path
                # Update last directory when opening recent file
                self.last_directory = str(Path(file_path).parent)
                self.setWindowTitle(f"GUI Less - {os.path.basename(file_path)}")
                self.status_bar.showMessage(f"Loaded: {file_path}")
                
                # Update recent files (moves to top)
                self.add_recent_file(file_path)
                
                # If in two-page mode, set up pagination
                if self.two_page_mode:
                    self.setup_two_page_display()
        else:
            # File no longer exists, remove from recent files
            if file_path in self.recent_files:
                self.recent_files.remove(file_path)
                self.save_config()
                self.update_recent_menu()
            QMessageBox.warning(self, "File Not Found", f"The file '{file_path}' no longer exists.")
    
    def clear_recent_files(self):
        """Clear the recent files list"""
        reply = QMessageBox.question(
            self, 'Clear Recent Files',
            'Are you sure you want to clear all recent files?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.recent_files = []
            self.save_config()
            self.update_recent_menu()
    
    def load_most_recent_file(self):
        """Load the most recent file if available"""
        if self.recent_files and os.path.exists(self.recent_files[0]):
            self.open_recent_file(self.recent_files[0])
    
    def open_file(self):
        """Open a file dialog and load selected file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Text File", self.last_directory, "Text Files (*.txt);;All Files (*)"
        )
        
        if file_path:
            if self.text_edit_1.load_file(file_path):
                self.current_file = file_path
                # Update last directory
                self.last_directory = str(Path(file_path).parent)
                self.setWindowTitle(f"GUI Less - {os.path.basename(file_path)}")
                self.status_bar.showMessage(f"Loaded: {file_path}")
                
                # Add to recent files
                self.add_recent_file(file_path)
                
                # If in two-page mode, set up pagination
                if self.two_page_mode:
                    self.setup_two_page_display()
    
    def toggle_line_numbers(self):
        """Toggle line number display"""
        show = self.line_numbers_action.isChecked()
        self.text_edit_1.toggle_line_numbers(show)
        if self.two_page_mode:
            self.text_edit_2.toggle_line_numbers(show)
    
    def toggle_word_wrap(self):
        """Toggle word wrap mode"""
        enable = self.word_wrap_action.isChecked()
        self.text_edit_1.toggle_word_wrap(enable)
        if self.two_page_mode:
            self.text_edit_2.toggle_word_wrap(enable)
            # Update page display after wrap mode change
            self.update_page_display()
    
    def toggle_two_page_mode(self):
        """Toggle between single and two-page mode"""
        self.two_page_mode = self.two_page_action.isChecked()
        
        if self.two_page_mode:
            # Show second editor and navigation
            self.splitter.addWidget(self.text_edit_2)
            self.text_edit_2.show()
            self.prev_page_btn.show()
            self.next_page_btn.show()
            self.page_info_label.show()
            
            # Set up pagination if file is loaded
            if self.current_file:
                self.setup_two_page_display()
            
            # Split equally
            self.splitter.setSizes([500, 500])
        else:
            # Hide second editor but keep navigation for single-page pagination
            self.text_edit_2.hide()
            
            # Set up single page pagination if file is loaded
            if self.current_file:
                self.setup_single_page_display()
            else:
                # No file loaded, hide navigation
                self.prev_page_btn.hide()
                self.next_page_btn.hide()
                self.page_info_label.hide()
    
    def setup_single_page_display(self):
        """Set up single page display with pagination if needed"""
        if not self.current_file:
            return
        
        # Calculate pagination for single page
        self.text_edit_1.calculate_pagination()
        
        # Check if pagination is needed (more than one page)
        if self.text_edit_1.total_pages > 1:
            # Show navigation controls for single page pagination
            self.prev_page_btn.show()
            self.next_page_btn.show()
            self.page_info_label.show()
            
            # Start with page 1
            self.current_left_page = 1
            self.update_single_page_display()
        else:
            # Only one page, show full content and hide navigation
            self.prev_page_btn.hide()
            self.next_page_btn.hide()
            self.page_info_label.hide()
            
            # Show full content with line numbers if enabled
            content = self.text_edit_1.original_content
            if self.text_edit_1.show_line_numbers:
                lines = content.split('\n')
                numbered_lines = []
                width = len(str(len(lines)))
                for i, line in enumerate(lines, 1):
                    line_num = str(i).rjust(width)
                    numbered_lines.append(f"{line_num}: {line}")
                content = '\n'.join(numbered_lines)
            self.text_edit_1.setPlainText(content)
    
    def setup_two_page_display(self):
        """Set up the two-page display with proper pagination"""
        if not self.current_file:
            return
            
        # Load content into both editors for pagination calculation
        self.text_edit_2.original_content = self.text_edit_1.original_content
        # Sync word wrap settings
        self.text_edit_2.word_wrap_enabled = self.text_edit_1.word_wrap_enabled
        self.text_edit_2.setLineWrapMode(self.text_edit_1.lineWrapMode())
        self.text_edit_2.calculate_pagination()
        
        # Start with pages 1 and 2
        self.current_left_page = 1
        self.update_page_display()
    
    def update_single_page_display(self):
        """Update display for single page mode"""
        if self.two_page_mode:
            return
        
        page_number = self.current_left_page
        total_pages = max(self.text_edit_1.total_pages, 1)
        
        # Set content for current page
        self.text_edit_1.set_page_content(page_number)
        
        # Update page info
        self.page_info_label.setText(f"Page {page_number} of {total_pages}")
        
        # Enable/disable navigation buttons
        self.prev_page_btn.setEnabled(page_number > 1)
        self.next_page_btn.setEnabled(page_number < total_pages)
    
    def update_page_display(self):
        """Update the display for current left and right pages"""
        if not self.two_page_mode:
            self.update_single_page_display()
            return
            
        left_page = self.current_left_page
        right_page = self.current_left_page + 1
        total_pages = max(self.text_edit_1.total_pages, 1)
        
        # Ensure we don't go beyond the last page
        left_page = min(left_page, total_pages)
        self.current_left_page = left_page
        
        # Set content for left page
        self.text_edit_1.set_page_content(left_page)
        
        # Set content for right page only if it exists
        if right_page <= total_pages:
            self.text_edit_2.set_page_content(right_page)
        else:
            # Clear right page if beyond document end
            self.text_edit_2.setPlainText("")
        
        # Update page info
        mode_text = "Sliding" if self.sliding_window_mode else "Spread"
        if right_page <= total_pages:
            self.page_info_label.setText(f"Pages {left_page}-{right_page} of {total_pages} ({mode_text})")
        else:
            self.page_info_label.setText(f"Page {left_page} of {total_pages} ({mode_text})")
        
        # Enable/disable navigation buttons
        self.prev_page_btn.setEnabled(left_page > 1)
        if self.sliding_window_mode:
            # In sliding mode, we can go next as long as we're not at the last page
            self.next_page_btn.setEnabled(left_page < total_pages)
        else:
            # In spread mode, we can go next as long as there are at least 2 more pages
            self.next_page_btn.setEnabled(left_page + 1 < total_pages)
    
    def previous_pages(self):
        """Go to previous page(s)"""
        if self.current_left_page > 1:
            if self.two_page_mode:
                if self.sliding_window_mode:
                    # Sliding window: move back by 1 page (1-2 -> 2-3 becomes 1-2)
                    self.current_left_page = max(1, self.current_left_page - 1)
                else:
                    # Spread view: move back by 2 pages (3-4 -> 1-2)
                    self.current_left_page = max(1, self.current_left_page - 2)
            else:
                # Single page mode: move back by 1 page
                self.current_left_page = max(1, self.current_left_page - 1)
            self.update_page_display()
    
    def next_pages(self):
        """Go to next page(s)"""
        total_pages = max(self.text_edit_1.total_pages, 1)
        if self.current_left_page < total_pages:
            if self.two_page_mode:
                if self.sliding_window_mode:
                    # Sliding window: move forward by 1 page (1-2 -> 2-3)
                    self.current_left_page = min(total_pages, self.current_left_page + 1)
                else:
                    # Spread view: move forward by 2 pages (1-2 -> 3-4)
                    self.current_left_page = min(total_pages, self.current_left_page + 2)
            else:
                # Single page mode: move forward by 1 page
                self.current_left_page = min(total_pages, self.current_left_page + 1)
            self.update_page_display()
    
    def zoom_in(self):
        """Zoom in on text"""
        self.text_edit_1.zoom_in()
        if self.two_page_mode:
            self.text_edit_2.zoom_in()
            # Recalculate pagination after zoom change
            self.update_page_display()
    
    def zoom_out(self):
        """Zoom out on text"""
        self.text_edit_1.zoom_out()
        if self.two_page_mode:
            self.text_edit_2.zoom_out()
            # Recalculate pagination after zoom change
            self.update_page_display()
    
    def reset_zoom(self):
        """Reset zoom to default"""
        self.text_edit_1.reset_zoom()
        if self.two_page_mode:
            self.text_edit_2.reset_zoom()
            # Recalculate pagination after zoom change
            self.update_page_display()
    
    def find_text(self):
        """Open find dialog"""
        dialog = FindDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            search_term = dialog.text()
            if search_term:
                cursor = self.text_edit_1.textCursor()
                cursor.movePosition(QTextCursor.Start)
                
                if cursor.find(search_term):
                    self.text_edit_1.setTextCursor(cursor)
                    self.status_bar.showMessage(f"Found: {search_term}", 2000)
                else:
                    self.status_bar.showMessage("No matches found.", 2000)
    
    def find_next(self):
        """Find next occurrence (placeholder)"""
        pass
    
    def find_previous(self):
        """Find previous occurrence (placeholder)"""
        pass
    
    def update_cursor_position(self):
        """Update cursor position in status bar"""
        cursor = self.text_edit_1.textCursor()
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber() + 1
        self.line_col_label.setText(f"Line: {line}, Col: {col}")
    
    def open_user_guide(self):
        """Open the user guide in the default web browser"""
        # GitHub URL for the help documentation
        github_help_url = "https://github.com/juren53/guiless/blob/main/Docs/HELP.md"
        
        try:
            webbrowser.open(github_help_url)
            self.status_bar.showMessage("Opening User Guide in web browser...", 3000)
        except Exception as e:
            QMessageBox.warning(
                self, "Error Opening User Guide",
                f"Could not open the User Guide in your web browser.\n\n"
                f"Please visit the following URL manually:\n"
                f"{github_help_url}\n\n"
                f"Error: {str(e)}"
            )
    
    def change_theme(self):
        """Open theme selection dialog"""
        dialog = ThemeDialog(self.current_theme, self.theme_manager, self)
        if dialog.exec_() == QDialog.Accepted:
            new_theme = dialog.get_selected_theme()
            if new_theme != self.current_theme:
                self.current_theme = new_theme
                self.apply_theme(new_theme)
                self.save_config()
                self.status_bar.showMessage(f"Theme changed to {new_theme}", 2000)
    
    def apply_theme(self, theme_name):
        """Apply the specified theme to the application"""
        stylesheet = self.theme_manager.generate_stylesheet(theme_name)
        self.setStyleSheet(stylesheet)
        
        # Update window title to reflect current theme if different from default
        if theme_name != 'Default':
            current_title = self.windowTitle()
            if ' - Theme: ' not in current_title:
                self.setWindowTitle(f"{current_title} - Theme: {theme_name}")
            else:
                # Replace existing theme name
                base_title = current_title.split(' - Theme: ')[0]
                self.setWindowTitle(f"{base_title} - Theme: {theme_name}")
        else:
            # Remove theme name from title for default theme
            current_title = self.windowTitle()
            if ' - Theme: ' in current_title:
                base_title = current_title.split(' - Theme: ')[0]
                self.setWindowTitle(base_title)
    
    def update_navigation_mode_ui(self):
        """Update UI elements based on current navigation mode"""
        self.sliding_window_action.setChecked(self.sliding_window_mode)
        self.spread_view_action.setChecked(not self.sliding_window_mode)
        self.update_navigation_button_text()
    
    def update_navigation_button_text(self):
        """Update navigation button text based on current mode"""
        if not self.two_page_mode:
            # Single page mode always uses simple page navigation
            self.prev_page_btn.setText("Previous Page")
            self.next_page_btn.setText("Next Page")
        elif self.sliding_window_mode:
            self.prev_page_btn.setText("Previous Page")
            self.next_page_btn.setText("Next Page")
        else:
            self.prev_page_btn.setText("Previous Spread")
            self.next_page_btn.setText("Next Spread")
    
    def show_about(self):
        """Show about dialog"""
        QMessageBox.about(
            self, "About GUI Less",
            "GUI Less v1.2.6\n\n"
            "A GUI version of the less utility built with PyQt5.\n\n"
            "Features:\n"
            "• Two-page mode as default for enhanced reading\n"
            "• Last directory memory for convenient navigation\n"
            "• File viewing with syntax similar to less\n"
            "• Zoom controls (Ctrl+/-, Ctrl+0 to reset)\n"
            "• Page navigation (Space/b for next/previous)\n"
            "• Optional line numbering\n"
            "• Toggleable word wrap for long lines\n"
            "• Recent files menu with auto-load\n"
            "• Fullscreen mode by default\n"
            "• Keyboard shortcuts compatible with less\n"
            "• Multiple UI themes for personalization\n"
            "• Two navigation modes: Sliding Window and Spread View"
        )
    
    def set_sliding_window_mode(self):
        """Set navigation to sliding window mode (1-2, 2-3, 3-4...)"""
        self.sliding_window_mode = True
        self.sliding_window_action.setChecked(True)
        self.spread_view_action.setChecked(False)
        
        # Update button text
        self.prev_page_btn.setText("Previous Page")
        self.next_page_btn.setText("Next Page")
        
        # Save configuration
        self.save_config()
        
        # Update display if in two-page mode
        if self.two_page_mode:
            self.update_page_display()
        
        self.status_bar.showMessage("Navigation mode: Sliding Window (1-2, 2-3, 3-4...)", 3000)
    
    def set_spread_view_mode(self):
        """Set navigation to spread view mode (1-2, 3-4, 5-6...)"""
        self.sliding_window_mode = False
        self.sliding_window_action.setChecked(False)
        self.spread_view_action.setChecked(True)
        
        # Update button text
        self.prev_page_btn.setText("Previous Spread")
        self.next_page_btn.setText("Next Spread")
        
        # Save configuration
        self.save_config()
        
        # Update display if in two-page mode
        if self.two_page_mode:
            self.update_page_display()
        
        self.status_bar.showMessage("Navigation mode: Spread View (1-2, 3-4, 5-6...)", 3000)

def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    
    window = GuiLess()
    window.show()
    
    # Handle command line arguments
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if os.path.exists(file_path):
            # Load the file specified on command line
            if window.text_edit_1.load_file(file_path):
                window.current_file = file_path
                window.setWindowTitle(f"GUI Less - {os.path.basename(file_path)}")
                window.add_recent_file(file_path)
                
                # If in two-page mode, set up pagination
                if window.two_page_mode:
                    window.setup_two_page_display()
        else:
            print(f"Error: File '{file_path}' not found.")
            sys.exit(1)
    else:
        # No command line argument, try to load most recent file
        window.load_most_recent_file()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

