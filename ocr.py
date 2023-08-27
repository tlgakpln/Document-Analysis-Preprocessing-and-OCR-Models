import pytesseract
from paddleocr import PaddleOCR
import easyocr
import os
import cv2
import scanner

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def extract_text_easyocr_opencv(image):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image)

    extracted_text = ""
    for detection in result:
        text = detection[1]
        extracted_text += text + " "

    return extracted_text.strip()


def extract_text_pytesseract_opencv(image):
    extracted_text = pytesseract.image_to_string(image, lang='eng')
    return extracted_text


def extract_text_paddleocr_opencv(image):
    text = []
    try:
        ocr = PaddleOCR(lang='en')
        result = ocr.ocr(image)
        for line in result:
            words = ' '.join([word[1][0] for word in line])
            text.append(words)
        return text
    except:
        text = None
        return text


def select_ocr(img_path, model):
    image = cv2.imread(img_path)
    image = scanner.find_cropped_image(image)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if model == 'tesseract':
        return extract_text_pytesseract_opencv(image)
    if model == 'paddle':
        return extract_text_paddleocr_opencv(image)
    else:
        return extract_text_easyocr_opencv(image)


if __name__ == "__main__":
    images_path = 'images'
    for filename in os.listdir(images_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join("images", filename)
            text = select_ocr(img_path=image_path, model='paddle')
            print(text)
