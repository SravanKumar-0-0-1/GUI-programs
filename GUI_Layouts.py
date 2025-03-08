# This file contains the code for the layout of the GUI
# This code is for creating a layout in the window.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.initUI()
    def initUI(self):
        central_widget=QWidget()
        self.setCentralWidget(central_widget)
        label1=QLabel("#1",self)
        label2=QLabel("#2",self)
        label3=QLabel("#3",self)
        label4=QLabel("#4",self)
        label5=QLabel("#5",self)
    
        label1.setStyleSheet("background-color:red")
        label2.setStyleSheet("background-color:blue")
        label3.setStyleSheet("background-color:green")
        label4.setStyleSheet("background-color:yellow")
        label5.setStyleSheet("background-color:orange")


        hbox=QGridLayout()
        hbox.addWidget(label1,0,0)
        hbox.addWidget(label2,0,1)
        hbox.addWidget(label3,1,0)
        hbox.addWidget(label4,1,1)
        hbox.addWidget(label5,2,2)
        central_widget.setLayout(hbox)
        


def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":   
    main()