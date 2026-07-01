from PIL import Image
from filters import blur

# Load the image
image = Image.open("images/photo.png")

# Apply the blur filter
blurred_image = blur(image)

# Save the blurred image
blurred_image.save("output/blurred_photo.png")

print("Blur filter applied successfully!")

