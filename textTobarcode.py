from pdf417 import encode, render_image, render_svg

# Some data to encode
text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""

# Convert to code words
codes = encode(text)

# Generate barcode as image
image = render_image(codes)  # Pillow Image object
image.save('barcode.jpg')

# Generate barcode as SVG
svg = render_svg(codes)  # ElementTree object
svg.write("barcode.svg")
