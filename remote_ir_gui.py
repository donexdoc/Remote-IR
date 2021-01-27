import sys
import os

from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication
from ui_control.MainFormControl import MainWindow


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("./assets/icons")

    return os.path.join(base_path, relative_path)


def main():

    app = QApplication([])
    app.setApplicationName('Remote IR')
    application = MainWindow()

    app_icon = QIcon()
    app_icon.addFile(resource_path("app-icon.svg"), QSize(), QIcon.Normal, QIcon.Off)
    application.setWindowIcon(app_icon)

    application.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
