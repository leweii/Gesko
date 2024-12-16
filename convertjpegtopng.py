import os
from PIL import Image

def compress_and_convert_images(input_folder):
    """
    Recursively traverse a folder, find all JPEG files, compress them to reduce size
    without significant loss in visual quality. Overwrite the JPEG if compression is effective.

    :param input_folder: Path to the root folder to process.
    """
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg')):
                jpeg_path = os.path.join(root, file)

                try:
                    # Open the JPEG image
                    with Image.open(jpeg_path) as img:
                        # Save the image as a compressed JPEG in memory to calculate size
                        from io import BytesIO
                        buffer = BytesIO()
                        img.save(buffer, format="JPEG", optimize=True, quality=85)
                        compressed_size = buffer.tell()

                        # Compare sizes
                        original_size = os.path.getsize(jpeg_path)
                        if compressed_size < original_size:
                            # Overwrite the JPEG file with the compressed version
                            with open(jpeg_path, "wb") as f:
                                f.write(buffer.getvalue())
                            print(f"Compressed and saved: {jpeg_path} ({original_size} -> {compressed_size} bytes)")
                        else:
                            print(f"Skipped (larger size): {jpeg_path}")

                except Exception as e:
                    print(f"Failed to process {jpeg_path}: {e}")

if __name__ == "__main__":
    input_folder = input("Enter the input folder path: ").strip()
    if os.path.isdir(input_folder):
        compress_and_convert_images(input_folder)
    else:
        print("Invalid folder path. Please try again.")
