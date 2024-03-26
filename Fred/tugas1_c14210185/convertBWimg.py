# Jika ingin melihat hasil gambar, function show diuncomment
from PIL import Image

# Open the image
imageName = 'black_and_white_image.bmp' #input image name
image = Image.open(imageName)

# Convert the image to grayscale
image = image.convert('L')

# Print the width and height of the image
width, height = image.size
print("Image width:", width)
print("Image height:", height)

# Display original pixel values in matrix
for y in range(height):
    for x in range(width):
        pixel_value = image.getpixel((x, y))
        # print(pixel_value, end=" ")
    # print()
# print()

# Print the pixel value at a specific coordinate (start from 0)
x_coordinate = 26  # input x
y_coordinate = 0   # input y
if 0 <= x_coordinate < width and 0 <= y_coordinate < height:
    pixel_value = image.getpixel((x_coordinate, y_coordinate))
    print("Pixel value at (", x_coordinate, ",", y_coordinate, "):", pixel_value)
else:
    print("Di luar boundaries")


# Modify pixel values to negative
reverted_image = Image.open(imageName)
for y in range(height):
    for x in range(width):
        current_pixel_value = reverted_image.getpixel((x, y))
        new_pixel_value = 255 - current_pixel_value  # Calculate negative value
        reverted_image.putpixel((x, y), new_pixel_value) # Update pixel value in the image
# reverted_image.show()


# Crop the image berdasarkan koordinat
cropped_image = image.crop((50, 50, 100, 100))
# cropped_image.show()


# Gambar dibalik secara horizontal
horizontally_flipped = Image.open(imageName)
for y in range(height): # Jika vertikal maka -1, -1, -1 dipindah ke height
    for x in range(width - 1, -1, -1):  # Dimulai dari kolom terakhir dan bergerak ke kiri
        pixel_value = image.getpixel((x, y))
        horizontally_flipped.putpixel(((width - 1) - x, y), pixel_value)
# horizontally_flipped.show()


# Rotate 90 derajat searah jarum jam
width, height = image.size  # Get the dimensions of the image
# Create a new image with swapped width and height for rotation
rotated_image_vertical = Image.new('L', (height, width))
rotated_image_horizontal = Image.open(imageName)
for y in range(height):
    for x in range(width):
        pixel_value = image.getpixel((x, y))
        # 90 derajat
        # rotated_image_vertical.putpixel((height - 1 - y, x), pixel_value)
        # horizontal = False
        
        # 180 derajat
        rotated_image_horizontal.putpixel((width - 1 - x, height - 1 - y), pixel_value)
        horizontal = True
        
        # 270 derajat
        # rotated_image_vertical.putpixel((y, width - 1 - x), pixel_value)
        # horizontal = False
        
# if horizontal:
#     rotated_image_horizontal.show()
# else:
#     rotated_image_vertical.show()


# Perbesar sekian kali lipat
mul = 2  # masukkan kelipatannya (hanya bisa integer)
new_width = width*mul
new_height = height*mul
bigger_image = Image.new('L', (new_width, new_height))

for y in range(height):
    for x in range(width):
        # Get the pixel value from the original image
        pixel_value = image.getpixel((x, y))
        # Put the pixel value at the corresponding position in the bigger image
        bigger_image.putpixel((mul*x, mul*y), pixel_value)
        bigger_image.putpixel((mul*x + 1, mul*y), pixel_value)
        bigger_image.putpixel((mul*x, mul*y + 1), pixel_value)
        bigger_image.putpixel((mul*x + 1, mul*y + 1), pixel_value)

# bigger_image.show()


#kalau semua pixel mines 128 jadi gelap, kalau tambah jadi terang
color_changed_image = Image.open(imageName)
for y in range(height):
    for x in range(width):
        current_pixel_value = color_changed_image.getpixel((x, y))
        new_pixel_value = int(current_pixel_value + 128) # angka dan operatornya bisa diganti
        if new_pixel_value < 0:
            new_pixel_value = 0
        elif new_pixel_value > 255:
            new_pixel_value = 255
        color_changed_image.putpixel((x, y), new_pixel_value) # Update pixel value in the image
        
# color_changed_image.show()


# Image blurring
blurred_image = Image.open(imageName)
width, height = blurred_image.size
for y in range(1, height - 1):
    for x in range(1, width - 1):
        pixel_sum = sum(image.getpixel((x + i, y + j)) for i in range(-1, 2) for j in range(-1, 2))
        blurred_value = int(pixel_sum / 9)  # 3x3 averaging filter
        blurred_image.putpixel((x, y), blurred_value)
        
blurred_image.show()
