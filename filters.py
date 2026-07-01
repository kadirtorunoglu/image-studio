from PIL import  ImageFilter
def blur(image):
    """
    Apply a blur filter to the given image.

    """
    return image.filter(ImageFilter.BLUR)
