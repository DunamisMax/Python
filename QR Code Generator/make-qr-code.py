from qrcodegen import QrCode
from PIL import Image, ImageDraw

# Define a function to generate a Pillow image from the QR code
def to_image(qr: QrCode, border: int) -> Image:
    """Creates and returns a Pillow Image of the given QR Code, with the given number of border modules."""
    if border < 0:
        raise ValueError("Border must be non-negative")
    
    size = qr.get_size()
    scale = 50  # Each QR module will be scaled up by 25 pixels for better visibility
    img_size = (size + border * 2) * scale
    img = Image.new('RGB', (img_size, img_size), "white")
    draw = ImageDraw.Draw(img)

    # Draw the QR code
    for y in range(size):
        for x in range(size):
            if qr.get_module(x, y):  # Is the module black?
                draw.rectangle(
                    [(x + border) * scale, (y + border) * scale, 
                     (x + border + 1) * scale - 1, (y + border + 1) * scale - 1],
                    fill="black")
    
    return img

# Function to print the QR code in the console
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
}.get(error_correction_input, QrCode.Ecc.HIGH)  # Default to HIGH if input is invalid

# Prompt the user for the desired border size
border_size = int(input("Enter the border size (default 2): ") or 2)

# Prompt the user for the filename and the text to encode
file_name = input("Enter the desired filename (without extension) to save the QR Code: ") + ".jpg"
text_to_encode = input("Enter the text/data you want to encode into the QR Code: ")

# Automatically choose the smallest QR code version that fits the input data
qr = QrCode.encode_text(text_to_encode, error_correction)

# Print the QR code to the console for quick verification
print("Here is the QR code printed in the console:")
print_qr(qr)

# Generate the image and save it as JPEG
img = to_image(qr, border_size)
img.save(file_name, "JPEG")

print(f"QR code generated and saved as '{file_name}'.")