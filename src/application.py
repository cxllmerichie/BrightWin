from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QSlider, QVBoxLayout, QLabel, QHBoxLayout, QPushButton
from screen_brightness_control.helpers import ScreenBrightnessError

from .menu import Menu
from .tray import Tray
from .utils import Controls


class Application(QMainWindow):
    def __init__(self):
        super(Application, self).__init__()

        self.controls = Controls()

        self.menu = Menu(self, self.__layout())
        self.tray = Tray(self, self.menu)

        self.__init()

    def __init(self):
        self.setObjectName('Application')
        self.setWindowTitle('BrightnessControl')

    def __layout(self):
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        vbox.setSpacing(20)
        for display in self.controls.displays:
            hbox = QHBoxLayout()
            hbox.setSpacing(5)
            hbox.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            hbox.addWidget(self.__button(display), alignment=Qt.AlignVCenter | Qt.AlignLeft)
            try:
                hbox.addWidget(self.__slider(display['name']))
            except ScreenBrightnessError:
                pass
            else:
                vbox.addLayout(hbox)
        return vbox

    def __button(self, display):
        button = QPushButton(self)
        button.setObjectName('Button')

        def signal():
            new = 100 if self.controls.get(display['name']) == 0 else 0
            self.controls.set(new, display['name'])
            self.findChildren(QSlider)[self.controls.displays.index(display)].setValue(new)

        button.clicked.connect(signal)
        button.setText(display['manufacturer'])
        return button

    def __slider(self, display):
        slider = QSlider(Qt.Horizontal)
        slider.setObjectName('Slider')
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setTickInterval(10)
        slider.setSingleStep(10)
        slider.setValue(self.controls.get(display=display))
        slider.valueChanged.connect(lambda: self.controls.set(display=display, value=slider.value()))
        return slider
