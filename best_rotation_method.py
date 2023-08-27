import cv2
import pytesseract
import enchant
from nltk.corpus import stopwords
import nltk
import math

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


def rotate_with_tesseract(image):
    custom_config = r'--oem 3 --psm 6'
    dictionary = enchant.Dict("en_US")
    meaningful_dict = {}

    for angle in range(0, 361, 90):
        meaningful_english_words = []
        image_center = tuple(map(int, (image.shape[1] / 2, image.shape[0] / 2)))
        rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1)
        result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
        details = pytesseract.image_to_data(result, config=custom_config, output_type=pytesseract.Output.DICT)

        for word_text in details['text']:
            if word_text.strip() and dictionary.check(word_text):
                cleaned_word = word_text.strip()
                meaningful_english_words.append(cleaned_word)
                meaningful_english_words = [item for item in meaningful_english_words if len(item) > 3]
        meaningful_dict[str(angle)] = len(meaningful_english_words)

    max_value = max(meaningful_dict.values())
    optimal_angle = max(meaningful_dict, key=meaningful_dict.get)

    print("Optimal Angle with Max Value:", optimal_angle)
    print("Max meaningful words count:", max_value)
    rotated_img = image.copy()
    if int(optimal_angle) == 180:
        for _ in range(2):
            rotated_img = cv2.rotate(rotated_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return rotated_img
    if int(optimal_angle) == 270:
        for _ in range(3):
            rotated_img = cv2.rotate(rotated_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return rotated_img
    else:
        rotated_img = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return rotated_img
    # rot_mat = cv2.getRotationMatrix2D(image_center, int(optimal_angle), 1)
    # rotated_img = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)



