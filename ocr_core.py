'''Credit to source for solution
https://stackabuse.com/pytesseract-simple-python-optical-character-recognition/
'''

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    #open image using Pillow and extract text from image
    text = pytesseract.image_to_string(Image.open(filename))  

    return text  


