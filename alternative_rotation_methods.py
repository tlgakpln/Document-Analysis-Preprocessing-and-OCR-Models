import cv2
import numpy as np
from paddleocr import PaddleOCR
import pytesseract
from pytesseract import Output
from imutils import rotate_bound
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

ocr = PaddleOCR(lang='en')


def rotated_with_paddle_image(image):

    max_rotation_attempts = 4  # En fazla 4 döndürme denemesi (her biri 90 derece)

    most_text_count = 0
    best_rotation_angle = 0

    for _ in range(max_rotation_attempts):
        results = ocr.ocr(image)

        text_count = sum([len(result) for result in results])
        print("text count:", text_count)

        if text_count > most_text_count:
            most_text_count = text_count
            best_rotation_angle = _ * 90

        image = np.rot90(image, 1)  # 90 derece döndür
        # cv2.imshow("Rotated Image", image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    print("Max text count:", most_text_count)
    print("Best rotation angle:", best_rotation_angle)

    rotated_image = np.rot90(image, best_rotation_angle // 90)
    return rotated_image


def rotate_image_to_text_angle_tesseract(image, tesseract=True, angle=None):
    if tesseract:
        osd = pytesseract.image_to_osd(image, lang='eng', output_type=Output.DICT, config='--oem 3')

        rotation_angle = osd['rotate']

    else:
        rotation_angle = angle

    rotated_image = rotate_bound(image, rotation_angle)

    return rotated_image




