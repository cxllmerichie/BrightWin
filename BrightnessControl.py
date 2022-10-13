import screen_brightness_control as sbc
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QSlider, QApplication, QVBoxLayout, QLabel
from sys import argv


class Application(QWidget):
    def __init__(self):
        super(Application, self).__init__()
        self.setWindowTitle('BrightnessControl')
        self.setLayout(self.__layout())
        self.show()

    def  __layout(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.__label('Primary display'))
        vbox.addWidget(self.__slider(display=1))
        vbox.addWidget(self.__label('Secondary display'))
        vbox.addWidget(self.__slider(display=0))
        return vbox

    def __label(self, text: str):
        label = QLabel(self)
        label.setFixedSize(QSize(400, 20))
        label.setFont(QFont('Colibri', 13))
        label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        label.setText(text)
        return label

    def __slider(self, *, display: int):
        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setTickInterval(10)
        slider.setSingleStep(5)
        slider.setFixedSize(QSize(400, 100))
        slider.setValue(sbc.get_brightness(display=display)[0])

        def set_brightness():
            sbc.set_brightness(display=display, value=slider.value())

        slider.valueChanged.connect(set_brightness)
        return slider


def main():
    qapp = QApplication(argv)
    app = Application()
    qapp.exec()


if __name__ == '__main__':
    main()
