from PySide6.QtWidgets import (
    QSystemTrayIcon, QMenu, QSlider, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QApplication
)
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt, QSize, Slot
from pynput.mouse import Listener
import webbrowser

from .utils import Brightness


class Menu(QMenu):
    def __init__(self):
        super().__init__()
        self.setObjectName(self.__class__.__name__)

        self.addAction(self._action('Help', lambda: webbrowser.open('https://github.com/cxllmerichie/BrightnessControl-Desktop-')))
        self.addAction(self._action('Close', QApplication.instance().quit))

    def _action(self, title: str, event) -> QAction:
        action = QAction(title, self)
        action.setObjectName('Action')
        action.triggered.connect(event)
        return action


class TrayActive(QFrame):
    instantiated: bool = False

    def __init__(self):
        super().__init__()
        self.setObjectName(self.__class__.__name__)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        self.setLayout(self._layout())
        TrayActive.instantiated = True

    def display(self):
        self.show()
        screen: QSize = QApplication.instance().primaryScreen().size()
        self.move(screen.width() - self.width(), screen.height() - self.height())

        def on_click(x, y, button, pressed):
            if pressed:  # True - clicked, False - released
                out_of_x = x < self.x() or x > self.x() + self.width()
                out_of_y = y < self.y() or y > self.y() + self.height()
                if out_of_x or out_of_y:
                    TrayActive.instantiated = False
                    self.hide()
                    return False  # stop the Listener (pynput feature)

        Listener(on_click=on_click).start()

    def _layout(self) -> QVBoxLayout:
        def button(display: dict) -> QPushButton:
            btn = QPushButton(display['manufacturer'], self)
            btn.setToolTip(display['name'])
            btn.setObjectName('Button')

            @Slot()
            def slot():
                brightness = 100 if Brightness.get(display['name']) == 0 else 0
                self.findChildren(QSlider)[Brightness.displays().index(display)].setValue(brightness)

            btn.clicked.connect(slot)
            return btn

        def slider(display: dict) -> QSlider:
            sld = QSlider(Qt.Horizontal, self)
            sld.setObjectName('Slider')
            sld.setFocusPolicy(Qt.StrongFocus)
            sld.setTickPosition(QSlider.TickPosition.TicksBothSides)
            sld.setTickInterval(10)
            sld.setSingleStep(10)
            sld.setValue(Brightness.get(display=display))
            sld.enterEvent = lambda event: sld.setToolTip(f'{sld.value()}%')  # dynamically changing toolTip
            sld.valueChanged.connect(lambda: Brightness.set(display=display, value=sld.value()))
            return sld

        vbox = QVBoxLayout(self)
        vbox.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        vbox.setSpacing(20)
        for display in Brightness.displays():
            hbox = QHBoxLayout(self)
            hbox.setSpacing(5)
            hbox.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            hbox.addWidget(button(display), alignment=Qt.AlignVCenter | Qt.AlignLeft)
            hbox.addWidget(slider(display['name']))
            vbox.addLayout(hbox)
        return vbox


class Tray(QSystemTrayIcon):
    def __init__(self):
        super(Tray, self).__init__()
        self.setObjectName(self.__class__.__name__)
        self.setIcon(QIcon('assets/icon-white.png'))
        self.setContextMenu(Menu())

        self.activated.connect(self.activate)

    def activate(self, reason: QSystemTrayIcon.ActivationReason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:  # left mouse click
            if not TrayActive.instantiated:
                TrayActive().display()
