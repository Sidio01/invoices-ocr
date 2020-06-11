import pytesseract
import cv2
import numpy as np
import matplotlib.pyplot as plt

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

img = cv2.imread('schet.png')

# Adding custom options
custom_config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(img, config=custom_config, lang='rus'))


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


a = get_grayscale(img)
plt.imshow(a, cmap='Greys')
plt.show()
plt.imshow(img, cmap='Greys')
plt.show()
