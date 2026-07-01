from PIL import Image

def resize_image(image_path, output_path, size):

    img = Image.open(image_path)
    
    resized_image = img.resize(size)
    resized_image.save(output_path)


    resized_image.show()