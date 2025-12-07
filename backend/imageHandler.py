import os
from PIL import Image

class ImageHandler:
    def __init__(self):
        self.image = None;
        self.image_path = None;

    def set_image(self, path=None):
        if path is None:
            path = input("Select your image file: ").strip()

        if not os.path.exists(path):
            print("File not found.")
            return False

        try:
            img = Image.open(path)
            self.image = img
            self.image_path = path
            print("Image loaded scessfully.")
            return True
        except Exception as e:
            print(f"Error loading image: {e}")
            return False

    def get_image(self):
        if self.image is None:
            print("No image loaded")
            return None
        return self.image

    def get_image_path(self):
        return self.image_path

