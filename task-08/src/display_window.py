import sys
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QApplication, QWidget, QHBoxLayout, QMessageBox, QDialog, QVBoxLayout
from PySide6.QtGui import QPalette, QPixmap, QColor
from PySide6.QtCore import QRect
import os
from PIL import Image


class DisplayWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setFixedSize(500, 650)

        

        self.image_label = QLabel(self)
        self.image_label.setGeometry(30, 30, 440, 580)

        self.pre = QPushButton("Previous", self)
        self.pre.setGeometry(30, 600, 160, 43)

        empty_palette = QPalette()
        empty_palette.setBrush(QPalette.Window, QColor(20, 20, 20))
        self.setPalette(empty_palette)

        self.next = QPushButton("Next", self)
        self.next.setGeometry(310, 600, 160, 43)
        self.name_tag = QLabel("Name", self)
        self.name_tag.setGeometry(90, 550, 280, 40)
        self.ind = 0
        self.images = '../capture/'
        my_pm = os.listdir(self.images)
        if (len(my_pm) == 0):
            self.name_tag.setText("You have no pokemon")
        else:
            image = Image.open(self.images+"/"+my_pm[self.ind])
            resized_image = image.resize((400, 500))

            resized_image.save(
                "../downloads/dis.png")

            pixmap = QPixmap(
                "../downloads/dis.png")
            self.image_label.setPixmap(pixmap)
            self.name_tag.setText(my_pm[self.ind][:-4].upper())
        self.pre.clicked.connect(self.prev_img)
        self.next.clicked.connect(self.next_img)

        self.setStyleSheet("""
            QPushButton {
                background-color: dark-grey;
                color: white;
                border: 1px solid #BA263E;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
            }
            QMainWindow {
                background-color: grey;
            }
           
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
            QLabel{
                color:white;
                font-size: 30px;
            }
            """)

    def next_img(self):
        my_pm = os.listdir(self.images)
        if (len(my_pm) == 0):
            self.name_tag.setText("You have no pokemon")
        else:
            
            self.ind = (self.ind + 1) % len(my_pm)
            image = Image.open(self.images+"/"+my_pm[self.ind])
            resized_image = image.resize((400, 500))

            resized_image.save(
                "../downloads/dis.png")

            pixmap = QPixmap(
                "../downloads/dis.png")
            self.image_label.setPixmap(pixmap)
            self.name_tag.setText(my_pm[self.ind][:-4].upper())

    def prev_img(self):
        my_pm = os.listdir(self.images)
        if (len(my_pm) == 0):
            self.name_tag.setText("You have no pokemon")
        else:
            
            self.ind = (self.ind - 1) % len(my_pm)
            image = Image.open(self.images+"/"+my_pm[self.ind])
            resized_image = image.resize((400, 500))
            os.remove("../downloads/dis.png")
            resized_image.save(
                "../downloads/dis.png")

            pixmap = QPixmap(
                "../downloads/dis.png")
            self.image_label.setPixmap(pixmap)
            self.name_tag.setText(my_pm[self.ind][:-4].upper())


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = DisplayWindow()
    window.show()
    sys.exit(app.exec())
