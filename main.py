from PyQt5.QtWidgets import QApplication

from GUI.WeatherGUI import WeatherGUI

import sys


app = QApplication(sys.argv)
ex = WeatherGUI()
sys.exit(app.exec_())
