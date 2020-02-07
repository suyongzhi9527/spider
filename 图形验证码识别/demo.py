import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'

img = Image.open('1.jpg')

img_str = pytesseract.image_to_string(img)
print(img_str)
