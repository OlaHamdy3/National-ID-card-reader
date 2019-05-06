from pytesseract import image_to_string
import cv2
import numpy as np
im_gray = cv2.imread('front10.jpg', cv2.IMREAD_GRAYSCALE)
im_bw = im_gray
thresh = 90
im_bw = cv2.threshold(im_bw, thresh, 255, cv2.THRESH_BINARY)[1]


pic = im_gray[50:350,50:275]
Name = im_bw[150:310, 400:1000]
address = im_bw[300:450, 400:1000]
ID = im_bw[500:560,400:1000]


name=image_to_string(Name,lang="ara")
add=image_to_string(address,lang="ara")
IDNumber=image_to_string(ID,lang="hin")
print(IDNumber)


IDNumber= ''.join(IDNumber.split())


if IDNumber[0]=='2': 
	year = '19' + IDNumber[1:3]
else:
	year = '20' + IDNumber[1:3]
month = IDNumber[3:5]
day = IDNumber[5:7]
BDate = year + '/' + month + '/'+ day


ocr_output=open("text.txt","w+")
ocr_output.write(name)
ocr_output.write('\n')
ocr_output.write(add)
ocr_output.write('\n')
ocr_output.write(IDNumber)
ocr_output.write('\n')
ocr_output.write(BDate)
ocr_output.close()
