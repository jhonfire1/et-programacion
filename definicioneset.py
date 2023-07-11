#archivo de funciones
from ast import If, Return
from glob import iglob
from operator import truediv
import numpy as np 
import os
def llenar(depa): #esta funcion me llena las matrices
    mensaje="PISO"
    mensaje2="    Tipo Habitacion"
    mensaje3=""
    p=1
    for i in range(11):
        if(i>0):
                depa[i]=p
                p+=1
        else:
            depa[i]=mensaje
        for j in range(5):
            if(i==0 and j ==1):
                depa[i,j]=mensaje2
            if(i==0 and j ==2):
                depa[i,j]=mensaje3
            if(i==0 and j ==3):
                depa[i,j]=mensaje3
            if(i==0 and j ==4):
                depa[i,j]=mensaje3
            if(i>0):
                if(j==1):
                    depa[i,j]='A'   
                elif(j==2):
                    depa[i,j]='B'
                elif(j==3):
                    depa[i,j]='C'
                elif(j==4):
                    depa[i,j]='D'
def validaOp():
    pp=0
    while(True):
        try:
            pp=int(input("   Elija opción: "))
            if(pp>=1 and pp<=5):
                break
            else:
                print("Debe ingresar una opción entre 1 y 5")
        except ValueError:
            print("Debe ingresar un número entero")
    return pp 

def departamentos(depa,ruts):
    piso=0
    tipo=""
    os.system("cls")
    for i in range(11):
        print("\n") 
        for j in range(5):
            if(j==0):
                print("\t",depa[i,j], end="        ")
            else:
                print("\t",depa[i,j], end="   ")
    print("\n\n")
    hola=0
    while(True):
        try:
            piso=int(input("ingresa el piso de la habitacion: "))
            if(piso > 10 or piso <= 0):
                print("ingresa desde 1 hasta 10 ")
            else:
                break
        except ValueError:
            print("error de digitacion")
    os.system("cls")
    print("Tipo A, 3.800 UF ")
    print("Tipo B, 3.000 UF")
    print("Tipo C, 2.800 UF ")
    print("Tipo D, 3.500 UF ")
    while(True):
        try:
            tipo=str(input("ingresa el tipo de habitacion: ")).upper()
            if(tipo != 'A' and tipo != 'B' and tipo != 'C' and tipo != 'D'):
                print("ingresa tipo desde A a D")
            else:
                break
        except ValueError:
            print("error de digitacion")
    os.system("cls")
    while(True):
                    while(True):
                        try:
                            rut=int(input("ingrese Rut, debe tener 8 digitos minimo: "))
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
                            print("El rut ya existe y no se puede agregar")
                        else:
                            ruts.append(rut)
                            break
                    else:
                        ruts.append(rut)
                        break
    for i in range(11):
        for j in range(1):
            if(piso==depa[i,j]):
                    hola=depa[i,j]
    for i in range(11):
        for j in range(5):
            if(tipo==depa[piso,j]):
                depa[piso,j]='X'
    os.system("cls")
    print("la operacion de compra se ha realizado correctamente :)")
    os.system("cls")
    return tipo

def mostrarDisponibles(depa):
    os.system("cls")
    for i in range(11):
        print("\n") 
        for j in range(5):
            if(j==0):
                print("\t",depa[i,j], end="        ")
            else:
                print("\t",depa[i,j], end="   ")
    print("\n\n")

def rutes(rut):
    rut.sort()
    print(rut)

def dinero(depa):
    tipo=1
    for i in range(2):
            for j in range(5):
                if(tipo==depa[i,j]):
                    print(depa[i,j])
                    os.system("pause")
