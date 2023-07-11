#programa principal
from cmath import e
import os
from unicodedata import numeric
import numpy as np 
import definicioneset as et 
depa=np.empty([11,5],type(object))
ruts=[] 
et.llenar(depa)
op=0
piso=0
tipo=''
rut=[]
i=0
while(op!=5):
    os.system("cls")
    print("          CASA FELIZ :)    ")
    print("     -------********-------     ")
    print(" 1.  comprar departamento ")
    print(" 2.  mostrar departamentos disponibles  ")
    print(" 3.  ver listado de compradores ")
    print(" 4.  mostrar ganancias totales ")
    print(" 5.  salir ")
    op=et.validaOp()
    if(op==1):
        et.departamentos(depa,ruts)
        i+=1
        os.system("pause")
    if(op==2):
        et.mostrarDisponibles(depa)
        os.system("pause")
    if(op==3):
        if (i > 0) :
            et.rutes(ruts)
            os.system("pause")
        else:
            print("aun no se han comprando departamentos")
            os.system("pause")
    if(op==4):
        print("no alncanze :(")