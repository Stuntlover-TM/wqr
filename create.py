from PIL import Image
import math

dynamic = True
input_string = open("input.txt", "r").read()

if dynamic:
    width, height = math.ceil(math.sqrt(len(input_string) * 8)), math.ceil(math.sqrt(len(input_string) * 8))
else:
    width, height = 32, 32
image = Image.new('RGB', (width, height), (255, 255, 255))

if len(input_string) > (width*height) // 8 and not dynamic:
    print(f"Input size exceeded limit, reduce by {len(input_string) - (width*height) // 8}")
    exit()

bytes_list = []

for char in input_string:
    bytes_list.append(str(bin(ord(char)))[2:].rjust(8, "0"))

black = (0, 0, 0)
white = (255, 255, 255)

x, y = 0, 0

for bit_string in bytes_list:
    for bit in bit_string:
        if bit == "0":
            pixel_value = black
        else:
            pixel_value = white

        image.putpixel((x, y), pixel_value)
        x += 1
        if x == width:
            y += 1
            x = 0
        if y == height:
            y = 0
            x = 0

image.save("wqr.png")
