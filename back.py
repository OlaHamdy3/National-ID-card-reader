from PIL import Image
import cv2
import pytesseract as image_to_string
import numpy as np



source_image='baba2.jpg'
img=Image.open(source_image) #1005 630
#text_all=image_to_string.image_to_string(img,lang='ara')
filew = open('output.txt','w+')

#text=image_to_string.image_to_string(img,lang='ara')
#filew.write(text)


im_gray = cv2.imread(source_image, cv2.IMREAD_GRAYSCALE)
ret,thresh_img = cv2.threshold(im_gray,140,255,cv2.THRESH_BINARY)
kernel = np.ones((2,2),np.uint8)
img_binary = cv2.erode(thresh_img,kernel,iterations = 1)
img_binary = cv2.medianBlur(img_binary, 1)
cv2.imwrite('threshold.jpg',thresh_img)

img_binary=Image.open('threshold.jpg')
text_all=image_to_string.image_to_string(img_binary,lang='ara')


def crop(dim1,dim2,dim3,dim4,name):
	area=(dim1,dim2,dim3,dim4)
	cropped_img=img_binary.crop(area)
	cropped_img.save(name+'.jpeg')
	#img2=Image.open('job.jpeg')
	text=image_to_string.image_to_string(cropped_img,lang='ara')
	if name=='religion':
		if 'مسلم' in text_all:
			text='مسلم'
		elif 'مسيحي' in text_all:
			text='مسيحي'
		elif 'مسلمة' in text_all:
			text='مسلمة'
		elif 'مسيحية' in text_all:
			text='مسيحية'
	if name=='gender':
		if 'ذكر' in text_all:
			text='ذكر'
		elif 'أنثى' in text_all:
			text='أنثى'

	print(text)
	filew.write(text+'\n')


def crop_date(dim1,dim2,dim3,dim4,name):
	area=(dim1,dim2,dim3,dim4)
	cropped_img=img_binary.crop(area)
	
	cropped_img.save(name+'.jpeg')

	text=image_to_string.image_to_string(cropped_img,lang='eng')
	print(text)
	#filew = open('output.txt','w+')
	filew.write(text+'\n')




crop(230,70,820,140,'job')

crop(230,125,820,190,'job2')

crop(700,180,820,260,'gender')

crop(480,180,760,260,'religion')

crop(200,180,570,260,'a3zb')

#crop_date(200,0,570,60,'date')



filew.close()

