from PIL import ImageFilter
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw
from PIL import ImageFont

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



def flip_horizontal(image):
    """
    Flip image horizontally.
    """
    return image.transpose(Image.FLIP_LEFT_RIGHT)

def add_text_watermark(
    input_path,
    output_path,
    text,
    position=(20, 20),
    font_size=40
):
    with Image.open(input_path).convert("RGBA") as image:
        watermark_layer = Image.new(
            "RGBA",
            image.size,
            (255, 255, 255, 0)
        )

        draw = ImageDraw.Draw(watermark_layer)

        try:
            font = ImageFont.truetype(
                "/System/Library/Fonts/Helvetica.ttc",
                font_size
            )
        except OSError:
            font = ImageFont.load_default()

        draw.text(
            position,
            text,
            font=font,
            fill=(255, 255, 255, 150)
        )

        watermarked_image = Image.alpha_composite(
            image,
            watermark_layer
        )

        watermarked_image.convert("RGB").save(output_path)
