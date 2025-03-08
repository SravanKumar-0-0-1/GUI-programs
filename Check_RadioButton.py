# This is a simple program to show how to use check box and radio button in pyqt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox,QRadioButton,QPushButton,QButtonGroup
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("C:/python full course/GUI_with_python/fear.png"))
        self.checkbox=QCheckBox("Do you like to stupid?",self)
        self.radio1=QRadioButton("idiot",self)
        self.radio2=QRadioButton("mental",self)
        self.radio3=QRadioButton("stage",self)
        self.radio4=QRadioButton("type",self)
        self.button_group1=QButtonGroup(self)
        self.button_group2=QButtonGroup(self)
        self.initUI()
    
    def initUI(self):
        self.checkbox.setGeometry(10,0,500,100)
        self.checkbox.setStyleSheet("font-size:30px;"
                                    "font-family:Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.check_on)
        self.radio1.setGeometry(10,100,300,100)
        self.radio2.setGeometry(10,150,300,100)
        self.radio3.setGeometry(10,200,300,100)
        self.radio4.setGeometry(10,250,300,100)

        self.setStyleSheet("QRadioButton{"
                           "font-size:30px;"
                           "font-family:Arial;"
                           "padding:10px;"
                           "}")
        
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group2.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
            radio=self.sender()
            if radio.isChecked():
                print(f"{radio.text()} is selected")
    def check_on(self,state):
        if state==Qt.Checked:
            print("you have been clicked")


def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":   
    main()