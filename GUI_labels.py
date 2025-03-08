# This code is for creating a label in the GUI window
# The label is used to display text or image in the window

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("C:/python full course/GUI_with_python/fear.png"))
        label1=QLabel("hello",self)
        label1.setFont(QFont("Arial",40))
        label1.setGeometry(0,0,500,100)
        label=QLabel(self)
        label.setGeometry(100,0,400,300)
        pixmap=QPixmap("C:/python full course/GUI_with_python/fear.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setGeometry((self.width()-label.width())//2,
                          (self.height()-label.height())//2,
                          label.width(),label.height())


def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":   
    main()