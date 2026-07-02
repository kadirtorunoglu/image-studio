from PIL import ImageFilter
from PIL import Image
from PIL import ImageEnhance
def grayscale(image):
    return image.convert("L")
def rotate_image(input_path, output_path, angle):
    with Image.open(input_path) as image:
        rotated_image = image.rotate(angle, expand=True)
        rotated_image.save(output_path)
        
        
def resize_image(image_path, output_path, size):

    
    img = Image.open(image_path)
    resized_image = img.resize(size)
    resized_image.save(output_path)


    
  
def blur(image):
    """
    Apply a blur filter to the given image.

     Parameters:
        image: PIL Image object

    Returns:
        Blurred PIL Image object
    """
    return image.filter(ImageFilter.GaussianBlur(radius=8))

  
def adjust_brightness(image,output,factor):
   

    enhancer = ImageEnhance.Brightness(image)

    brightened_image = enhancer.enhance(factor)
    brightened_image.save(output)
    return brightened_image
