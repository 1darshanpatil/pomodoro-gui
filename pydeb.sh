#!/bin/bash

# Dependencies
sudo apt-get install sox

# Check if the script argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: ./package.sh <python_script_name>"
    exit 1
fi

PYTHON_SCRIPT=$1
PACKAGE_NAME=$(basename "$PYTHON_SCRIPT" .py)

# Organize the Python script
mkdir -p "$PACKAGE_NAME/usr/local/bin"
cp "$PYTHON_SCRIPT" "$PACKAGE_NAME/usr/local/bin/$PACKAGE_NAME"

# Make sure the script is executable
chmod +x "$PACKAGE_NAME/usr/local/bin/$PACKAGE_NAME"

# Add an icon for the Python GUI
mkdir -p "$PACKAGE_NAME/usr/share/icons/hicolor/512x512/apps"
cp background.png "$PACKAGE_NAME/usr/share/icons/hicolor/512x512/apps/background.png"


# Add an icon for the .desktop entry
mkdir -p "$PACKAGE_NAME/usr/share/pixmaps"
cp app.png "$PACKAGE_NAME/usr/share/icons/hicolor/512x512/apps/app.png"



# Create a .desktop file
mkdir -p "$PACKAGE_NAME/usr/share/applications"
cat <<EOL > "$PACKAGE_NAME/usr/share/applications/${PACKAGE_NAME}.desktop"
[Desktop Entry]
Version=1.0
Name=Pomodoro Timer
Exec=python3 /usr/local/bin/$PACKAGE_NAME
Icon=/usr/share/icons/hicolor/512x512/apps/app.png
Terminal=false
Type=Application
Categories=Utility;
EOL

# Create Debian directory and control file
mkdir -p "$PACKAGE_NAME/DEBIAN"

cat <<EOL > "$PACKAGE_NAME/DEBIAN/control"
Package: $PACKAGE_NAME
Version: 1.0
Section: base
Priority: optional
Architecture: all
Maintainer: Darwin <drshnp@outlook.com>
Description: Package created from $PYTHON_SCRIPT
EOL

# Build the Debian package
dpkg-deb --build "$PACKAGE_NAME"

# Optional: Cleanup
rm -r "$PACKAGE_NAME"

echo "Done! Your Debian package is named ${PACKAGE_NAME}.deb"

sudo dpkg -i pomodoro-gui.deb
sudo apt-get install -f
