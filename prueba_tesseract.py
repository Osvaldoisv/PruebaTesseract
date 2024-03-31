import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

image = cv2.imread('imgColores.jpg')

text = pytesseract.image_to_string(image,lang='eng')
print('Text: ',text)
      
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()