from PIL import Image
import math
import numpy as np

dynamic = False
input_string = open("input.txt", "r").read()

black = (0, 0, 0)
white = (255, 255, 255)

dynamic_func = math.ceil(math.sqrt(len(input_string) * 8))

if dynamic:
    size = (dynamic_func, dynamic_func)
else:
    size = (32, 32)
image = Image.new('RGB', (size[0], size[1]), white)

pixels = np.full((size[0], size[1], 3), white, dtype=np.uint8)

x, y = 0, 0

for char in input_string:
    binary_char = format(ord(char), '08b')
    for bit in binary_char:
        if bit == '0':
            pixels[y, x] = black
        x += 1
        if x == size[1]:
            y += 1
            x = 0

image = Image.fromarray(pixels)

image.save("wqr.png")
