from PySide6.QtWidgets import QApplication, QStyleFactory
import sys

from src.app import Tray
from src.style import style


def main():
    qapp = QApplication(sys.argv)
    qapp.setStyle(QStyleFactory.keys()[2])
    qapp.setStyleSheet(style)
    qapp.setQuitOnLastWindowClosed(False)

    app = Tray()
    app.show()

    sys.exit(qapp.exec())


if __name__ == '__main__':
    main()
