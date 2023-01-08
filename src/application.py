from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QSlider, QVBoxLayout, QLabel, QHBoxLayout

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
            hbox.addWidget(self.__label(display['manufacturer']))
            hbox.addWidget(self.__slider(display['name']))
            vbox.addLayout(hbox)
        return vbox

    def __label(self, text: str):
        label = QLabel(self)
        label.setObjectName('Label')
        label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        label.setText(text)
        return label

    def __slider(self, display: int):
        slider = QSlider(Qt.Horizontal)
        slider.setObjectName('Slider')
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setTickInterval(10)
        slider.setSingleStep(5)
        slider.setValue(self.controls.get(display=display))
        slider.valueChanged.connect(lambda: self.controls.set(display=display, value=slider.value()))
        return slider
