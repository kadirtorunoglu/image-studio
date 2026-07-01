from PIL import Image

def rotate_image(input_path, output_path, angle):
    with Image.open(input_path) as image:
        rotated_image = image.rotate(angle, expand=True)
        rotated_image.save(output_path)
        rotated_image.show()
        
def resize_image(image_path, output_path, size):

    img = Image.open(image_path)
    
    resized_image = img.resize(size)
    resized_image.save(output_path)


    resized_image.show()

def grayscale(image):
    return image.convert("L")

