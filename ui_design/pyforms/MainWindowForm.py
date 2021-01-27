# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(909, 505)
        icon = QIcon()
        icon.addFile(u"../../assets/icons/app-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockNestingEnabled(True)
        self.updatePortListAct = QAction(MainWindow)
        self.updatePortListAct.setObjectName(u"updatePortListAct")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.updatePortListBtn = QPushButton(self.centralwidget)
        self.updatePortListBtn.setObjectName(u"updatePortListBtn")
        icon1 = QIcon()
        icon1.addFile(u"../../assets/icons/sync-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.updatePortListBtn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.updatePortListBtn)

        self.serialPortCmbx = QComboBox(self.centralwidget)
        self.serialPortCmbx.setObjectName(u"serialPortCmbx")
        self.serialPortCmbx.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.serialPortCmbx)

        self.serialRateLe = QLineEdit(self.centralwidget)
        self.serialRateLe.setObjectName(u"serialRateLe")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialRateLe.sizePolicy().hasHeightForWidth())
        self.serialRateLe.setSizePolicy(sizePolicy)
        self.serialRateLe.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.serialRateLe)

        self.receiveChangeBtn = QPushButton(self.centralwidget)
        self.receiveChangeBtn.setObjectName(u"receiveChangeBtn")
        self.receiveChangeBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"../../assets/icons/play-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.receiveChangeBtn.setIcon(icon2)
        self.receiveChangeBtn.setCheckable(False)
        self.receiveChangeBtn.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.receiveChangeBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.infoBtn = QPushButton(self.centralwidget)
        self.infoBtn.setObjectName(u"infoBtn")
        icon3 = QIcon()
        icon3.addFile(u"../../assets/icons/info-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon3)

        self.horizontalLayout.addWidget(self.infoBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.signalLw = QListWidget(self.centralwidget)
        self.signalLw.setObjectName(u"signalLw")

        self.verticalLayout_2.addWidget(self.signalLw)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.addCommandBtn = QPushButton(self.centralwidget)
        self.addCommandBtn.setObjectName(u"addCommandBtn")
        icon4 = QIcon()
        icon4.addFile(u"../../assets/icons/plus-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addCommandBtn.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.addCommandBtn)

        self.saveCommandBtn = QPushButton(self.centralwidget)
        self.saveCommandBtn.setObjectName(u"saveCommandBtn")
        icon5 = QIcon()
        icon5.addFile(u"../../assets/icons/save-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveCommandBtn.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.saveCommandBtn)

        self.deleteCommandBtn = QPushButton(self.centralwidget)
        self.deleteCommandBtn.setObjectName(u"deleteCommandBtn")
        icon6 = QIcon()
        icon6.addFile(u"../../assets/icons/trash-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteCommandBtn.setIcon(icon6)

        self.horizontalLayout_4.addWidget(self.deleteCommandBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.selectedCommandLayout = QVBoxLayout()
        self.selectedCommandLayout.setObjectName(u"selectedCommandLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.selectedCommandLayout.addWidget(self.label_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.signalCodeLe = QLineEdit(self.centralwidget)
        self.signalCodeLe.setObjectName(u"signalCodeLe")

        self.horizontalLayout_5.addWidget(self.signalCodeLe)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 3)

        self.selectedCommandLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.actionSelectCmbx = QComboBox(self.centralwidget)
        self.actionSelectCmbx.setObjectName(u"actionSelectCmbx")
        self.actionSelectCmbx.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.actionSelectCmbx)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)

        self.selectedCommandLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.selectedCommandLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.logTe = QTextEdit(self.centralwidget)
        self.logTe.setObjectName(u"logTe")
        self.logTe.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.logTe)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 909, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Remote IR", None))
        self.updatePortListAct.setText(QCoreApplication.translate("MainWindow", u"update port list", None))
#if QT_CONFIG(tooltip)
        self.updatePortListBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Refresh port list", None))
#endif // QT_CONFIG(tooltip)
        self.updatePortListBtn.setText("")
#if QT_CONFIG(tooltip)
        self.serialPortCmbx.setToolTip(QCoreApplication.translate("MainWindow", u"Select port", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.serialPortCmbx.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.serialPortCmbx.setCurrentText("")
        self.serialPortCmbx.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.serialRateLe.setToolTip(QCoreApplication.translate("MainWindow", u"Serial port speed", None))
#endif // QT_CONFIG(tooltip)
        self.serialRateLe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Serial port rate", None))
#if QT_CONFIG(tooltip)
        self.receiveChangeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Start/Stop port listening", None))
#endif // QT_CONFIG(tooltip)
        self.receiveChangeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"About programm", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bound signals:", None))
#if QT_CONFIG(tooltip)
        self.signalLw.setToolTip(QCoreApplication.translate("MainWindow", u"All processed signals", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.addCommandBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Add command", None))
#endif // QT_CONFIG(tooltip)
        self.addCommandBtn.setText("")
#if QT_CONFIG(tooltip)
        self.saveCommandBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Save selected command", None))
#endif // QT_CONFIG(tooltip)
        self.saveCommandBtn.setText("")
#if QT_CONFIG(tooltip)
        self.deleteCommandBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Delete selected command", None))
#endif // QT_CONFIG(tooltip)
        self.deleteCommandBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Selected signal:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Code", None))
#if QT_CONFIG(tooltip)
        self.signalCodeLe.setToolTip(QCoreApplication.translate("MainWindow", u"Signal code from port", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select action", None))
#if QT_CONFIG(tooltip)
        self.actionSelectCmbx.setToolTip(QCoreApplication.translate("MainWindow", u"Available actions", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"log:", None))
#if QT_CONFIG(tooltip)
        self.logTe.setToolTip(QCoreApplication.translate("MainWindow", u"Actions log", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

