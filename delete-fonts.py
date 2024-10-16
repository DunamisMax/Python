import os
import shutil
import ctypes
import sys
from pathlib import Path

# List of default fonts to keep (these are font family names)
default_fonts = {
    "arial", "calibri", "cambria", "comic sans ms", "courier new", 
    "georgia", "impact", "lucida console", "segoe ui", 
    "times new roman", "trebuchet ms", "verdana", 
    "webdings", "wingdings"
}

# Additional default system fonts that should be kept
additional_fonts_to_keep = {
    "segoe script", "segoe print", "symbol", "marlett"
}

# Combine all fonts to keep
default_fonts.update(additional_fonts_to_keep)

# Path to the Windows Fonts directory
fonts_dir = Path(r"C:\Windows\Fonts")

# Destination folder to copy fonts to (on the desktop)
destination_dir = Path(r"C:\Users\Sawyer\Desktop\fonts")

# Log file to keep track of copied fonts
log_file = Path("copied_fonts.log")

# Function to check if script is running as admin
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def copy_default_fonts():
    # Create the destination directory if it doesn't exist
    if not destination_dir.exists():
        destination_dir.mkdir(parents=True)
    
    # Open log file to write copied fonts
    with open(log_file, "w") as log:
        log.write("Copied Fonts:\n")
        log.write("=====================\n")

        # Iterate over each file in the Fonts directory
        for font_file in fonts_dir.iterdir():
            # Get the font file name without extension for comparison
            font_name = font_file.stem.lower()

            # Check if the font name matches any of the default fonts to keep
            if any(font_name.startswith(default_font) for default_font in default_fonts):
                try:
                    # Copy the font file to the destination directory
                    if font_file.is_file():
                        destination_path = destination_dir / font_file.name
                        shutil.copy2(font_file, destination_path)
                        log.write(f"Copied: {font_file.name}\n")
                    elif font_file.is_dir():
                        # This handles cases where a font might be in a directory
                        destination_path = destination_dir / font_file.name
                        shutil.copytree(font_file, destination_path)
                        log.write(f"Copied directory: {font_file.name}\n")
                except PermissionError:
                    log.write(f"Failed to copy: {font_file.name}. Access is denied.\n")
                except Exception as e:
                    log.write(f"Failed to copy: {font_file.name}. Reason: {e}\n")

if __name__ == "__main__":
    if is_admin():
        copy_default_fonts()
        print(f"Font copy complete. See {log_file} for details.")
    else:
        print("Script requires admin privileges to copy fonts.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)  # Re-run as admin