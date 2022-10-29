from ast import Return
from multiprocessing.resource_sharer import stop
import numpy as np
import pandas as pd
import random

def Lap_year(year):
    if(year%4 == 0):
        if((year%100 == 0)):
            if(year%400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def Lap_year2(year):
    if((year%4 == 0) and ((year%100 != 0) or (year%400 == 0))):
       return True
    else:
        return False
        
year = int(input("Write a year: "))
if(Lap_year(year)):
    print("The year is lap year.")
else:
    print("It's not lap year.")

if (Lap_year2(year)):
    print("The year is lap year.")
else:
    print("It's not lap year.")
