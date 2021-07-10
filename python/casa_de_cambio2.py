import platform
import os

# tasas del día (cantidad de bolívares que cuesta cada dólar)
TASA_VENTA_AGENTE = 3200000
TASA_COMPRA_CLIENTE = 3200000
TASA_VENTA_CLIENTE = 3000000
TASA_COMPRA_AGENTE = 3000000

# función para limpiar la pantalla tanto en windows como en 
# otros sistemas operativos
def clear():
  if (platform.system() == 'Windows'):
    os.system('cls')
  else:
    os.system('clear')
clear()

# función para satisfactoriamente recibir un número del usuario
def intInput(label):
  numero = None
  
  while not isinstance(numero, int):
    clear()
    try:
      numero = int(input(label))
    except:
      pass

  return numero

# clase padre Usuario de la cual heredarán otras 2 clases abajo
class Usuario:
  # método constructor que iniciará los atributos de la clase
  def __init__(self, nombre, bolivares, dolares):
    # atributo publico
    self.nombre = nombre
    # atributo protegido
    self._bolivares = bolivares
    # atributo protegido
    self._dolares = dolares
    # atributo privado
    self.__transacciones = []
  
  # los métodos que se encuentran abajo, gracias a la herencia 
  # podran ser utilizados tambien por las clases "hijas"
  
  # método para mostrar el dinero del usuario
  def mostrar_dinero(self):
    print('Posees:')
    # str es una función que convierte un valor numérico en una string

    # en python accedemos a los atributos de la clase anteponiéndoles 
    # la palabra self y un punto, ya que self es el propio objeto
    print('Dólares: ', str(self._dolares) , '$')
    print('Bolívares: ', str(self._bolivares) , 'bs')

  # método para mostrar las últimas transacciones del usuarioz
  def mostrar_ultimas_transacciones(self):
    # verificando que la cantidad de transacciones sea mayor a 1 
    # para poder mostrarlas
    if len(self.__transacciones):
      i = 1
      for transaccion in self.__transacciones:
        # cada transacción es un diccionario (objeto), por lo tanto 
        # debemos acceder a las propiedades de tal objeto encerrando el
        # nombre de la propiedad en comillas y corchetes
        print(
          str(i) + ')',
          transaccion['tipo'].capitalize() + ':',
          str(transaccion['cantidad']),
          '$'
        )
        i += 1
    else:
      print('No poses transacciones aun')

  # metodo que facilita el agregado de nuevas transacciones, ya que el arreglo
  # de transacciones es un atributo privado
  def agregar_transaccion(self, transaccion):
    self.__transacciones.append(transaccion)
  
  # método para deshacer la última transacción del usuario
  def deshacer_ultima_transaccion(self):
    # verificando que la cantidad de transacciones sea mayor a 1 
    # para poder eliminar la última
    if len(self.__transacciones):
      # el método .pop() elimina y retorna el último elemento de un array
      transaccion = self.__transacciones.pop()

      if transaccion['tipo'] == 'venta':
        # si la transacción es de tipo venta, se sumará la cantidad de 
        # dólares y se restará la cantidad de bolívares
        self._dolares += transaccion['cantidad']
        self._bolivares -= transaccion['cantidad'] * transaccion['tasa']
      else:
        # si la transacción es de tipo compra, se sumará la cantidad de 
        # bolívares y se restara la cantidad de dólares
        self._dolares -= transaccion['cantidad']
        self._bolivares += transaccion['cantidad'] * transaccion['tasa']

      print('Última transacción deshecha satisfactoriamente.')
    else:
      print('No posees transacciones aún')

# clase hija Agente que hereda los métodos y atributos de la clase
# padre Usuario
class Agente(Usuario):
  # método constructor de la clase
  def __init__(self, nombre, bolivares, dolares):
    # gracias a la función super() obtenemos el objeto de la clase 
    # padre y podemos inicializar la clase con el mismo método 
    # __init__ de la clase padre
    super().__init__(nombre, bolivares, dolares)
  
  # método para vender dólares
  def vender(self):
    # preguntando al usuario cuál es la cantidad de dólares que quiere vender
    cantidad = intInput('¿Cuántos dólares quieres vender?\n-----> ')

    clear()
    print('Serían', cantidad * TASA_VENTA_AGENTE, 'bolívares los que obtendrías\n')

    # verificando que la cantidad de dólares que el usuario quiere vender 
    # sea menor o igual que la cantidad de dólares que posee
    if cantidad > self._dolares:
      print('No posees esa cantidad de dólares')
    else:
      # restando y sumando la correspondiente cantidad de dólares y 
      # bolívares respectivamente al dinero del usuario
      self._dolares -= cantidad
      self._bolivares += cantidad * TASA_VENTA_AGENTE

      # agregando un nuevo objeto a las transacciones que tiene los datos
      # de la transacción realizada
      self.agregar_transaccion({
        'tipo': 'venta',
        'cantidad': cantidad,
        'tasa': TASA_VENTA_AGENTE
      })
      
      print('Dólares vendidos exitosamente!')

  def comprar(self):
    # preguntando al usuario cual es la cantidad de dólares que quiere comprar
    cantidad = intInput('¿Cuántos dólares quieres comprar?\n-----> ')

    clear()

    print('Serían', cantidad * TASA_COMPRA_AGENTE, 'bolívares\n')

    # verificando que la cantidad de bolívares que el usuario requiere para
    # realizar la compra sea menor o igual que la cantidad de bolívares
    # que posee
    if cantidad * TASA_COMPRA_AGENTE > self._bolivares:
      print('No posees esa cantidad de bolívares')
    else:
      # restando y sumando la correspondiente cantidad de bolívares y 
      # dólares respectivamente al dinero del usuario
      self._bolivares -= cantidad * TASA_COMPRA_AGENTE
      self._dolares += cantidad

      # agregando un nuevo objeto a las transacciones que tiene los datos
      # de la transacción realizada
      self.agregar_transaccion({
        'tipo': 'compra',
        'cantidad': cantidad,
        'tasa': TASA_COMPRA_AGENTE
      })
      
      print('Dólares comprados exitosamente!')


