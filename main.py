
from filters import rotate_image
from filters import resize_image
from PIL import Image
from filters import grayscale


resize_image("images/test.jpg", "output/resized_test.jpg", (800, 600))

img = Image.open("images/image.jpg")

gray = grayscale(img)

gray.save("output/grayscale.jpg")

rotate_image(
    input_path="images/gibbon.jpg",
    output_path="output/gibbon_rotated.jpg",
    angle=180
)

print("Done!")

