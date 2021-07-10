import platform
import os

# funcion para con seguridad obtener un numero entero del usuario
def intInput(label):
  numero = None
  
  while not isinstance(numero, int):
    clear()
    try:
      numero = int(input(label))
    except:
      pass

  return numero

# funcion para limpiar la consola tanto en windows como en otros sistemas operativos
def clear():
  if (platform.system() == 'Windows'):
    os.system('cls')
  else:
    os.system('clear')

clear()

numeros = []

# pidiendole al usuario 15 numeros ya almacenandolos en la lista numeros
for num in range(1, 16):
    numeros.append(intInput('Ingresa el ' + str(num) + ' numero: '))

numeros_pares = []
numeros_impares = []

# verificando cuales numeros son pares y cuales pares, y almacenandolos en 
# su respectiva lista
for num in numeros:
    if num % 2 == 0:
        numeros_pares.append(num)
    else:
        numeros_impares.append(num)

clear()
# imprimiendo una lista de los numeros impares
print('Numeros impares:')
for num in numeros_impares:
    print(num)

print('\n\n')

suma_numeros_pares = 0

for num in numeros_pares:
    suma_numeros_pares += num

# imprimiendo la suma de los numeros pares
print('Suma numeros pares:')
print(suma_numeros_pares)