class Cliente(Usuario):
  # método constructor de la clase
  def __init__(self, nombre, bolivares, dolares):
    # gracias a la funcion super() obtenemos el objeto de la clase 
    # padre y podemos inicializar la clase con el mismo método 
    # __init__ de la clase padre
    super().__init__(nombre, bolivares, dolares)

  # método para vender dólares
  def vender(self):
    # preguntando al usuario cuál es la cantidad de dólares que quiere vender
    cantidad = intInput('¿Cuántos dólares quieres vender?\n-----> ')

    clear()
    print('Serían', cantidad * TASA_VENTA_CLIENTE, 'bolívares los que obtendrías\n')

    # verificando que la cantidad de dólares que el usuario quiere vender 
    # sea menor o igual que la cantidad de dólares que posee
    if cantidad > self._dolares:
      print('No posees esa cantidad de dólares')
    else:
      # restando y sumando la correspondiente cantidad de dólares y 
      # bolívares respectivamente al dinero del usuario
      self._dolares -= cantidad
      self._bolivares += cantidad * TASA_VENTA_CLIENTE

      # agregando un nuevo objeto a las transacciones que tiene los datos
      # de la transacción realizada
      self.agregar_transaccion({
        'tipo': 'venta',
        'cantidad': cantidad,
        'tasa': TASA_VENTA_CLIENTE
      })
      
      print('Dólares vendidos exitosamente!')

  def comprar(self):
    # preguntando al usuario cual es la cantidad de dólares que quiere comprar
    cantidad = intInput('¿Cuántos dólares quieres comprar?\n-----> ')

    clear()

    print('Serían', cantidad * TASA_COMPRA_CLIENTE, 'bolívares\n')

    # verificando que la cantidad de bolívares que el usuario requiere para
    # realizar la compra sea menor o igual que la cantidad de bolívares
    # que posee
    if cantidad * TASA_COMPRA_CLIENTE > self._bolivares:
      print('No posees esa cantidad de bolívares')
    else:
      # restando y sumando la correspondiente cantidad de bolívares y 
      # dólares respectivamente al dinero del usuario
      self._bolivares -= cantidad * TASA_COMPRA_CLIENTE
      self._dolares += cantidad

      # agregando un nuevo objeto a las transacciones que tiene los datos
      # de la transacción realizada
      self.agregar_transaccion({
        'tipo': 'compra',
        'cantidad': cantidad,
        'tasa': TASA_COMPRA_CLIENTE
      })
      
      print('Dólares comprados exitosamente!')

nombre = input('Ingresa tu nombre:\n------> ')

usuario = None

rol = None
# bucle que se asegurará de que rol siempre sea un valor válido ('1' o  '2')
while not (rol in ['1', '2']):
  clear()
  rol = input('¿Quieres ingresar como agente o cliente? (1 o 2)\n1) Agente\n2) Cliente\n-----> ')

bolivares = intInput('Ingrese la cantidad de bolívares que tiene (número entero)\n-----> ')
dolares = intInput('Ingrese la cantidad de dólares que tiene (número entero)\n-----> ')

# creando el usuario como Agente o Cliente dependiendo de la opción 
# que haya escogido el usuario
if (rol == '1'):
  usuario = Agente(nombre, bolivares, dolares)
elif (rol == '2'):
  usuario = Cliente(nombre, bolivares, dolares)

clear()

# bucle principal del programa que solo puede ser finalizado con la 
# terminación del programa
while True:
  opcion = None

  # bucle que se asegurará de que opción siempre sea un valor válido
  while not opcion in ['1', '2', '3', '4', '5', '6']:
    clear()
    if rol == '1':
      print('Tasa del dia para la venta:', TASA_VENTA_AGENTE)
      print('Tasa del dia para la compra:', TASA_COMPRA_AGENTE)
      print('')
    if rol == '2':
      print('Tasa del dia para la venta:', TASA_VENTA_CLIENTE)
      print('Tasa del dia para la compra:', TASA_COMPRA_CLIENTE)
    print('Hola,', usuario.nombre + '. ¿Qué acción quieres realizar? (1, 2, 3, 4 o 5)')
    print('1) Consultar mi dinero')
    print('2) Revisar últimas transacciones')
    print('3) Deshacer mi última transacción')
    print('4) Vender dólares')
    print('5) Comprar dólares')
    print('6) Salir')
    opcion = input('-----> ')
  
  clear()
  
  # realizando la acción correspondiente dependiendo de la opción que 
  # haya elegido el usuario
  if (opcion == '1'):
    usuario.mostrar_dinero()
  if (opcion == '2'):
    usuario.mostrar_ultimas_transacciones()
  if (opcion == '3'):
    usuario.deshacer_ultima_transaccion()
  if (opcion == '4'):
      usuario.vender()
  if (opcion == '5'):
      usuario.comprar()
  if (opcion == '6'):
    print('Hasta luego.')
    exit()
  
  input()
