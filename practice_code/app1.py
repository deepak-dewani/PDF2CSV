from PIL import Image
import pytesseract as pt
import os

folder_name = os.mkdir("f2")
def main():
    path = "/home/deepak/Documents/pdf2image/f1"
    tempPath ="/home/deepak/Documents/pdf2image/f2/"

    for imageName in os.listdir(path):
        inputpath = os.path.join(path, imageName)
        text = pt.image_to_string(Image.open(inputpath))
        imageName = imageName[0:-4]
        fulltemppath = os.path.join(tempPath, 'page_'+imageName+".txt")
        print(text)
        
        file1 = open(fulltemppath, "w")
        file1.write(text)
        file1.close()

if __name__ == '__main__':
    main()

        
        # text = pytesseract.image_to_string(Image.open(img))
        # print(text) 

# main("f1", "outfile")
# image = '/home/deepak/Documents/pdf2image/f1/1.png'
# text = pytesseract.image_to_string(Image.open(image))
# print(text)