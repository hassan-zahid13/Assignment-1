import cv2
import pytesseract
test = cv2.imread('test.png')
text = pytesseract.image_to_string(test)
print(text)