# Weird QR
Some weird "QR" image thing
(You need to have Pillow installed before running this)

## Usage

### Encoding
(WQR can encode and decode all UTF-8 characters.)

Make a file called input.txt and put some text that you want to make into a WQR image, then run the `encode.py` file, it should create a file called `wqr.png`,
which should be very small in size

### Dynamic Mode

By default, Dynamic Mode is on, which means it will scale your image as your input string gets larger automatically, you can turn this off (not recommended)
by turning `dynamic = True` to `dynamic = False` and changing the width and height variables (from 32, 32) manually.

### Decoding
To decode a WQR image, simply run `decode.py`, it should output the original text in the console.


### Example image
![Example WQR image](https://raw.githubusercontent.com/Stuntlover-TM/wqr/main/example-21x21-upscaled.png)
