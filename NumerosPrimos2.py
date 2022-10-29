import pandas as pd
import numpy as np
import matplotlib as plt
import random

print("Este programa trata sobre numeros primos.")

numero = int(input("Ingrese un numero: "))
numeros_primos = []
contador = 0


opcion = int(input("Marque 1 para saber si el numero " + str(numero) + " es primo, o marque 2 si quiere saber todos los numeros primos que hay hasta el " + str(numero) + ": "))
if ((opcion==1) or (opcion==2)):
    if(opcion==1):
        for i in range(1,numero+1,1):
            if((numero%i==0)&(i!=1)&(i!=numero)):
                print("El numero no es numero primo, el numero es divisible por " + str(i))
                break
            if(numero==i):
                print("El numero " + str(numero) + " es primo.")

    if(opcion==2):
        for i in range(1,numero+1,1):
            for u in range(1,i+1,1):
                if ((i%u==0)&(u!=1)&(u!=i)):
                    break
                if(i==u):
                    numeros_primos.append(i)
        
        print("Los numeros primos que hay desde el 1 hasta el " + str(numero) + " son: ", numeros_primos, "(Son ", len(numeros_primos), " numeros primos)")

print("Grafica con numeros primos.\n")

print(numeros_primos)
