# - * - coding: utf - 8 -* -

# Form implementation generated from reading ui file 'descriptor_archivos.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import os
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 700)
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueLT Pro 55 Roman")
        font.setPointSize(14)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("7MO SEMESTRE / BASES DE DATOS / PROYECTO / icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(" * {\n"
"    background - color: #333;\n"
"}\n"
"\n"
"QLabel {\n"
"    font - family: \"HelveticaNeueLT Pro 55 Roman\";\n"
"    font - size: 20px;\n"
"    font - weight: bold;\n"
"    color: white;\n"
"    qproperty - alignment: AlignCenter;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font - family: \"HelveticaNeueLT Pro 55 Roman\";\n"
"    font - weight: bold;\n"
"    font - size: 20px;\n"
"    background - color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #20e1a7, stop: 1  #08beb2);    \n"
"    color: black;\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"    background - color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #20e1a7, stop: 1  #08beb2);    \n"
"    color: black;\n"
"}\n"
"\n"
" QPushButton:pressed {\n"
"    background - color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #08beb2, stop: 1 #20e1a7 );\n"
" }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnDoQuery = QtWidgets.QPushButton(self.centralwidget)
        self.btnDoQuery.setGeometry(QtCore.QRect(70, 410, 200, 40))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueLT Pro 55 Roman")
        font.setPointSize( - 1)
        font.setBold(True)
        font.setWeight(75)
        self.btnDoQuery.setFont(font)
        self.btnDoQuery.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDoQuery.setToolTip("")
        self.btnDoQuery.setStyleSheet("QPushButton {\n"
"    border - radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" }\n"
"")
        self.btnDoQuery.setAutoDefault(False)
        self.btnDoQuery.setFlat(False)
        self.btnDoQuery.setObjectName("btnDoQuery")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 60, 301, 261))
        self.frame.setStyleSheet("background - color: #444;\n"
"border - radius: 20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(2)
        self.frame.setObjectName("frame")
        self.lblQueryContent = QtWidgets.QLabel(self.frame)
        self.lblQueryContent.setGeometry(QtCore.QRect(20, 20, 271, 51))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize( - 1)
        font.setBold(False)
        font.setWeight(50)
        self.lblQueryContent.setFont(font)
        self.lblQueryContent.setStyleSheet("font - family: \"SF Pro Display\";\n"
"font - size: 13px;\n"
"font - weight: normal;\n"
"color: #eee;\n"
"qproperty - alignment: AlignLeft;")
        self.lblQueryContent.setObjectName("lblQueryContent")
        self.lblQueryTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblQueryTitle.setGeometry(QtCore.QRect(20, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueLT Pro 55 Roman")
        font.setPointSize( - 1)
        font.setBold(True)
        font.setWeight(75)
        self.lblQueryTitle.setFont(font)
        self.lblQueryTitle.setStyleSheet("font - family: \"HelveticaNeueLT Pro 55 Roman\";\n"
"font - size: 20px;\n"
"font - weight: bold;\n"
"color: white;\n"
"qproperty - alignment: AlignCenter;")
        self.lblQueryTitle.setObjectName("lblQueryTitle")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(350, 60, 921, 571))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize( - 1)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background - color: #666;\n"
"border - radius: 20px;\n"
"padding: 10px;\n"
"color: #eee;\n"
"font - family: \"SF Pro Display\";\n"
"font - size: 16px;")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.lblResults = QtWidgets.QLabel(self.centralwidget)
        self.lblResults.setGeometry(QtCore.QRect(350, 30, 111, 16))
        self.lblResults.setStyleSheet("font - family: \"HelveticaNeueLT Pro 55 Roman\";\n"
"font - size: 20px;\n"
"font - weight: bold;\n"
"color: white;\n"
"qproperty - alignment: AlignCenter;")
        self.lblResults.setObjectName("lblResults")
        self.btnSelectQuery = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelectQuery.setGeometry(QtCore.QRect(120, 350, 100, 40))
        self.btnSelectQuery.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSelectQuery.setStyleSheet("QPushButton {\n"
"    border - radius: 20px;\n"
"    border - style: solid;\n"
"    border - width: 1px;\n"
"    border - color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #08beb2, stop: 1     #20e1a7 );    \n"
"    color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #08beb2, stop: 1         #20e1a7 ); \n"
"    background - color: transparent;\n"
"    font - size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background - color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #20e1a7, stop: 1  #08beb2);    \n"
"    color: black;\n"
"}\n"
"\n"
" QPushButton:pressed {\n"
"    background - color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #08beb2, stop: 1 #20e1a7 );\n"
"    border - radius: 20px;\n"
" }")
        self.btnSelectQuery.setObjectName("btnSelectQuery")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Descriptor de archivos"))
        self.btnDoQuery.setText(_translate("MainWindow", "Realizar consulta"))
        self.lblQueryContent.setText(_translate("MainWindow", "SELECT first_name, salary\n"
"FROM EMPLOYEES\n"
"WHERE salary BETWEEN 10000 AND 15000;"))
        self.lblQueryTitle.setText(_translate("MainWindow", "Query"))
        self.textEdit.setHtml(_translate("MainWindow", " < !DOCTYPE HTML PUBLIC \" - / / W3C // DTD HTML 4.0 // EN\" \"http: // www.w3.org / TR / REC - html40 / strict.dtd\" > \n"
" < html >< head >< meta name = \"qrichtext\" content = \"1\" / > < style type = \"text / css\" > \n"
"p, li { white - space: pre - wrap; }\n"
" </ style > < / head >< body style = \" font - family:\'SF Pro Display\'; font - size:16px; font - weight:400; font - style:normal;\" > \n"
" < p style = \" - qt - paragraph - type:empty; margin - top:0px; margin - bottom:0px; margin - left:0px; margin - right:0px; - qt - block - indent:0; text - indent:0px; font - family:\'MS Shell Dlg 2\'; font - size:8.25pt;\" >< br / >< / p > < / body > < / html > "))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Aqu irn apareciendo los resultados. Vamos, realiza una query!"))
        self.lblResults.setText(_translate("MainWindow", "Resultados"))
        self.btnSelectQuery.setText(_translate("MainWindow", "SELECT"))

def seleccionTuplaTodas(listaTupla, atributo, caracteristicaAtributo):
    registros = atributo
    atributoRango = listaTupla[0].split(',') 
    atributoRango.remove('')
    posicionLista = 0
    listaPosicionAtributo = []
    for x in range(2, len(atributoRango), 3): # Hace una lista con las posiciones donde se encuentran los atributos, el rango en el archivo
        listaPosicionAtributo.append([])
        listaPosicionAtributo[posicionLista].append(atributoRango[x])
        listaPosicionAtributo[posicionLista].append(atributoRango[x + 1])
        posicionLista = posicionLista + 1
    longitudListaTupla = len(listaTupla)
    for x in range(1, longitudListaTupla): # Une todas las tuplas en una cadena para que sea enviada a un CSV
        for rango in listaPosicionAtributo:
            cadena = listaTupla[x][int(rango[0]):int(rango[1]) + 1]
            registros += cadena.replace(' ', '')
            registros += ","
        registros += "\n"
    return registros

def OPC_1():
    print('#Resultado:')
    emp = 'EMPLOYEES'
    datos = pd.read_csv(emp + '.csv ')
    datos2 = datos[(datos['SALARY'] >= 10000 ) & (datos['SALARY'] <= 15000)]
    print(datos2.reset_index().iloc[:,[2,8]])
    df1 = pd.DataFrame(datos2.reset_index().iloc[:,[2,8]])
    df1.to_csv('RESULT_PROY.csv',header = True,index = False)
    input()

def OPC_2():
    emp = 'EMPLOYEES'
    datos = pd.read_csv(emp + '.csv')
    datos2 = datos.iloc[0:-1]
    print(datos2)
    df = pd.DataFrame(datos2)
    df.to_csv('RESULT_SELECT.csv',header = True,index = False)
    input()

def OPC_3():
    emp = 'EMPLOYEES'
    datos = pd.read_csv(emp + '.csv')
    datos2 = datos.iloc[:, [1, 4, 6]]
    print(datos2)
    df = pd.DataFrame(datos2)
    df.to_csv('RESULT_SELECT2.csv',header = True,index = False)
    input()

def MENU():
    OPC = 1
    while OPC != 0:
        os.system("cls")
        print('\n\tMENU\n1.OPERACIN 1:\n\tSELECT FIRST_NAME,SALARY\n\tFROM EMPLOYEES\n\tWHERE SALARY BETWEEN 10000 AND 15000; \n2.- SELECT * FROM EMPLOYEES\n3.- SELECT FIRST_NAME, PHONE_NUMBER, JOB_ID FROM EMPLOYEES')
        print('0.SALIR\n')
        OPC = int(input('Selecione una Opcion:'))
        os.system("cls")
        if OPC == 1:
            OPC_1()
        elif OPC == 2:
            OPC_2()
        elif OPC == 3:
            OPC_3()
        if OPC == 0:
            os.remove('RESULT_SELECT.csv')
            os.remove('RESULT_SELECT2.csv')
            os.remove('RESULT_PROY.csv')
            os.remove('EMPLOYEES.csv')
            os.system("cls")


if __name__ == "__main__":
    arch = open("EMPLOYEES.txt","r") 
    tupla = arch.read() # Todo el archivo lo guarda en una cadena
    arch.close()
    tuplas = tupla.split('\n') # Archivo convertido en una lista
    atributoTabla = '' # Cadena que contiene los atributos de la tabla
    i = tupla.find(',') + 1 # En esta posicion empieza el primer atributo de la tabla
    nombreArchivo = tupla[:i-1] # Nombre de la tabla
    listaAtributo = tuplas[0].split(',') # La primera linea la convierto en una lista
    listaAtributo.remove('') 
    for x in range(1, len(listaAtributo), 3): # En una cadena se anaden todos los atributos a exepcion de su longitud
        atributoTabla += listaAtributo[x]
        atributoTabla += ','
    atributoTabla += "\n"
    registros = seleccionTuplaTodas(tuplas, atributoTabla, listaAtributo)
    arch2 = open(nombreArchivo + '.csv','w')
    arch2.write(registros)
    arch2.close()
    MENU()    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
