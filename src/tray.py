from PyQt5.QtWidgets import QSystemTrayIcon
from PyQt5.QtGui import QIcon


class Tray(QSystemTrayIcon):
    def __init__(self, parent, menu, icon: str = 'src/assets/tray.png'):
        super(Tray, self).__init__(parent)
        self.setIcon(QIcon(icon))
        self.setContextMenu(menu)
        self.__init()

    def __init(self):
        self.setObjectName('Tray')
        self.show()
