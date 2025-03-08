# This is a simple program to show how to use line edit in PyQt5
# In this program, we will create a window with a label, a line edit and a button.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("C:/python full course/GUI_with_python/fear.png"))
        self.label=QLabel("Look at the Magic",self)
        self.label1=QLabel("",self)
        self.line_edit=QLineEdit(self)
        self.button=QPushButton("Submit",self)
        self.initUI()

    def initUI(self):
        self.label.setGeometry(100,10,400,100)
        self.label.setFont(QFont("Arial",20))
    
        self.line_edit.setGeometry(50,100,200,40)
        self.button.setGeometry(220,100,100,40)
        self.line_edit.setStyleSheet("font-size:20px;"
                                     "font-family:Arial;")
        self.line_edit.setPlaceholderText("Enter your Name")
        self.button.setStyleSheet("font-size:20px;"
                                     "font-family:Arial;"
                                     "color:black;"
                                     "background-color:#6fdcf7")
        self.label1.setGeometry(50,200,400,100)
        self.label1.setStyleSheet("font-size:30px;"
                                  "font-family:Arial;")
        self.button.clicked.connect(self.submit)

    def submit(self):
        text=self.line_edit.text()
        self.label1.setText(f"Hello {text}")




def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":   
    main()