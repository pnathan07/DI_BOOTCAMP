import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import requests
from io import BytesIO

def show_images(original, augmented, title):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(augmented)
    plt.title(title)
    plt.axis('off')

    plt.show()

# Load an example image from the Flower Color Images dataset
image_url = 'https://example.com/flower.jpg'  # Replace with actual URL or path
response = requests.get(image_url)
original_image = Image.open(BytesIO(response.content))

# Display the original image
plt.imshow(original_image)
plt.title('Original Image')
plt.axis('off')
plt.show()

# Rotate the image by 90 degrees
rotated_image = original_image.rotate(90, expand=True)
show_images(original_image, rotated_image, 'Rotated Image (90 Degrees)')

# Flip the image horizontally
flipped_horizontally = ImageOps.mirror(original_image)
show_images(original_image, flipped_horizontally, 'Horizontally Flipped Image')

# Flip the image vertically
flipped_vertically = ImageOps.flip(original_image)
show_images(original_image, flipped_vertically, 'Vertically Flipped Image')

# Zoom in on the image (scale by 1.2x)
width, height = original_image.size
zoomed_image = original_image.resize((int(width * 1.2), int(height * 1.2)))
show_images(original_image, zoomed_image, 'Zoomed Image (1.2x)')
