from PIL import Image

def grayscale(image):
    return image.convert("L")