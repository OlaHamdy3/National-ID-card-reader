from PIL import Image
import cv2
import pytesseract as image_to_string
import numpy as np

img=Image.open("bta2a1.jpeg") #1005 630
filew = open('output.txt','w+')
#text=image_to_string.image_to_string(img,lang='ara')
#filew.write(text)


im_gray = cv2.imread('bta2a1.jpeg', cv2.IMREAD_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 90
img_binary = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
kernel = np.ones((2,2),np.uint8)
img_binary = cv2.erode(img_binary,kernel,iterations = 1)
img_binary = cv2.medianBlur(img_binary, 1)
cv2.imwrite('bta2a3.png',img_binary)
img_binary=Image.open("bta2a3.png")
'''
kollo=cv2.imread("im.png")
kollo = cv2.erode(kollo,kernel,iterations = 1)
cv2.imwrite('im2.jpeg',kollo)
kollo=Image.open("im2.jpeg")
'''
def crop(dim1,dim2,dim3,dim4,name):
	area=(dim1,dim2,dim3,dim4)
	cropped_img=img_binary.crop(area)
	
	cropped_img.save(name+'.jpeg')
	#img2=Image.open('job.jpeg')
	text=image_to_string.image_to_string(cropped_img,lang='ara')
	print(text)
	#filew = open('output.txt','w+')
	filew.write(text+'\n')
	#if name=='a3zb':
	#	cropped_img.show()




def crop_date(dim1,dim2,dim3,dim4,name):
	area=(dim1,dim2,dim3,dim4)
	cropped_img=img_binary.crop(area)
	
	cropped_img.save(name+'.jpeg')

	text=image_to_string.image_to_string(cropped_img,lang='eng')
	print(text)
	#filew = open('output.txt','w+')
	filew.write(text+'\n')




crop(230,70,820,140,'job')

crop(230,120,820,190,'job2')

crop(700,180,820,260,'gender')

crop(480,180,760,260,'religion')

crop(200,180,570,260,'a3zb')

#crop_date(200,0,570,60,'date')



filew.close()

