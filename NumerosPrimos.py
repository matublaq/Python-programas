print("Este es un programa que te hallara todos los numeros primos que hay desde el 3 hasta el numero que elijas.")

numero = int(input("Escriba hasta que numero quieres saber: "))

contador0 = 0
contador = 0

for i in range(3,numero+1,1):
  for u in range(1,i+1,1):
    if(i%u == 0):
      contador += 1
      if(i == u):
        if(contador == 2):
          print("El numero ", i, " es primo.")
          contador0 += 1
        else:
          contador = 0

print("Hay "+str(contador0)+" numeros primos desde 3 hasta "+str(numero)+".")