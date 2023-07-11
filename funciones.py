import os
import numpy as np
def llenarmatriz(piso,tipo):
    p=1
    for i in range(10):
            for j in range(4):
                tipo[i,j]=p
                piso[i,j]=p
                p+=1

def validop():
    op=0
    while(True):
        try:
            op=int(input('ELIJA OPCIÓN:'))
            if (op>=1 and op <=5):
                break
            else:
                print('debe ingresar una opción entre 1 y 5')
        except ValueError:
            print('debe ingresar un número entero')
    return op

def mostrarDisponibles(piso,tipo):
    os.system('cls')
    for i in range(10):
        print('\n') #salto de linea
        for j in range(4):
            if(j==1 or j==5):
                print('\t',piso[i,j], end="  ")
            else:
                print('\t',tipo[i,j], end="  ")
    print('\n\n')


def validaPiso():
    piso=0
    while(True):
        try:
            piso=int(input(" Ingrese número de asiento entre 1-40: "))
            if(piso>=1 and piso<=40):
                break
            else:
                print("Error debe ingresar un asiento entre 1 y 40")
        except ValueError:
            print("Debe ser un número entero")
    return piso
def comprarDep(piso,tipo,ruts):
    for i in range(13):
        for j in range(8):
            if(piso==tipo[i,j]):
                while(True):
                    while(True):
                        try:
                            rut=int(input("Rut debe tener 8 digitos minimo "))
                            if(rut<9999999):
                                print("Error, debe tener 8 dígitos mínimo")
                            else:
                                break
                        except ValueError:
                            print("Debe ser número entero")
                    if(len(ruts)>0): 
                        sw=0
                        for y in range(len(ruts)):
                            if(rut==ruts[y]):
                                sw=1
                        if(sw==1):
                            print("El rut ya existe y no se puede agregar el pasajero")
                        else:
                            ruts.append(rut)
                            break
                    else:
                        ruts.append(rut)
                        break
                piso[i,j]=0 #cambio el número de asiento a cero porque vendo el asiento!!!!!!!!
                if(i>=0 and i<=2):
                    pago+=3800
                elif(i>=3 and i<=7):
                    pago+=3000
                elif(i>=11 and i<=12):
                    pago+=2800
                elif(i>=4):
                    pago+=3000