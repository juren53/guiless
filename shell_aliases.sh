#!/bin/bash
# GUI Less Shell Aliases
# Source this file or add to your ~/.bashrc or ~/.zshrc

# Navigation aliases
alias guiless='cd /home/juren/Projects/guiless'
alias guiless-current='cd /home/juren/Projects/guiless'
alias guiless-old='cd /home/juren/Projects/guiless-old-prototype'

# Application aliases
alias guiless-run='cd /home/juren/Projects/guiless && python guiless.py'
alias guiless-sample='cd /home/juren/Projects/guiless && python guiless.py sample.txt'

# Development aliases
alias guiless-status='cd /home/juren/Projects/guiless && pwd && git status'
alias guiless-log='cd /home/juren/Projects/guiless && git log --oneline --graph --decorate -10'
alias guiless-test='cd /home/juren/Projects/guiless && python -c "from guiless import GuiLess; print(\"✅ Import successful\")"; '

# Safety check aliases
alias guiless-check='cd /home/juren/Projects/guiless && pwd && ls -la *.py && echo "✅ In correct directory if you see guiless.py"'
alias guiless-verify='pwd | grep -q "guiless$" && echo "✅ In current project" || echo "⚠️  Not in current project directory"'

# Information aliases
alias guiless-info='echo "Current Project: /home/juren/Projects/guiless"; echo "Legacy Project: /home/juren/Projects/guiless-old-prototype (deprecated)"; echo "Use: guiless-check to verify location"'

echo "GUI Less aliases loaded!"
echo "Available commands:"
echo "  guiless          - Navigate to current project"
echo "  guiless-run      - Run the application"
echo "  guiless-sample   - Run with sample file"
echo "  guiless-check    - Verify you're in correct directory"
echo "  guiless-info     - Show project information"

