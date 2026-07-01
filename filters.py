from PIL import ImageFilter
def blur(image):
    """
    Apply a blur filter to the given image.

     Parameters:
        image: PIL Image object

    Returns:
        Blurred PIL Image object
    """
    return image.filter(ImageFilter.BLUR)
