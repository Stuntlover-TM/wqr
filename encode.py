from PIL import Image
import math
import numpy as np
import time

start = time.time()

dynamic = True
input_string = open("input.txt", "r").read()

black = (0, 0, 0)
white = (255, 255, 255)

if dynamic:
    size = math.ceil(math.sqrt(len(input_string) * 8))
else:
    size = 32
image = Image.new('RGB', (size, size), white)

pixels = np.full((size, size, 3), white, dtype=np.uint8)

x, y = 0, 0

for char in input_string:
    binary_char = format(ord(char), '08b')
    for bit in binary_char:
        if bit == '0':
            pixels[y, x] = black
        x += 1
        if x == size:
            y += 1
            x = 0

image = Image.fromarray(pixels)

image.save("wqr.png")

time_taken = time.time() - start
print(time_taken)
