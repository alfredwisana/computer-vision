from PIL import Image

imageName = 'turtle.jpg'  # input image name
image = Image.open(imageName)

image = image.convert('RGB')

# Print the width and height of the image
width, height = image.size
print("Image width:", width)
print("Image height:", height)

# Display original pixel values in matrix
for y in range(height):
    for x in range(width):
        pixel_value = image.getpixel((x, y))
        # For RGB images, pixel_value will be a tuple (R, G, B) (0, 1, 2)
        # print(f"Pixel at ({x}, {y}): R={pixel_value[0]}, G={pixel_value[1]}, B={pixel_value[2]}")

# Warnanya diubah menjadi negatif/kebalikan
reverted_image = image.copy()
for y in range(height):
    for x in range(width):
        current_pixel_value = image.getpixel((x, y))
        new_pixel_value = tuple(255 - value for value in current_pixel_value)
        
        reverted_image.putpixel((x, y), new_pixel_value)  # Update pixel value in the image
# reverted_image.show()


# Mengubah gambar berwarna menjadi hitam putih
monochrome_image = Image.new('L', (width, height))

# Iterate through each pixel in the image
for y in range(height):
    for x in range(width):
        # Get the pixel value at the current position
        r, g, b = image.getpixel((x, y))
        
        # Convert RGB to grayscale using luminosity method
        gray_value = int(0.21 * r + 0.72 * g + 0.07 * b)
        
        # Set the pixel value in the new image
        monochrome_image.putpixel((x, y), gray_value)

# monochrome_image.show()