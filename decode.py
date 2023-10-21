from PIL import Image

image = Image.open("wqr.png")
image = image.convert("1")

width, height = image.size

bytes_list = []
bit_string = ""
break_out = False

for y in range(height):
    if break_out:
        break
    for x in range(width):
        pixel = image.getpixel((x, y))
        if pixel == 0:
            bit = 0
        else:
            bit = 1

        bit_string += str(bit)

        if len(bit_string) == 8:
            if bit_string != "11111111":
                bytes_list.append(bit_string)
            else:
                break_out = True
                break
            bit_string = ""

if bit_string:
    if bit_string != "11111111" and len(bit_string) == 8:
        bytes_list.append(bit_string)

result = ""

for wqr_byte in bytes_list:
    result += chr(int(wqr_byte, 2))

print(result)
