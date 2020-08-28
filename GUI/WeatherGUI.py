from PyQt5.QtWidgets import QPushButton, QMessageBox, QLineEdit, QDesktopWidget, QMainWindow
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import pyqtSlot

from GUI.ResultsGUI import ResultsGUI
from WeatherAPI import WeatherAPI
from GUI.MultipleOptionGUI import MultipleOptionGUI




class WeatherGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PythonWeather'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.options_window = None
        self.results_window = None
        self.API = WeatherAPI()
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)



        self.create_textbox()
        self.center_window()
        self.paint_window()
        self.show()

    def paint_window(self):
        window_pal = QPalette()
        window_pal.setColor(QPalette.Window, QColor(72, 72, 74))
        self.setPalette(window_pal)
        self.search_button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : #e96e50;"
                             "}"
                             )

    def center_window(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def create_textbox(self):
        # Create textbox
        self.search_textbox = QLineEdit(self)
        self.search_textbox.move(20, 40)
        self.search_textbox.resize(600, 40)

        # Create a button in the window
        self.search_button = QPushButton('Search city', self)
        self.search_button.move(280, 100)


        # connect button to function on_click
        self.search_button.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        city = self.search_textbox.text()
        if city in self.API.cities:
            found = self.API.cities[city]
            l = len(found)
            if l > 1:
                if self.options_window is not None:
                    self.options_window.close()
                    self.options_window = None

                self.options_window = MultipleOptionGUI(self.API, city, found)
            else:
                if self.results_window is not None:
                    self.results_window.close()
                    self.results_window = None
                data = self.API.GUI_option_selected(self.API.cities[city][0]["id"])
                self.results_window = ResultsGUI(data)
        else:
            QMessageBox.question(self, 'Error', "City not found", QMessageBox.Ok, QMessageBox.Ok)
            self.search_textbox.setText("")
