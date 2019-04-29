from PIL import Image
import cv2
import pytesseract as image_to_string
import numpy as np

img=Image.open("baba2.jpg") #1005 630
filew = open('output.txt','w+')
#text=image_to_string.image_to_string(img,lang='ara')
#filew.write(text)


im_gray = cv2.imread('baba2.jpg', cv2.IMREAD_GRAYSCALE)
ret,thresh_img = cv2.threshold(im_gray,140,255,cv2.THRESH_BINARY)
kernel = np.ones((2,2),np.uint8)
img_binary = cv2.erode(thresh_img,kernel,iterations = 1)
img_binary = cv2.medianBlur(img_binary, 1)
cv2.imwrite('threshold.jpg',thresh_img)


img_binary=Image.open('threshold.jpg')
text=image_to_string.image_to_string(img,lang='ara')
#print(text)
#filew.write(text+'\n')
if 'مسلم' in text:
	print("YESSSSSSSSSSSSSSSSSSSSS")

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

