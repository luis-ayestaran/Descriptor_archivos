import pandas as pd
import os
import sys
from front_ui import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow,Ui_ventana):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)        
        self.query1.clicked.connect(self.actualizar)
    def actualizar(self):
        relt=desriptor_arch()
        relt=str(relt)  
        self.textEdit.setText(relt)


def TEM_ARCH():
    arch=open('RESULT_SELECT.csv','w')
    arch.close()
    arch1=open('RESULT_PROY.csv','w')
    arch1.close()

def desriptor_arch():
    arch=open("EMPLOYEES.txt","r")
    tupla=arch.read()
    i=0
    cont=0
    tem=''
    Nam_arch=''
    Atri=''
    i=0
    while tupla[i]!=',':
        Nam_arch+=tupla[i]
        i=i+1
    i=i+1
    while tupla[i]!='\n':
        while tupla[i]!=',':
            Atri+=tupla[i]
            i=i+1
        Atri+=tupla[i]
        i=i+1
        while cont<2:
            while tupla[i]!= ',':
                if cont>0:
                    tem+=tupla[i]
                i=i+1
            cont=cont+1
            i=i+1
        tem+=','
        cont=0
    cont=0
    Atri+=tupla[i]
          
    def TUPLAS(aux1,Atri):
        aux=''
        cont=0
        j=0
        tam=0
        while aux1[j]!='\n':
            while aux1[j]==' ':
                j=j+1
            while tem[cont]!=',':
                aux+=tem[cont]
                cont=cont+1
            tam=int(aux)
            cont=cont+1
            while j<=tam:
                Atri+=aux1[j]
                j=j+1
            Atri+=','
            aux=''
        Atri+=aux1[j]
        return Atri

    arch.close()
    arch=open("EMPLOYEES.txt","r")
    tuplas=arch.readlines()
    i=1
    j1=(len(tuplas))
    Atri=TUPLAS(tuplas[3],Atri)
    while i<j1-1:
        Atri=TUPLAS(tuplas[i],Atri)
        i=i+1
    arch2=open(Nam_arch+'.csv','w')
    arch2.write(Atri)
    arch2.close()
    arch.close()
    import pandas as pd
    import os   
    emp='EMPLOYEES'
    datos=pd.read_csv(emp+'.csv')
    datos2=datos[(datos['SALARY']>=10000 )& (datos['SALARY']<=15000)]
    #print(datos2.reset_index().iloc[:,[2,8]])
    df=pd.DataFrame(datos2)
    df1=pd.DataFrame(datos2.reset_index().iloc[:,[2,8]])
    TEM_ARCH()
    df.to_csv('RESULT_SELECT.csv',header=True,index=False)
    df1.to_csv('RESULT_PROY.csv',header=True,index=False)
    return df1
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()