# Developed by:   
   -Aliaa Mahmoud Ahmed      
   -Mostafa Atef Abd-Allah     
   -Mostafa Fahmy Al-Noqrashy      
   -Ola Hamdy Ahmed     
     Senior students at Faculty of Engineering, Ain-Shams University   
     
# Description
Copying information from national ID card is needed in each and every place we go to everyday, either to record it or to fill it in an application form. An error in only one digit can delay an urgent process for days.   
Therefore, it is necessary to develop software capable of scanning the card rapidly, and with high accuracy, extracting personal information from it, and providing this information to the user to reduce the time needed for copying along with typos.   
This project performs its tasks using Python Open-CV libraries.

# Inputs and Outputs
The software accepts photos of national ID cards captured using smart-phones or scanned with a scanner. It accepts photos with JPG, PNG, and JPEG extension; it generates a photo of a form in JPG format.  
  
  -Note: Make sure you capture a photo in good light conditions.
# How to run
1.Install all required libraries in the readme file then run the make file.   
```   
pip3 install python-opencv   
pip3 install PyQt5   
pip3 install matplotlib   
pip3 install Pillow=4.3.0   
pip3 install arabic-reshaper   
pip3 install imutils   
pip3 install scikit-image   
pip3 install argparse   
pip3 install python-bidi   
pip3 install pytesseract   
sudo apt-get install tesseract-ocr   
sudo apt-get install tesseract-ocr-ara   
sudo apt-get install tesseract-ocr-hin   
sudo ./makefile   
```     
2.Execute the command "python3 main.py".

# Test set
https://drive.google.com/open?id=1gmZd9nh37YwWUn7yeGeQdCAaWFBep9jD

# YouTube tutorial
https://www.youtube.com/watch?v=xUIy5EQ3R6s&t
