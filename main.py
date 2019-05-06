from PyQt5.uic import loadUiType
import sys
from os import path
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import form
import Scanner
import cv2
#from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
   # QPushButton, QCheckBox, QLabel, QLineEdit, QComboBox
#from PyQt5.QtGui import QIcon




FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "gui.ui"))
front_addr=''
back_addr=''
class MainApp(QMainWindow, FORM_CLASS):

    

    def __init__(self, parent= None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.front_btn.clicked.connect(self.front)

        self.back_btn.clicked.connect(self.back)

        self.generate_btn.clicked.connect(self.generate)


    def front(self):
        global front_addr
        front_addr,_ = QFileDialog.getOpenFileName(self,'Open File','',"Image files(*.jpg *.png *.jpeg)")
        Scanner.scan(front_addr,"front")
        #front_addr = str(front_addr)[2:str(front_addr).find(',')-1]
        pixmap = QPixmap("temp_front.jpg")
        self.label_imgf.setPixmap(pixmap)
        self.label_imgf.setScaledContents(True)
        
        
        print ("____",front_addr,"____")

    def back(self):
        global back_addr
        back_addr,_ = QFileDialog.getOpenFileName(self,'Open File','',"Image files(*.jpg *.png *.jpeg)")
        Scanner.scan(back_addr,"back")
        #back_addr = str(back_addr)[2:str(back_addr).find(',')-1]
        pixmap = QPixmap("temp_back.jpg")
        
        self.label_imgb.setPixmap(pixmap)
        self.label_imgb.setScaledContents(True)

        #print(input_file1)

        print ("____",back_addr,"____")
	
  
    def generate(self):
        global front_addr,back_addr
        if front_addr=='' or back_addr=='':
            QMessageBox.about(self, "Couldn't generate", "Image is not inserted!")
        else:
            form.form("temp_front.jpg","temp_back.jpg")
            print("done")
        
   


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


