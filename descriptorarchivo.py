import os
import sys

def where(listaCampo, totalTupla, archivoTupla):
    propiedadTabla = archivoTupla[0].split(",")
    descripcionTabla = [propiedadTabla[0]]
    posicionLista = 1
    for x in range(1, len(propiedadTabla), 3):
        descripcionTabla.append([propiedadTabla[x]])
        descripcionTabla[posicionLista].append(propiedadTabla[x + 1])
        descripcionTabla[posicionLista].append(propiedadTabla[x + 2])
        posicionLista = posicionLista + 1
    longitudListaCampo = len(listaCampo)
    print("\n\n\nSQL> ", end = "")
    for x in range(0, longitudListaCampo):
        if x != (longitudListaCampo - 1):
            print(listaCampo[x], ", ", end = "", sep = (''))
        else:
            print(listaCampo[x])
    print("FROM employees")
    print("WHERE salary>=1500 and salary<=3000\n")
    for x in range(0, longitudListaCampo):
        print(listaCampo[x], " ", end = "", sep = (''))
    print()
    band = False
    for x in range(1, totalTupla):
        for y in range(1, len(descripcionTabla)):
            for z in range(0, len(listaCampo)):
                if listaCampo[z] == descripcionTabla[y][0]:
                    salario = int(archivoTupla[x][114 - 1 : 121])
                    if salario >= 1500 and salario <= 3000:
                        band = True
                        letrero = archivoTupla[x][int(descripcionTabla[y][1]):int(descripcionTabla[y][2])]
                        print(letrero, end = "", sep = (''))
        if band:
            band = False
            print()
            #query.append(letrero)


def select(listaCampo, totalTupla, archivoTupla):
    propiedadTabla = archivoTupla[0].split(",")
    descripcionTabla = [propiedadTabla[0]]
    posicionLista = 1
    for x in range(1, len(propiedadTabla), 3):
        descripcionTabla.append([propiedadTabla[x]])
        descripcionTabla[posicionLista].append(propiedadTabla[x + 1])
        descripcionTabla[posicionLista].append(propiedadTabla[x + 2])
        posicionLista = posicionLista + 1
    longitudListaCampo = len(listaCampo)
    print("\n\n\nSQL> ", end = "")
    for x in range(0, longitudListaCampo):
        if x != (longitudListaCampo - 1):
            print(listaCampo[x], ", ", end = "", sep = (''))
        else:
            print(listaCampo[x])
    print("FROM employees\n")
    for x in range(0, longitudListaCampo):
        print(listaCampo[x], " ", end = "", sep = (''))
    print()
    for x in range(1, totalTupla):
        for y in range(1, len(descripcionTabla)):
            for z in range(0, len(listaCampo)):
                if listaCampo[z] == descripcionTabla[y][0]:
                    letrero = archivoTupla[x][int(descripcionTabla[y][1]):int(descripcionTabla[y][2])]
                    print(letrero, end = "")
        #input()
        print()

if __name__ == "__main__":
    try:
        archivo = sys.argv[1]
        ubicacion = os.getcwd()
    except Exception as e:
        print("No pasaste un archivo como parámetro.")
    if os.path.isfile(archivo):
        if os.access(archivo, os.F_OK):
            if os.access(archivo, os.R_OK):
                if os.access(archivo, os.W_OK):
                    with open(archivo, encoding = "utf8", errors = "ignore") as file:
                        lineas = file.readlines()
                    file.close()
                    archivoSeparadoTupla = [] # lA PRIMER FILA ES PARA DECRIPCION DEL ARCHIVO
                    archivoSeparadoTupla.append(lineas[0].split(','))
                    totalTupla = len(lineas)
                    print("SQL> SELECT * FROM employees")
                    print("|employees_id|     first_name     |     last_name     |email|phone_number|hire_date|job_id|salary|commission_pct|manager_id|department_id")
                    for x in range(1, totalTupla):
                        archivoSeparadoTupla.append([lineas[x][0:6]])
                        cadena = ""
                        longitudPropiedadInicial = 2
                        longitudPropiedadFinal = 3
                        try:
                            while True:
                                posicionInicialTupla = int(archivoSeparadoTupla[0][longitudPropiedadInicial])
                                posicionFinalTupla = int(archivoSeparadoTupla[0][longitudPropiedadFinal])
                                print(lineas[x][posicionInicialTupla - 1:posicionFinalTupla], end = "")
                                longitudPropiedadInicial = longitudPropiedadInicial + 3
                                longitudPropiedadFinal = longitudPropiedadFinal + 3
                        except Exception as e:
                            print()
                            #input()

                    select(["employees_id", "phone_number", "salary"], totalTupla, lineas)
                    where(["employees_id", "phone_number", "salary"], totalTupla, lineas)
#201623159Ismael      Sosa      Gutierrez
