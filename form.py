import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
from PIL import ImageFont, ImageDraw, Image
import arabic_reshaper
from bidi.algorithm import get_display
import integrate #front&back
def write_txt(image,txt,pos,size,color):
    font = ImageFont.truetype("arial.ttf", size, encoding="unic")
    reshaped_text = arabic_reshaper.reshape(txt)    # correct its shape
    bidi_text = get_display(reshaped_text)           # correct its direction
    # start drawing on image
    draw = ImageDraw.Draw(image)
    draw.text(pos, bidi_text, color, font=font)
    draw = ImageDraw.Draw(image)
    return image
def remove_newline(txt):
    txt_arr=txt.splitlines()
    res=""
    for i in txt_arr:
        if(i!=""):
            res=res+" "+i+" "
            
    return res
image = Image.open("empty_form.jpg")
front_path="front3.png"
back_path="back1.jpg"
integrate.front_read(front_path)
integrate.back_read(back_path)
name=remove_newline(integrate.name)
id=integrate.IDNumber
address=remove_newline(integrate.add)
birthdata=integrate.BDate
place_of_birth="empty"
gender=integrate.gender
religion=integrate.religion
social_status=integrate.a3zb
husband_name="none"#integrate.husband
job=integrate.job+" "+integrate.job2

font=70
margin=130
next_pos=890
start_x=700
image=write_txt(image,name,(start_x,next_pos),font,(0,0,0))
next_pos+=margin
image=write_txt(image,id,(start_x,next_pos),font,(0,0,0))
next_pos+=margin
image=write_txt(image,address,(start_x,next_pos),font,(0,0,0))
next_pos+=margin
image=write_txt(image,birthdata,(start_x,next_pos),font,(0,0,0))
next_pos+=margin
image=write_txt(image,place_of_birth,(start_x,next_pos),font,(0,0,0))
next_pos+=margin
image=write_txt(image,gender,(start_x,next_pos),font,(0,0,0))
next_pos+=margin
image=write_txt(image,religion,(start_x,next_pos),font,(0,0,0))
next_pos+=margin
image=write_txt(image,social_status,(start_x,next_pos),font,(0,0,0))
next_pos+=margin
image=write_txt(image,husband_name,(start_x,next_pos),font,(0,0,0))
next_pos+=margin
image=write_txt(image,job,(start_x,next_pos),font,(0,0,0))


image.save("out_form.jpg")
img = plt.imread('empty_form.jpg',0)
img_txt = plt.imread('out_form.jpg',0)
pic=integrate.pic
newpic = cv.resize(pic,(int(225*1.8),int(300*1.8)))
h = newpic.shape[0]
w = newpic.shape[1]
pos_x=300
pos_y=200
img_txt2=img_txt.copy()
for y in range(0, h):
        for x in range(0, w):
            img_txt2[(y+pos_y),(x+pos_x)]=newpic[y,x]
cv.imwrite("out_form.jpg",img_txt2)
plt.figure(figsize=(20,20))
plt.subplot(121),plt.imshow(img,'gray'),plt.title('empty_form')
plt.subplot(122),plt.imshow(img_txt2,'gray'),plt.title('output')
plt.show()