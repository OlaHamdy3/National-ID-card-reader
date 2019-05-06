from PIL import Image
import cv2
from pytesseract import image_to_string
import numpy as np
import pob
import gender as gn
pic =np.zeros((300,225))
name,add,IDNumber,BDate = '','','',''
job,job2,gender,religion,a3zb,husband,govern = '','','','','','',''
#Reading the front side of the ID card
def front_read(front_src):
	
	im_gray = cv2.imread(front_src, cv2.IMREAD_GRAYSCALE)
	im_bw = im_gray
	thresh = 95
	im_bw = cv2.threshold(im_bw, thresh, 255, cv2.THRESH_BINARY)[1]
	global pic
	global name
	global add
	global IDNumber
	global BDate
	global govern
	# split the img
	pic = im_gray[50:350,50:275]
	Name = im_bw[150:310, 400:1000]
	address = im_bw[300:450, 400:1000]
	ID = im_bw[500:560,400:1000]
	# Reading the splitted images
	name=image_to_string(Name,lang="ara")
	add=image_to_string(address,lang="ara")
	IDNumber=image_to_string(ID,lang="hin")
	IDNumber= ''.join(IDNumber.split())
	
	#Calculate the birth date
	if IDNumber[0]=='2': 
		year = '19' + IDNumber[1:3]
	else:
		year = '20' + IDNumber[1:3]
	month = IDNumber[3:5]
	day = IDNumber[5:7]
	BDate = year + '/' + month + '/'+ day
	#Getting the governorate.
	govern = pob.placeOfBirth(IDNumber)


# split image
def crop(dim1,dim2,dim3,dim4,name,img_binary,text_all):
	area=(dim1,dim2,dim3,dim4)
	cropped_img=img_binary.crop(area)
	text=image_to_string(cropped_img,lang='ara')
##	cropped_img.show()
	if name=='religion':
		
		if 'مسلم' in text_all:
			text='مسلم'
		elif 'مسيحي' in text_all:
			text='مسيحي'
		elif 'مسيحى' in text_all:
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
		elif 'انثى' in text_all:
			text='أنثى'

	if name=='a3zb':
		if 'أنسة' in text_all:
			text='أنسة'
		elif 'متزوجة' in text_all:
			text='متزوجة'
		elif 'متزوج' in text_all:
			text='متزوج'
		elif 'أعزب' in text_all:
			text='أعزب'
	
	return text


# Reading the data from the back side of the ID card
def back_read(source_image):
	
	img=Image.open(source_image) #1005 630
	im_gray = cv2.imread(source_image, cv2.IMREAD_GRAYSCALE)
	ret,thresh_img = cv2.threshold(im_gray,145,255,cv2.THRESH_BINARY)
	kernel = np.ones((2,2),np.uint8)
	cv2.imwrite('threshold.jpg',thresh_img)
	img_binary=Image.open('threshold.jpg')
	text_all=image_to_string(img_binary,lang='ara')
	global job,job2,gender,religion,a3zb,husband
	global IDNumber

	job = crop(230,70,820,140,'job',img_binary,text_all)
	# job2 represents the place of work
	job2 = crop(230,125,820,190,'job2',img_binary,text_all)
	#gender = crop(700,180,820,260,'gender',img_binary,text_all)
	gender = gn.gen(IDNumber)
	religion = crop(480,180,760,260,'religion',img_binary,text_all)

	a3zb = crop(200,180,570,260,'a3zb',img_binary,text_all)
	# husband name in case of women
	husband = crop(200,225,820,290,'husband',img_binary,text_all)
