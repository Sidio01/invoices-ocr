# Warming up
# Let’s start writing our script. First of all, we will be importing the required libraries:
# Note: I imported Image from PIL as PI because
# otherwise it would have conflicted with the Image module from wand.image.

from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io

# Get Going
# Now we need to get the handle of the OCR library (in our case, tesseract)
# and the language which will be used by pyocr.
tool = pyocr.get_available_tools()[0]
lang = tool.get_available_languages()[1]
# We used the second language in the tool.get_available_languages() because the last time I checked, it was English.

# Now we need to setup two lists which will be used to hold our images and final_text.
req_image = []
final_text = []

# Next step is to open the PDF file using wand and convert it to jpeg. Let’s do it!
image_pdf = Image(filename="test_pdf.pdf", resolution=300)
image_jpeg = image_pdf.convert('jpeg')
# Note: Replace PDF_FILE_NAME with a valid PDF file name in the current path.
# wand has converted all the separate pages in the PDF into separate image blobs.
# We can loop over them and append them as a blob into the _reqimage list.

for img in image_jpeg.sequence:
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpeg'))

# Now we just need to run OCR over the image blobs. It is very easy.
for img in req_image:
    txt = tool.image_to_string(
        PI.open(io.BytesIO(img)),
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
    final_text.append(txt)

# Now all of the recognized text has been appended in the _finaltext list. You can use it in any way you want.
# I hope this tutorial was helpful for you guys!
# If you have any comments and suggestions then do let me know in the comments section below.
# Till next time! 🙂
