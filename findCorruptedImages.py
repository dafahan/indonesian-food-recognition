from PIL import Image
import os

def check_images_in_directory(directory):
    """Check all image files in the given directory for potential corruption."""
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                # Attempt to open the image file
                with Image.open(filepath) as img:
                    # If successful, the file is not corrupted
                    print(f"{filename}: OK")
            except Exception as e:
                # If an error occurs, the file may be corrupted
                print(f"{filename}: Error - {e}")

# Directories containing the images
directories = [
    '/home/dafahan/Downloads/makanan/train',
    '/home/dafahan/Downloads/makanan/validation',
    '/home/dafahan/Downloads/makanan/test'
]

# Check images in each directory
for directory in directories:
    print(f"Checking images in {directory}:")
    check_images_in_directory(directory)
    print("\n")
