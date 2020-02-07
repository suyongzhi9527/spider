import pytesseract
from PIL import Image
from urllib import request
import time


def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'
    url = 'https://passport.qyer.com/qcross/passport/captcha?scene=mobile_register_sms&timer=1581064580150'
    while True:
        request.urlretrieve(url, 'captcha.png')
        img = Image.open('captcha.png')
        img_str = pytesseract.image_to_string(img)
        print(img_str)
        time.sleep(2)


if __name__ == '__main__':
    main()
