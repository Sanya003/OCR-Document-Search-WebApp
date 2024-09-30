from PIL import Image
import pytesseract

def ocr_image(image_path):
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image, lang='eng+hin')
    return extracted_text

print(f'Extracted text: \n {ocr_image(input())}')