import os
import string
import numpy as np
import funciones as fn
tipo=np.empty([10,4],type)
piso=np.empty([10,4],type(int))
ruts=[]
fn.llenarmatriz(piso,tipo)
op=0
#debo recorrer la matriz pasando por la primera fila de la matriz y setearle el abcd
while (op!=6):
    os.system('cls')
    print('          CASA BONITA')
    print('       *******************') 
    print(' 1.    Comprar departamento')
    print(' 2.    Mostrar departamentos disponibles') 
    print(' 3.    Ver listado de compradores')
    print(' 4.    Mostrar ganancias totales') 
    print(' 5.    SALIR')
    op=fn.validop()
    if(op==1):
        fn.comprarDep(piso,tipo,ruts)
        valPiso=fn.validop
        os.system('pause')
    if (op==2):
        fn.mostrarDisponibles(piso,tipo)
        os.system('pause')
        