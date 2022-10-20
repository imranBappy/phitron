"""
My Camera Application
Author : Imran Hossen
Version : 1.0.0
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import QTimer
import cv2


class Window(QWidget):
    """ Main app window """

    def __init__(self):
        super().__init__()
        # variables for app window
        self.window_width = 640
        self.window_height = 400

        self.img_width = 640
        self.img_height = 400

        self.setWindowTitle("My web Cam")
        self.setGeometry(100, 100, self.window_width, self.window_height)
        self.setFixedSize(self.window_width, self.window_height)

        # setup timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)

        self.ui()

    def ui(self):
        """contains all ui things"""
        # images label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.img_width, self.img_height)

        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(10)

        self.show()

    def update(self):
        """Update frames"""
        _, self.frame = self.cap.read()
        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        step = channel * width
        q_frame = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(q_frame))
        pass

    def save_img(self):
        """ Save image from camera"""
        pass

    def record(self):
        """Record Video"""
        pass


# run app
app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
# python -m fbs my-cam
