import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'

img = Image.open('CheckCode.jfif')
img = img.convert('L')
thres = 140
table = []
for i in range(256):
    if i < thres:
        table.append(0)
    else:
        table.append(1)
img = img.point(table, '1')
img.show()
img_str = pytesseract.image_to_string(img)
print(img_str)
