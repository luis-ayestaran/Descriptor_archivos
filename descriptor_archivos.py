# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:36:47 2019

@author: carlos efraim
"""
arch=open("EMPLOYEES.txt","r")
tupla=arch.read()
i = 0
cont = 0
tem = ''
Nam_arch = ''
Atri=''
j=0
aux = ''
tam = 0
i=0
flag=0
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
    #print(Atri)
    return Atri
arch.close()
arch=open("EMPLOYEES.txt","r")
#print(len(arch.readlines()))
tuplas=arch.readlines()
#print(tuplas[1])
i=1
j1=(len(tuplas))
aux=''
Atri=TUPLAS(tuplas[3],Atri)
while i<j1-1:
    Atri=TUPLAS(tuplas[i],Atri)
    i=i+1
#print(Atri)
arch2=open(Nam_arch+'.csv','w')
arch2.write(Atri)
arch2.close()
arch.close()
#print (Nam_arch)
import pandas as pd
import os
def TEM_ARCH():
    arch=open('RESULT_SELECT.csv','w')
    arch.close()
    arch1=open('RESULT_PROY.csv','w')
    arch1.close()

def OPC_1():
    print('#Resultado:')
    emp='EMPLOYEES'
    datos=pd.read_csv(emp+'.csv')
    datos2=datos[(datos['SALARY']>=10000 )& (datos['SALARY']<=15000)]
    print(datos2.reset_index().iloc[:,[2,8]])
    df=pd.DataFrame(datos2)
    df1=pd.DataFrame(datos2.reset_index().iloc[:,[2,8]])
    TEM_ARCH()
    df.to_csv('RESULT_SELECT.csv',header=True,index=False)
    df1.to_csv('RESULT_PROY.csv',header=True,index=False)
    input()

#OPC_1()
def MENU():
    OPC=1
    while OPC !=0:
        os.system("cls")
        print('\n\tMENU\n1.OPERACIÓN 1:\n\tSELECT FIRST_NAME,SALARY\n\tFROM EMPLOYEES\n\tWHERE SALARY BETWEEN 10000 AND 15000;')
        print('0.SALIR\n')
        OPC=int(input('Selecione una Opcion:'))
        os.system("cls")
        if OPC==1:
            OPC_1()
        if OPC==0:
            TEM_ARCH()
            os.remove('RESULT_SELECT.csv')
            os.remove('RESULT_PROY.csv')
            os.remove('EMPLOYEES.csv')
            os.system("cls")
MENU()
