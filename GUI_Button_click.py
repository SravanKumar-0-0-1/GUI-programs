# This code is for creating a button and a label in the window.
#  When the button is clicked, the label will change its text to "You Hacked 😊".

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QPushButton
from PyQt5.QtGui import QIcon,QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("C:/python full course/GUI_with_python/fear.png"))
        self.button=QPushButton("Click here!",self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size:30px")
        self.button.clicked.connect(self.on_click)

        self.label = QLabel("hi", self)
        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet("font-size:30px")
    def on_click(self):
        self.label.setText("You Hacked 😊")



def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":   
    main()