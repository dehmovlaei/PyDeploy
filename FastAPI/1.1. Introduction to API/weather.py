import sys
from datetime import datetime, timedelta
import json
from requests import get as get_api
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.get_forecast("tehran")
        self.ui.lbl_error.setText("")
        self.ui.btn_search.clicked.connect(self.get_city)

    @staticmethod
    def create_path(description):
        if description == "Sunny":
            image_path = "./res/sun.png"
        elif description == "Cloudy":
            image_path = "./res/Cloudy.png"
        elif description == "Partly cloudy":
            image_path = "./res/partly.png"
        elif description == "Rainy":
            image_path = "./res/rain.png"
        else:
            image_path = "./res/sun.png"
        return image_path

    def get_forecast(self, city):
        url = f"https://goweather.herokuapp.com/weather/{city}"
        now = datetime.now()
        second_day = now + timedelta(days=2)
        third_day = now + timedelta(days=3)
        self.ui.lbl_d1.setText("Tomorrow")
        self.ui.lbl_d2.setText(second_day.strftime("%A"))
        self.ui.lbl_d3.setText(third_day.strftime("%A"))
        response = get_api(f"{url}")
        print(response.status_code)
        if response.status_code == 200:
            weather = json.loads(response.text)
            print(weather)
            temperature = weather.get("temperature")
            wind = weather.get("wind")
            description = weather.get("description")
            self.ui.lbl_tmp.setText(f"Real Feel: {temperature}")
            self.ui.lbl_wind.setText(f"Wind: {wind}")
            self.ui.lbl_desc.setText(f"Weather: {description}")
            self.define_png(description)
            three_day = weather.get("forecast")
            day_1 = three_day[0]
            day_2 = three_day[1]
            day_3 = three_day[2]
            self.ui.lbl_tmp1.setText(day_1.get("temperature"))
            self.ui.lbl_wind1.setText(day_1.get("wind"))
            self.ui.lbl_tmp2.setText(day_2.get("temperature"))
            self.ui.lbl_wind2.setText(day_2.get("wind"))
            self.ui.lbl_tmp3.setText(day_3.get("temperature"))
            self.ui.lbl_wind3.setText(day_3.get("wind"))
        else:
            self.ui.lbl_error.setText(f"City Name is not valid_{response.status_code}")

    def define_png(self, description):
        image_path = self.create_path(description)
        qpix = QPixmap(image_path)
        self.ui.lbl_qpix.setPixmap(qpix)
        self.ui.lbl_qpix.setScaledContents(True)

    def get_city(self):
        self.ui.lbl_error.setText("")
        self.get_forecast(self.ui.lne_city.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
