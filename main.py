from PIL import Image
from filters import grayscale
from filters import resize_image
from filters import rotate_image
from filters import blur
from utils import image_info

img = Image.open("images/image.jpg")

gray = grayscale(img)

gray.save("output/grayscale.jpg")

resize_image("output/grayscale.jpg", "output/resized_test.jpg", (800, 600))


rotate_image(
    input_path="output/resized_test.jpg",
    output_path="output/gibbon_rotated.jpg",
    angle=180
)

# Load the image
image = Image.open("output/gibbon_rotated.jpg")

# Apply the blur filter
blurred_image = blur(image)

# Save the blurred image
blurred_image.save("output/blurred_photo.png")


blurred_image.show()

image_info("images/image.jpg")

print("Done!")