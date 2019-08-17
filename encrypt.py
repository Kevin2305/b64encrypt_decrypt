#!/usr/bin/env python
# coding: utf-8
import base64
import sys
import logging
from PyQt5 import QtWidgets
import encryptui
dfmt="%Y-%m-%d %H:%M:%S"
fmt="%(asctime)s %(levelname)s : %(message)s"
level=logging.WARN

def ToEncry(aw):
    try:
        miwen=base64.b64encode(aw.encode('utf-8')).decode('utf-8')
    except Exception:
        logging.warning("ming wen cuo le!")

def ToPlainText(bw):
    try:
        mingwen=base64.b64decode(bw).decode('utf-8')
    except Exception:
        logging.warning("mi wen cuo le!")

class MyWidget(QtWidgets.QWidget,encryptui.Ui_Form):
    def __init__(self,parent=None):
        super(MyWidget,self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    logging.basicConfig(filename="log.log",level=level,format=fmt,datefmt=dfmt)
    app =  QtWidgets.QApplication(sys.argv)
    mf=MyWidget()
    mf.show()
    sys.exit(app.exec_())

