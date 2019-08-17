# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'b64encrypt.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

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
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Encrypted Text"))
        self.bt_to_plain.setText(_translate("Form", "To Plain Text"))
        self.label.setText(_translate("Form", "Plain Text"))
        self.bt_to_encrypt.setText(_translate("Form", "To Encrypted Text"))

