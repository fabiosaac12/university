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

# clase Alumno con todos los datos de un alumno
class Alumno():
    # metodo constructor de la clase
    def __init__(self, nombre, apellido, cedula, correo, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.correo = correo
        self.notas = notas

# clase Notas con todas las notas de un alumno y un metodo para obtener
# el promedio de las notas
class Notas():
    # metodo constructor de la clase
    def __init__(self, quimica, fisica, matematica, historia, literatura):
        self.quimica = quimica
        self.fisica = fisica
        self.matematica = matematica
        self.historia = historia
        self.literatura = literatura

    # metodo para obtener el promedio de el alumno
    def obtener_promedio(self):
        suma_notas = self.quimica + self.fisica + self.matematica + self.historia + self.literatura

        return suma_notas / 5

alumnos = []

num = 1
while True:
    # pidiendole al usuario todos los datos del alumno

    nombre = input('Ingresa el nombre del ' + str(num) + ' alumno: ')
    clear()
    apellido = input('Ingresa el apellido del ' + str(num) + ' alumno: ')
    clear()
    cedula = input('Ingresa la cedula del ' + str(num) + ' alumno: ')
    clear()
    correo = input('Ingresa el correo del ' + str(num) + ' alumno: ')
    clear()

    notas = Notas(
        intInput('Ingresa la nota de quimica del ' + str(num) + ' alumno: '),
        intInput('Ingresa la nota de fisica del ' + str(num) + ' alumno: '),
        intInput('Ingresa la nota de matematica del ' + str(num) + ' alumno: '),
        intInput('Ingresa la nota de historia del ' + str(num) + ' alumno: '),
        intInput('Ingresa la nota de literatura del ' + str(num) + ' alumno: ')
    )

    clear()

    # creando una instancia de la clase alumno par aluego agregarla a la
    # lista de alumnos
    alumno = Alumno(nombre, apellido, cedula, correo, notas)
    alumnos.append(alumno)

    seguir = None

    # preguntandole al usuario si desea seguir agregando alumnos
    while seguir != '1' and seguir != '2':
        seguir = input('Deseas seguir agregando alumnos? (1 o 2):\n1) Si\n2) No\n\n-----> ')
        clear()

    if seguir == '2':
        break

    num += 1

while True:
    opcion = None

    # preguntandole al usuario que accion quiere realizar
    while not opcion in ['1', '2', '3', '4']:
        clear()
        # mostrando el menu
        print('Que deseas? (1, 2, 3, 4):')
        print('1) Promedio de cada materia')
        print('2) Promedio total de la clase')
        print('3) Promedio de cada alumno')
        print('4) Salir')
        opcion = input('-----> ')

    clear()

    # creando listas con todas las notas de una materia utilizando
    # las listas por comprension
    notas_quimica = [alumno.notas.quimica for alumno in alumnos]
    notas_fisica = [alumno.notas.fisica for alumno in alumnos]
    notas_matematica = [alumno.notas.matematica for alumno in alumnos]
    notas_historia = [alumno.notas.historia for alumno in alumnos]
    notas_literatura = [alumno.notas.literatura for alumno in alumnos]

    # calculando el promedio de cada materia
    promedio_quimica = sum(notas_quimica) / len(notas_quimica)
    promedio_fisica = sum(notas_fisica) / len(notas_fisica)
    promedio_matematica = sum(notas_matematica) / len(notas_matematica)
    promedio_historia = sum(notas_historia) / len(notas_historia)
    promedio_literatura = sum(notas_literatura) / len(notas_literatura)

    # decidiendo que accion realizar dependiendo de la opcion que haya escogido el usuario

    if opcion == '1':
        # mostrando el promedio de cada materia
        print('Promedio quimica:', round(promedio_quimica))
        print('Promedio fisica:', round(promedio_fisica))
        print('Promedio matematica:', round(promedio_matematica))
        print('Promedio historia:', round(promedio_historia))
        print('Promedio literatura:', round(promedio_literatura))

    elif opcion == '2':
        # sumando todos los promedios
        suma_promedios = promedio_quimica + promedio_fisica + promedio_matematica + promedio_historia + promedio_literatura

        print('Promedio clase:', round(suma_promedios / 5))

    elif opcion == '3':
        # ordenando los alumnos de forma ascendente con respecto al promedio con la funcion sorted
        # pasandole como key una funcion lambda que devuelve el promedio de un alumno
        alumnos_ordenados_por_promedio = sorted(alumnos, key = lambda x: x.notas.obtener_promedio())

        for alumno in alumnos_ordenados_por_promedio:
            print(alumno.nombre + ':', round(alumno.notas.obtener_promedio()))

    elif opcion == '4':
        # cerrando el programa
        print('Hasta luego')
        exit()

    input()
