import urllib

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QFont



class ResultsGUI(QWidget):

    def __init__(self, data):
        super().__init__()
        self.title = 'PythonWeather - Results'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.data = data
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background : salmon")

        self.center_window()

        self.createImage()

        self.generate_labels_style()

        self.set_label_text()

        self.show()


    def createImage(self):
        # loading image
        url = "http://openweathermap.org/img/wn/"+self.data["weather"][0]["icon"]+"@4x.png"

        data = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)

        self.photo = QLabel(self)
        self.photo.setGeometry(210, 10, 251, 281)
        self.photo.setText("")
        self.photo.setPixmap(pixmap)
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")



    def center_window(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())


    def generate_labels_style(self):
        self.title_label = QLabel(self)
        self.title_label.setGeometry(190, 250, 241, 20)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)

        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setObjectName("title_label")

        self.conditions_label = QLabel(self)
        self.conditions_label.setGeometry(90, 310, 171, 40)
        self.conditions_label.setObjectName("conditions_label")

        self.temperature_label = QLabel(self)
        self.temperature_label.setGeometry(90, 340, 171, 40)
        self.temperature_label.setObjectName("temperature_label")

        self.min_temp_label = QLabel(self)
        self.min_temp_label.setGeometry(90, 380, 181, 40)
        self.min_temp_label.setObjectName("min_temp_label")

        self.max_temp_label = QLabel(self)
        self.max_temp_label.setGeometry(90, 420, 171, 40)
        self.max_temp_label.setObjectName("max_temp_label")

    def set_label_text(self):
        self.title_label.setText(self.data["name"]+" -- "+self.data["sys"]["country"])
        self.conditions_label.setText("Weather Conditions: "+self.data["weather"][0]["main"])
        self.temperature_label.setText("Actual temperature: "+str(self.data["main"]["temp"])+"ºC")
        self.min_temp_label.setText("Minimum temperature: "+str(self.data["main"]["temp_min"])+"ºC")
        self.max_temp_label.setText("Maximum temperature: "+str(self.data["main"]["temp_max"])+"ºC")
