#!/usr/bin/env python
# coding: utf-8
import sys
import b64ui
from PyQt5 import QtWidgets

class MyWidget(QtWidgets.QWidget,b64ui.Ui_Form):
    def __init__(self,parent=None):
        super(MyWidget,self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    
    app =  QtWidgets.QApplication(sys.argv)
    mf=MyWidget()
    mf.show()
    sys.exit(app.exec_())

