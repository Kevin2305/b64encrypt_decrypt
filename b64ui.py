# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\b64encrypt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import base64
import logging
dfmt="%Y-%m-%d %H:%M:%S"
fmt="%(asctime)s %(levelname)s : %(message)s"
level=logging.WARN

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(658, 417)
        self.encryped_edit = QtWidgets.QLineEdit(Form)
        self.encryped_edit.setGeometry(QtCore.QRect(80, 320, 511, 20))
        self.encryped_edit.setObjectName("encryped_edit")
        self.plain_edit = QtWidgets.QLineEdit(Form)
        self.plain_edit.setGeometry(QtCore.QRect(80, 130, 511, 20))
        self.plain_edit.setObjectName("plain_edit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 240, 371, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.bt_to_plain = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.bt_to_plain.setObjectName("bt_to_plain")
        self.horizontalLayout.addWidget(self.bt_to_plain)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, 50, 371, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.bt_to_encrypt = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.bt_to_encrypt.setObjectName("bt_to_encrypt")
        self.horizontalLayout_2.addWidget(self.bt_to_encrypt)

        self.retranslateUi(Form)
        self.bt_to_encrypt.clicked.connect(self.ToEncry)
        self.bt_to_plain.clicked.connect(self.ToPlainText)
        QtCore.QMetaObject.connectSlotsByName(Form)

        logging.basicConfig(filename="log.log",level=level,format=fmt,datefmt=dfmt)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Base64 Convertor"))
        self.label_2.setText(_translate("Form", "Base64 Text"))
        self.bt_to_plain.setText(_translate("Form", "To Plain Text"))
        self.label.setText(_translate("Form", "Plain Text"))
        self.bt_to_encrypt.setText(_translate("Form", "To Base64 Text"))

    def ToEncry(self):
        try:
            aw=None
            aw=self.plain_edit.text()
            if len(aw)>0:
                miwen=base64.b64encode(aw.encode('utf-8')).decode('utf-8')
                self.encryped_edit.setText(miwen)
        except Exception as e:
            logging.warning("encrypt cuo le!")
            logging.warning(e)

    def ToPlainText(self):
        try:
            bw=None
            bw=self.encryped_edit.text()
            if len(bw)>0:
                mingwen=base64.b64decode(bw).decode('utf-8')
                self.plain_edit.setText(mingwen)
        except Exception as e:
            logging.warning("decrypt cuo le!")
            logging.warning(e)