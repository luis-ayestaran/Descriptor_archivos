# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventana(object):
    def setupUi(self, ventana):
        ventana.setObjectName("ventana")
        ventana.setEnabled(True)
        ventana.resize(800, 618)
        ventana.setAutoFillBackground(False)
        ventana.setStyleSheet("#ventana{\n"
"        background-color:rgb(102, 102, 102);\n"
"    }\n"
" #query1{\n"
"background-color:#55ff7f;\n"
"}\n"
"QPushButton{\n"
"        border-radius: 4px;\n"
"        color: #fff;\n"
"        font-family: \'Roboto\';\n"
"        font-size: 17px;\n"
"        \n"
"    }\n"
"QTextEdit{\n"
"border - radius: 15px;\n"
"color: #eee;\n"
"padding: 10px;\n"
"}\n"
"")
        self.verticalLayoutWidget = QtWidgets.QWidget(ventana)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 90, 181, 123))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setObjectName("Layout")
        self.textQuery = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textQuery.setEnabled(False)
        self.textQuery.setStyleSheet("background-color:rgb(159, 159, 159);\n"
"border- radius: 10px;\n"
"border: 3px solid;\n"
"\n"
"\n"
"")
        self.textQuery.setTabStopDistance(81.0)
        self.textQuery.setObjectName("textQuery")
        self.Layout.addWidget(self.textQuery)
        self.query1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.query1.setEnabled(True)
        self.query1.setStyleSheet("")
        self.query1.setObjectName("query1")
        self.Layout.addWidget(self.query1)
        self.gridLayoutWidget = QtWidgets.QWidget(ventana)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 80, 521, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.layout_r = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.layout_r.setContentsMargins(0, 0, 0, 0)
        self.layout_r.setObjectName("layout_r")
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 479))
        self.textEdit.setStyleSheet("background-color: rgb(122, 122, 122);")
        self.textEdit.setObjectName("textEdit")
        self.layout_r.addWidget(self.textEdit, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(ventana)
        self.label.setGeometry(QtCore.QRect(410, 40, 141, 36))
        self.label.setStyleSheet("#label{\n"
"font-size: 30px;\n"
"color: #212121;\n"
"}")
        self.label.setObjectName("label")

        self.retranslateUi(ventana)
        QtCore.QMetaObject.connectSlotsByName(ventana)

    def retranslateUi(self, ventana):
        _translate = QtCore.QCoreApplication.translate
        ventana.setWindowTitle(_translate("ventana", "ProyectoDB"))
        self.textQuery.setHtml(_translate("ventana", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff; background-color:#1e1e1e;\">SELECT first_name,salary<br />&quot;FROM&quot; EMPLOYEES<br />WHERE salary BETWEEN 10000 AND 15000</span></p></body></html>"))
        self.query1.setText(_translate("ventana", "Realizar Query"))
        self.label.setToolTip(_translate("ventana", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setWhatsThis(_translate("ventana", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("ventana", "Resultado"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = QtWidgets.QDialog()
    ui = Ui_ventana()
    ui.setupUi(ventana)
    ventana.show()
    sys.exit(app.exec_())
