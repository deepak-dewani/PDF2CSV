from PIL import Image
import pytesseract
import os
from pdf2image import convert_from_path

folder_name = os.mkdir("f1")
def convert_pdf(path, folder_name):
    pages = convert_from_path(path)
    name = path.split('.')[0]
    # print(name)

    for i, page in enumerate(pages):
        page.save(f'{folder_name}/{i+1}.png','PNG')
    
convert_pdf("f1.pdf","f1")


