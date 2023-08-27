import cv2
import numpy as np
from imutils.perspective import four_point_transform
import alternative_rotation_methods
import best_rotation_method
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def image_processing(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY)

    return threshold


def scan_detection(image):
    global document_contour

    document_contour = np.array([[0, 0], [1080, 0], [1080, 720], [0, 720]])

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, threshold = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 850:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.015 * peri, True)
            if area > max_area and len(approx) == 4:
                document_contour = approx
                max_area = area

    cv2.drawContours(image, [document_contour], -1, (0, 255, 0), 3)
    return image


def add_background(image, border_size):
    image_height, image_width = image.shape[:2]

    new_width = image_width + border_size
    new_height = image_height + border_size

    background_color = (255, 255, 255)  # Beyaz arka plan rengi
    background = np.full((new_height, new_width, 3), background_color, dtype=np.uint8)

    x_offset = int((new_width - image_width) / 2)
    y_offset = int((new_height - image_height) / 2)
    background[y_offset:y_offset + image_height, x_offset:x_offset + image_width] = image
    return background


def find_cropped_image(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    scanned_image = scan_detection(image)
    warped = four_point_transform(scanned_image, document_contour.reshape(4, 2))
    warped_bordered = add_background(warped, 150)
    processed = image_processing(warped_bordered)
    rotated = best_rotation_method.rotate_with_tesseract(processed)
    cv2.imwrite('outputs/gray_img.png', gray_img)
    cv2.imwrite('outputs/processed.png', processed)
    cv2.imwrite('outputs/rotated.png', rotated)

    return rotated
