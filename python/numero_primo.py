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

while True:
    numero = intInput('Ingresa un numero para determinar si es primo: ')

    cantidad_divisores = 0

    # por cada numero desde el 1 hasta el numero ingresado por el usuario se
    # verifica si el numero ingresado por el usuario es divisible entre ese numero,
    # en caso positivo, se suma uno a la cantidad de divisores
    for num in range(1, numero + 1):
        if numero % num == 0:
            cantidad_divisores += 1

    # si la cantidad de divisores es mayor a 2 entonces no es un numero primo,
    # de lo contrario, si lo es
    if cantidad_divisores > 2:
        print('No es un numero primo')
    else:
        print('Es un numero primo')

    salir = None

    print('\n\n')

    while salir != '1' and salir != '2':
        salir = input('Deseas salir del programa? (1 o 2):\n1) Si\n2) No\n\n-----> ')
        clear()

    if salir == '1':
        exit()

