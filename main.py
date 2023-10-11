# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':

#     print_hi('PyCharm')

'''
# print('kjsdgbjh')
# import paddle
# from PaddleOCR import PaddleOCR, draw_ocr # main OCR dependencies

# paddle.utils.run_ch


#
# from paddleocr import PaddleOCR, draw_ocr # main OCR dependencies
# from matplotlib import pyplot as plt # plot images
# import cv2 #opencv
# import os # folder directory navigation
#
# ocr_model= PaddleOCR()#lang='ar')
#
# result=ocr_model.ocr('images/english_text.PNG')
# print(result)
#
# for res in result[0]:
#         print(res[1][0])
'''


#downloaded from https://github.com/UB-Mannheim/tesseract/wiki , then run installer


import pytesseract
import cv2
# import matplotlib as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'



# img=cv2.imread('images/bbcnews.PNG')

#download arabic data https://tesseract-ocr.github.io/tessdoc/Data-Files   , then paste it to  C:\Program Files\Tesseract-OCR\tessdata

# text =pytesseract.image_to_string(img,lang='ara')
# print(text)

# cv2.imshow('image', img)
# cv2.waitKey(0)


def extract_ar_text(image_url):
    image = cv2.imread(image_url)
    text = pytesseract.image_to_string(image, lang='ara')
    print(text)

    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

url_text='images/eng+ara.PNG'

extract_ar_text(url_text)
