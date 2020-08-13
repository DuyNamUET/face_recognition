from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import datetime
import sys

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Face App"
        self.left = 0; self.top = 0
        self.width = 1280; self.height = 720

        self.initUI()
    
    def initUI(self):
        # Main window
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: rgb(187, 225, 250);")

        # Camera area
        self.cam_area = QLabel(self)
        self.cam_area.setGeometry(0,0,750,720)
        self.cam_area.setStyleSheet("background-color: rgb(15, 76, 117);")

        # Show camera
        self.cam = QLabel(self)
        self.cam.setGeometry(55,50,640,480)
        self.cam.setStyleSheet("border-color: rgb(187, 225, 250);"
                                "border-radius: 20px;"
                                "border-width: 6px;"
                                "border-style: solid;")

        # Attendance button
        self.attendance_button = QPushButton("Attendance", self)
        self.attendance_button.setGeometry(225,580,300,100)
        self.attendance_button.clicked.connect(self.click_attendance_button)
        self.attendance_button.setStyleSheet("background-color: rgb(50, 130, 184);"
                                            "border-color: rgb(50, 130, 184);"
                                            "border-radius: 20px;"
                                            "border-width: 6px;"
                                            "border-style: solid;"
                                            "font-size: 50px;"
                                            "color: rgb(255, 255, 255)") 

        # Date-Time label
        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setGeometry(800, 150, 440, 120)
        font_timer = QFont('Roboto', 60, QFont.Bold)
        self.time_label.setFont(font_timer)
        timer = QTimer(self)
        timer.timeout.connect(self.updateTimer)
        timer.start(1000)
        self.time_label.setStyleSheet("color: rgb(15, 76, 117);")

        self.date_label = QLabel(self)
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setGeometry(854,270,330,50)
        font_date = QFont('Roboto', 40, QFont.Bold)
        self.date_label.setFont(font_date)
        date = QTimer(self)
        date.timeout.connect(self.updateTimer)
        date.start(1000)
        self.date_label.setStyleSheet("color: rgb(15, 76, 117);")

        self.welcome = QLabel("Welcome!", self)
        self.welcome.setGeometry(800, 400, 444, 120)
        font_welcome = QFont('Roboto', 60, QFont.Bold)
        self.welcome.setFont(font_welcome)
        self.welcome.setStyleSheet("color: rgb(15, 76, 117);")


        self.show()

    def updateTimer(self):
        today = str(datetime.datetime.today())
        date = today.split(' ')[0]
        time = today.split(' ')[1].split('.')[0]
        self.time_label.setText(time)
        self.date_label.setText(date) 
    
    def click_attendance_button(self):
        print("Attendance")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())