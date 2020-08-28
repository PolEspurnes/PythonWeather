from PyQt5.QtWidgets import QRadioButton, QPushButton, QDesktopWidget, QWidget
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import pyqtSlot

from GUI.ResultsGUI import ResultsGUI
from WeatherAPI import WeatherAPI


class MultipleOptionGUI(QWidget):

    def __init__(self, api, name, options):
        super().__init__()
        self.title = 'PythonWeather - Multiple Options'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 200
        self.cities = options
        self.name = name
        self.API = api
        self.results_window = None
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_buttons()
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

    def create_buttons(self):
        # Create a button for each city option
        self.option_buttons = []
        for i in range(len(self.cities)):
            str = self.name + " - " + self.cities[i]["country"]
            self.option_buttons.append(QRadioButton(str, self))
            self.option_buttons[i].move(280, 20 + (i*20))
            self.option_buttons[i].setStyleSheet("QRadioButton"
                             "{"
                             "color : white;"
                             "}"
                             )

        # connect button to function on_click
        self.search_button = QPushButton("Search", self)
        self.search_button.move(280, 160)
        self.search_button.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        for i in range(len(self.option_buttons)):
            if self.option_buttons[i].isChecked():
                print(self.option_buttons[i].text())
                response = self.API.GUI_option_selected(self.cities[i]["id"])
                if self.results_window is not None:
                    self.results_window.close()
                    self.results_window = None
                self.results_window = ResultsGUI(response)
                self.close()