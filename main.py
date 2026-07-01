from PIL import Image
from filters import grayscale

img = Image.open("images/image.jpg")

gray = grayscale(img)

gray.save("output/grayscale.jpg")

print("Done!")