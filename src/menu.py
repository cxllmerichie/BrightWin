from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMenu, QWidgetAction, QWidget, QShortcut


class Menu(QMenu):
    def __init__(self, parent, layout):
        super(Menu, self).__init__(parent=parent)
        self.addAction(self._action(self, layout))
        self.__init()

    def __init(self):
        self.setObjectName('Menu')
        self.__shortcut('Ctrl+Q', self.parent().close)

    def __shortcut(self, keys: str, signal: callable) -> QShortcut:
        shortcut: QShortcut = QShortcut(QKeySequence(keys), self)
        shortcut.activated.connect(signal)
        return shortcut

    def _action(self, parent: QMenu, layout):
        action = QWidgetAction(parent)
        widget = QWidget(self)
        widget.setLayout(layout)
        action.setDefaultWidget(widget)
        return action
