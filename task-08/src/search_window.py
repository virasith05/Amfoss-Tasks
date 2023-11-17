
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QApplication, QWidget, QHBoxLayout, QMessageBox, QDialog, QVBoxLayout
from PySide6.QtGui import QPalette, QPixmap, QColor
from PySide6.QtCore import Qt
import requests
from PIL import Image
from display_window import DisplayWindow
import shutil


class SearchWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.w = None
        self.setFixedSize(850, 500)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.setGeometry(50, 50, 280, 40)

        self.flag = 0
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
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-size: cover;
            }
            QLabel {
                font-size: 20px;
                color:white;
                
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
            QLineEdit{
                background-color: dark-grey;
                color:white;
                border: 1px solid #60064F;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
                padding-left:5px;
            }
            """)

        palette = QPalette()

        background_image = QPixmap(
            '../assets/landing.jpg')
        palette.setBrush(QPalette.Window, background_image)

        self.setPalette(palette)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(500, 40, 180, 180)

        self.info = QLabel("", self)
        self.info.setGeometry(500, 200, 500, 300)

        self.label1 = QLabel("Enter the name", self)
        self.label1.setGeometry(50, 5, 600, 70)

        self.enter_button = QPushButton("Search", self)
        self.enter_button.setGeometry(50, 300, 160, 43)
        self.enter_button.clicked.connect(self.search)

        self.capture_button = QPushButton("Capture", self)
        self.capture_button.setGeometry(50, 350, 160, 43)
        self.capture_button.clicked.connect(self.capture)

        self.display_button = QPushButton("Display", self)
        self.display_button.setGeometry(50, 400, 160, 43)
        self.display_button.clicked.connect(self.open_display_window)
    ## TO-DO ##

    def search(self):
        empty_palette = QPalette()
        empty_palette.setBrush(QPalette.Window, QColor(20, 20, 20))
        self.setPalette(empty_palette)
        response = requests.get(
            "https://pokeapi.co/api/v2/pokemon/"+self.textbox.text().strip())
        if response.status_code == 200 and self.textbox.text().strip!="":

            data = response.json()
        else:
            image = Image.open(
                "../assets/9fe.jpg")
            resized_image = image.resize((180, 180))

            resized_image.save(
                "../assets/9feop.jpg")

            pixmap = QPixmap(
                "../assets/9feop.jpg")
            self.image_label.setPixmap(pixmap)
            return

        img_url = data["sprites"]["other"]["official-artwork"]["front_shiny"]
        try:
            img = requests.get(img_url, timeout=5)
            if (img.status_code == 200):

                with open("../downloads/downloaded_image.jpg", "wb") as f:
                    f.write(img.content)

            image = Image.open(
                "../downloads/downloaded_image.jpg")
            resized_image = image.resize((180, 180))


        except Exception as e:
            print(e)
            image = Image.open("../assets/default.jpeg")
            resized_default_image = image.resize((180, 180))
            resized_default_image.save("../downloads/downloaded_image.jpg")
# 
        resized_image = image.resize((180, 180))
        resized_image.save("../downloads/output.png")
        pixmap = QPixmap("../downloads/output.png")
        self.image_label.setPixmap(pixmap)
        self.flag = 1
        
          

        empty_palette = QPalette()
        empty_palette.setBrush(QPalette.Window, QColor(20, 20, 20))
        self.setPalette(empty_palette)
        abilities = [ability["ability"]["name"]
                     for ability in data["abilities"]]
        self.info.setText(f"""Name : {data["name"].upper()}
Abilities : {", ".join(abilities)}
Types : {data["types"][0]["type"]["name"]}
Stats : 
    HP : {data["stats"][0]["base_stat"]}
    Attack : {data["stats"][1]["base_stat"]}
    Defense : {data["stats"][2]["base_stat"]}
    Special-Attack : {data["stats"][3]["base_stat"]}
    Special-Defense : {data["stats"][4]["base_stat"]}
    Speed : {data["stats"][5]["base_stat"]}
                          """)

    def capture(self):
        empty_palette = QPalette()
        empty_palette.setBrush(QPalette.Window, QColor(20, 20, 20))
        self.setPalette(empty_palette)
        response = requests.get(
            "https://pokeapi.co/api/v2/pokemon/"+self.textbox.text().strip())
        if response.status_code == 200 and self.textbox.text().strip()!="":

            data = response.json()
        else:
            image = Image.open(
                "../assets/9fe.jpg")
            resized_image = image.resize((180, 180))

            resized_image.save(
                "../assets/9feop.jpg")

            pixmap = QPixmap(
                "../assets/9feop.jpg")
            self.image_label.setPixmap(pixmap)
            return

        img_url = data["sprites"]["other"]["official-artwork"]["front_shiny"]
        print(img_url)
        try:
            if (self.flag):
                shutil.copy("../downloads/downloaded_image.jpg",
                            "../capture/"+data["name"]+".jpg")
            else:
                img = requests.get(img_url, timeout=5)
                if (img.status_code == 200):

                    with open("../capture/"+data["name"]+".jpg", "wb") as f:
                        f.write(img.content)

            image = Image.open(
                "../capture/"+data["name"]+".jpg")

            resized_image = image.resize((180, 180))

            resized_image.save(
                "../downloads/output.png")
            pixmap = QPixmap(
                "../downloads/output.png")
            self.image_label.setPixmap(pixmap)

            message_box = QMessageBox(self)
            message_box.setStyleSheet("""QMessageBox {
            background-color: #050505;
            color: white;
            text-align:center;
            border: 2px solid #007ACC;
            font-size:20px;
        }
        QPushButton {
            background-color: #007ACC;
            color: white;
            border: 1px solid #007ACC;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #00578A;
            border: 1px solid #00578A;
        }
        QPushButton:pressed {
            background-color: #003655;
            border: 1px solid #003655;
        }
            """)
            message_box.setWindowTitle("Success")
            message_box.setText("Captured the pokemon")

            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec()

        except Exception as e:
            print(e)
            

    
    def open_display_window(self, checked):
        if self.w is None:
            self.w = DisplayWindow()
        self.w.show()


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
