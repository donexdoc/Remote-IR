import sys

from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication
from ui_control.MainFormControl import MainWindow


def main():

    app = QApplication([])
    app.setApplicationName('Remote IR')
    application = MainWindow()

    app_icon = QIcon()
    app_icon.addFile(u"assets/icons/app-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
    application.setWindowIcon(app_icon)

    application.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
