# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogInfo(object):
    def setupUi(self, DialogInfo):
        if not DialogInfo.objectName():
            DialogInfo.setObjectName(u"DialogInfo")
        DialogInfo.resize(480, 197)
        self.horizontalLayout = QHBoxLayout(DialogInfo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DialogInfo)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(DialogInfo)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(DialogInfo)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(DialogInfo)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(DialogInfo)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(DialogInfo)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setTextFormat(Qt.AutoText)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_6)

        self.label_7 = QLabel(DialogInfo)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(DialogInfo)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_2.addWidget(self.label_8)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_9 = QLabel(DialogInfo)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setTextFormat(Qt.MarkdownText)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_9)

        self.label_10 = QLabel(DialogInfo)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setTextFormat(Qt.MarkdownText)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(5, QFormLayout.FieldRole, self.verticalSpacer)


        self.horizontalLayout.addLayout(self.formLayout)


        self.retranslateUi(DialogInfo)

        QMetaObject.connectSlotsByName(DialogInfo)
    # setupUi

    def retranslateUi(self, DialogInfo):
        DialogInfo.setWindowTitle(QCoreApplication.translate("DialogInfo", u"About programm", None))
        self.label.setText(QCoreApplication.translate("DialogInfo", u"About:", None))
        self.label_2.setText(QCoreApplication.translate("DialogInfo", u"Version:", None))
        self.label_3.setText(QCoreApplication.translate("DialogInfo", u"Developer:", None))
        self.label_4.setText(QCoreApplication.translate("DialogInfo", u"Project GitHub:", None))
        self.label_5.setText(QCoreApplication.translate("DialogInfo", u"Resources used:", None))
        self.label_6.setText(QCoreApplication.translate("DialogInfo", u"This is a simple program for controlling a computer using Arduino and infrared.", None))
        self.label_7.setText(QCoreApplication.translate("DialogInfo", u"0.1.9", None))
        self.label_8.setText(QCoreApplication.translate("DialogInfo", u"<html><head/><body><p>Link to GitHub - <a href=\"https://github.com/donexdoc\"><span style=\" text-decoration: underline; color:#0000ff;\">donexdoc</span></a>. link to website - <a href=\"https://donex-project.ru/\"><span style=\" text-decoration: underline; color:#0000ff;\">https://donex-project.ru/</span></a>.</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("DialogInfo", u"<html><head/><body><p><a href=\"https://github.com/donexdoc/Remote-IR\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/donexdoc/Remote-IR</span></a></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("DialogInfo", u"<html><head/><body><p>App icon getted from FlatIcon:</p><p>Icons made by <a href=\"http://www.freepik.com\"><span style=\" text-decoration: underline; color:#0000ff;\">Freepik</span></a> from <a href=\"https://www.flaticon.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">www.flaticon.com</span></a></p><p>The icons used inside the app were taken from the <a href=\"https://fontawesome.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">https://fontawesome.com</span></a>.</p><p>\n"
"</p></body></html>", None))
    # retranslateUi

