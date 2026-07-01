from PIL import Image

def rotate_image(input_path, output_path, angle):
    with Image.open(input_path) as image:
        rotated_image = image.rotate(angle, expand=True)
        rotated_image.save(output_path)
        rotated_image.show()