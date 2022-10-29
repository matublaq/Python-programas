import pandas as pd
import numpy as np
import matplotlib as plt
import random

def Factorial(Facto, Numero, SumaFactorial):
    for i in range(1, Numero, 1):
        SumaFactorial += Facto
        Facto = 1
        for u in range(1, Numero, 1):
            Facto *= u
        Numero -= 1
    return SumaFactorial

Numero = int(input("Hasta que numero queres ver la suma de factoriales?\n"))
SumaFactorial = 1
Facto = 1
Factorial(Facto, Numero, SumaFactorial)
print("La suma de factoriales es: ", SumaFactorial)