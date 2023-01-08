from PyQt5.QtWidgets import QApplication
import sys

from src import Application, style


def main():
    qapp = QApplication(sys.argv)
    qapp.setStyle('Windows')
    qapp.setStyleSheet(style)
    app = Application()
    sys.exit(qapp.exec_())


if __name__ == '__main__':
    main()
