# importing libraries
import socket
import PIL.Image as qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.connect(('localhost', 2668))


# window class
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'Guesser'


        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)

        pybutton = QPushButton('Send', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200, 32)
        pybutton.move(80, 60)


        self.setWindowTitle(self.title)
        self.setGeometry(600, 300, 800,600)
        image = qt.open('croc.png')
        new_image = image.resize((250, 250))
        new_image.save('myimage_500.jpg')
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('myimage_500.jpg')

        label.setPixmap(pixmap)
        label.move(500, 40)


    def clickMethod(self):
        pass
        item = self.line.text()
        print(item)
        sock.send(f'{item}'.encode())


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# showing the window
window.show()

# start the app
sys.exit(App.exec())
