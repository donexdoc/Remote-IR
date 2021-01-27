from PySide2.QtWidgets import QDialog

from ui_design.pyforms.AboutWindowForm import Ui_DialogInfo

import config_gui


class InfoWindow(QDialog):
    """
    Форма с отображением информации о программе
    """

    def __init__(self, parent):
        super(InfoWindow, self).__init__(parent)

        self.ui = Ui_DialogInfo()
        self.ui.setupUi(self)
        self.ui.programmVersionLb.setText(config_gui.PROGRAM_VERSION)
