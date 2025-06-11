#!/bin/bash
# Launcher script for GUI Less application

# Check if PyQt5 is installed
if ! python3 -c "import PyQt5" 2>/dev/null; then
    echo "Error: PyQt5 is not installed."
    echo "Please install it with: pip install PyQt5"
    exit 1
fi

# Get the directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Run the application with any provided arguments
python3 "$DIR/guiless.py" "$@"

