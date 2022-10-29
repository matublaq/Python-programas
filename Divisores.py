print("Te dire todos los divisores del numero que quieras.")

numero = int(input("Indique los divisores de que numero quiere saber: "))
contador = 0
for i in range(1,numero+1,1):
    if (numero%i == 0):
        print(i)
        contador += 1
print("El numero ", numero, " tiene ", contador, " divisores.")