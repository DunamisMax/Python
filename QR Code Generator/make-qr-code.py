from qrcodegen import QrCode

# Define a function to generate the SVG string from the QR code
def to_svg_str(qr: QrCode, border: int) -> str:
    """Returns a string of SVG code for an image depicting the given QR Code, with the given number of border modules."""
    if border < 0:
        raise ValueError("Border must be non-negative")
    
    parts = []
    size = qr.get_size()
    
    # Prepare the SVG elements
    parts.append(f'<?xml version="1.0" encoding="UTF-8"?>\n')
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 {size + border * 2} {size + border * 2}" stroke="none">\n')
    parts.append(f'\t<rect width="100%" height="100%" fill="#FFFFFF"/>\n')
    parts.append(f'\t<path d="')
    
    # Generate the QR code path
    for y in range(size):
        for x in range(size):
            if qr.get_module(x, y):  # is the module black?
                parts.append(f'M{x + border},{y + border}h1v1h-1z ')
    
    parts.append(f'" fill="#000000"/>\n')
    parts.append(f'</svg>\n')
    
    return ''.join(parts)

# Define a function to print a textual representation of the QR code in the console
def print_qr(qr: QrCode) -> None:
    """Prints the given QrCode object to the console."""
    border = 2  # You can adjust the border size for terminal display
    for y in range(-border, qr.get_size() + border):
        for x in range(-border, qr.get_size() + border):
            print("\u2588 "[1 if qr.get_module(x, y) else 0] * 2, end="")
        print()
    print()

# Prompt the user to choose the error correction level
error_correction_input = input("Choose error correction level (LOW, MEDIUM, QUARTILE, HIGH): ").upper()
error_correction = {
    "LOW": QrCode.Ecc.LOW,
    "MEDIUM": QrCode.Ecc.MEDIUM,
    "QUARTILE": QrCode.Ecc.QUARTILE,
    "HIGH": QrCode.Ecc.HIGH
}.get(error_correction_input, QrCode.Ecc.MEDIUM)  # Default to MEDIUM if input is invalid

# Prompt the user for the desired border size
border_size = int(input("Enter the border size (default 4): ") or 4)

# Prompt the user for the filename and the text to encode
file_name = input("Enter the desired filename (without extension) to save the QR Code: ") + ".svg"
text_to_encode = input("Enter the text/data you want to encode into the QR Code: ")

# Automatically choose the smallest QR code version that fits the input data
qr = QrCode.encode_text(text_to_encode, error_correction)

# Print the QR code to the console for quick verification
print("Here is the QR code printed in the console:")
print_qr(qr)

# Convert the QR code to an SVG string
svg = to_svg_str(qr, border_size)

# Write the SVG string to a file with the user-provided filename
with open(file_name, "w") as f:
    f.write(svg)

print(f"QR code generated and saved as '{file_name}'.")