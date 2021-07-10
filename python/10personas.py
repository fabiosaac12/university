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

# clase Persona que tendra los datos de una persona
class Persona():
    # metodo constructor de la clase
    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad

personas = []

# pidiendo los datos de 10 personas y almacenandolos en el arreglo personas
for num in range(1, 11):
    nombre = input('Ingresa el nombre de la ' + str(num) + ' persona: ')
    clear()
    direccion = input('Ingresa la direccion de la ' + str(num) + ' persona: ')
    clear()
    edad = intInput('Ingresa la edad de la ' + str(num) + ' persona: ')
    clear()

    personas.append(Persona(nombre, direccion, edad))

persona_mayor = personas[0]
persona_menor = personas[0]
suma_edades = 0
ninios = []
adultos = []
adultos_mayores = []

# determinando varias cosas:
# 1) Cual es la persona mayor y almacenandola en la variable persona_mayor
# 2) Cual es la persona menor y almacenandola en la variable persona_menor
# 3) La suma de todas las edades y almacenandola en la variable suma_edades
# 4) Cuales son las personas menores de 18 anios y almacenandolas en la lista ninios
# 5) Cuales son las personas mayores de 60 anios y almacenandolas en la lista adultos_mayores
# 6) Cuales son las personas cuya edad se encuentra entre los 18 y los 60 anios y
# almacenandolas en la lista adultos
for persona in personas:
    suma_edades += persona.edad

    if persona.edad > persona_mayor.edad:
        persona_mayor = persona

    if persona.edad < persona_menor.edad:
        persona_menor = persona

    if persona.edad < 18:
        ninios.append(persona)
    elif persona.edad > 60:
        adultos_mayores.append(persona)
    else:
        adultos.append(persona)

print('Nombre de la persona mayor: ', persona_mayor.nombre)
print('Promedio de edades: ', str(round(suma_edades / 10)))
print('Direccion de la persona menor: ', persona_menor.direccion)
print('Cantidad de ninios: ', str(len(ninios)))
print('Cantidad de adultos: ', str(len(adultos)))
print('Cantidad de adultos mayores: ', str(len(adultos_mayores)))
