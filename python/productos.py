import platform
import json
import os

TASA = 3600000

def intInput(label):
    numero = None
      
    # mientras numero no sea un entero se seguira pidiendo un numero al usuario
    while not isinstance(numero, int):
        clear()
        try:
            numero = int(input(label))
        except:
            pass

    return numero

def clear():
    # si el sistema operativo es windows se ejecutara el comand "cls",
    # si no, se ejecutara el comando "clear"
    if (platform.system() == 'Windows'):
        os.system('cls')
    else: os.system('clear')

clear()

class Producto():
    # metodo constructor de la clase
    def __init__(self, codigo, nombre, descripcion, categoria, precio, cantidad):
        # atributos de la clase
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    def obtener_informacion(self):
        # devuelve una string con toda la informacion de el producto
        return (
            f'{self.nombre}:\n'
            f'  Codigo: {self.codigo}\n'
            f'  Descripcion: {self.descripcion}\n'
            f'  Categoria: {self.categoria}\n'
            f'  Precio: {self.precio}\n'
            f'  Cantidad: {self.cantidad}\n'
        )

class Venta():
    # metodo constructor de la clase
    def __init__(self, codigo_producto, cantidad):
        # atributos de la clase
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad

archivo_productos = None
archivo_ventas = None

try:
    # abriendo los archivos de productos y ventas
    archivo_productos = open('productos.txt')
    archivo_ventas = open('ventas.txt')
except:
    # en caso de que los archivos no existan simplemente no hacemos nada
    pass

productos = []
ventas = []

if archivo_productos:
    # en el archivo de productos estan almacenados los productos como una string
    # tenemos que convertirlos en un arreglo de diccionarios
    # con el metodo loads de el objeto json lo hacemos
    productos_como_diccionarios = json.loads(archivo_productos.read())

    for producto_como_diccionario in productos_como_diccionarios:
        # creando un objeto con los datos del diccionario
        producto = Producto(
            producto_como_diccionario['codigo'],
            producto_como_diccionario['nombre'],
            producto_como_diccionario['descripcion'],
            producto_como_diccionario['categoria'],
            producto_como_diccionario['precio'],
            producto_como_diccionario['cantidad'],
        )

        productos.append(producto)

    archivo_productos.close()

if archivo_ventas:
    # en el archivo de ventas estan almacenadas las ventas como una string
    # tenemos que convertirlas en un arreglo de diccionarios
    # con el metodo loads de el objeto json lo hacemos
    ventas_como_diccionarios = json.loads(archivo_ventas.read())

    for venta_como_diccionario in ventas_como_diccionarios:
        # creando un objeto con los datos del diccionario
        venta = Venta(
            venta_como_diccionario['codigo_producto'],
            venta_como_diccionario['cantidad'],
        )

        ventas.append(venta)

    archivo_ventas.close()

cantidad_bolivares = 0
cantidad_dolares = 0

while True:
    clear()
    opcion = None

    # mientras la opcion no sea valida, seguiremos preguntando
    while not (opcion in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']):
        # mostrando el menu de opciones
        print('Selecciona una opcion (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11):')
        print('1) Agregar un producto')
        print('2) Vender un producto')
        print('3) Modificar un producto')
        print('4) Mostrar lista de productos')
        print('5) Mostrar lista de productos por categoria')
        print('6) Mostrar dinero')
        print('7) Mostrar dinero obtenido en ventas')
        print('8) Mostrar productos agotados')
        print('9) Mostrar producto mas costoso')
        print('10) Mostrar producto mas economico')
        print('11) Salir')

        opcion = input('\n-----> ')

    clear()

    # si la opcion es igual a 1, el usuario quiere agregar un nuevo producto
    if opcion == '1':
        codigo = input('Ingresa el codigo del producto: ')
        clear()

        nombre = input('Ingresa el nombre del producto: ')
        clear()

        descripcion = input('Ingresa la descripcion del producto: ')
        clear()

        categoria = input('Ingresa la categoria del producto: ')
        clear()

        precio = intInput('Ingresa el precio del producto: ')
        clear()

        cantidad = intInput('Ingresa la cantidad disponible del producto: ')
        clear()

        # creando el objeto de clase Producto para agregarlo en el arreglo de productos
        producto_nuevo = Producto(codigo, nombre, descripcion, categoria, precio, cantidad)

        productos.append(producto_nuevo)

        print('Producto agregado exitosamente.')

    # si la opcion es igual a 2, el usuario quiere vender un producto
    elif opcion == '2':
        codigo = input('Ingresa el codigo del producto que quieres vender: ')
        clear()
        
        try:
            # buscamos entre todos los productos el producto cuyo codigo sea igual al
            # codigo ingresado por el usuario
            # en caso de que el usuario ingrese un codigo de un producto inexistente
            # ocurrira un error, por eso manejamos esto dentro de un try
            producto = next(p for p in productos if p.codigo == codigo)
            cantidad = intInput('Ingresa las unidades que quieres vender del producto: ')
            clear()

            # verificamos que el producto este disponible
            if producto.cantidad < cantidad:
                print('No posees suficientes unidades del producto.')
            else:
                forma_de_pago = None
                while not (forma_de_pago in ['1', '2']):
                    forma_de_pago = input('El producto sera pagado con bolivares o dolares (1 o 2):\n1) Bolivares\n2) Dolares\n\n-----> ')
                    clear()

                # si la forma de pago es igual a "1", la venta se hara en bolivares, de lo
                # contrario, la venta se hara en dolares
                if forma_de_pago == '1':
                    cantidad_bolivares += cantidad * (TASA * producto.precio)
                else:
                    cantidad_dolares += cantidad * producto.precio

                producto.cantidad -= cantidad

                print('El producto ha sido vendido exitosamente')

                # creamos una instancia de la clase Venta para agregarla a la variable ventas
                venta = Venta(producto.codigo, cantidad)

                ventas.append(venta)

        except:
            print('El codigo que has ingresado no pertenece a ningun producto')

    # si la opcion es igual a 3, el usuario quiere modificar un producto
    elif opcion == '3':
        codigo = input('Ingresa el codigo del producto que quieres modificar: ')
        clear()

        try:
            # buscamos entre todos los productos el producto cuyo codigo sea igual al
            # codigo ingresado por el usuario
            # en caso de que el usuario ingrese un codigo de un producto inexistente
            # ocurrira un error, por eso manejamos esto dentro de un try
            producto = next(p for p in productos if p.codigo == codigo)

            # preguntando al usuario los nuevos datos para el producto y actualizandolo
            # de una vez
            clear()
            print(producto.obtener_informacion())
            nombre = input('\nIngresa el nuevo nombre del producto: ')
            producto.nombre = nombre

            clear()
            print(producto.obtener_informacion())
            descripcion = input('\nIngresa la nueva descripcion del producto: ')
            producto.descripcion = descripcion

            clear()
            print(producto.obtener_informacion())
            categoria = input('Ingresa la nueva categoria del producto: ')
            producto.categoria = categoria

            clear()
            precio = intInput(producto.obtener_informacion() + '\n\nIngresa el nuevo precio del producto: ')
            producto.precio = precio

            clear()
            cantidad = intInput(producto.obtener_informacion() + '\n\nIngresa la nueva cantidad disponible del producto: ')
            producto.cantidad = cantidad

            clear()

            print('El producto ha sido actualizado exitosamente.')

        except:
            print('El codigo que has ingresado no pertenece a ningun producto')

    # si la opcion es igual a 4, el usuario quiere una lista de todos los productos
    elif opcion == '4':
        # iteramos sobre todos los productos y para cada producto ejecutamos el
        # metodo obtener_informacion
        for producto in productos:
            print(producto.obtener_informacion())

    # si la opcion es igual a 5, el usuario quiere una lista de todos los
    # productos de una categoria
    elif opcion == '5':
        categoria = input('Ingresa la categoria de los productos que quieres consultar:\n\n-----> ')

        clear()
        
        productos_filtrados = []

        for producto in productos:
            # verificando que el producto pertenece a la categoria ingresada
            # por el usuario, en caso positivo, lo agregaremos a la lista de
            # productos_filtrados
            if producto.categoria == categoria:
                productos_filtrados.append(producto)

        # si la cantidad de productos_filtrados es igual a 0 es por que no hay productos
        # con esa categoria, en caso contrario, imprimiremos todos los productos filtrados
        if len(productos_filtrados) == 0:
            print('No hay ningun producto que pertenezca a la categoria ingresada')
        else:
            print('Productos pertenecientes a la categoria', categoria, ':\n')
            for producto in productos_filtrados:
                print(producto.obtener_informacion())

    # si la opcion es igual a 6, el usuario quiere saber cual es la cantidad de dinero
    # que posee, tanto en dolares como en bolivares
    elif opcion == '6':
        print('Cantidad de dolares:', cantidad_dolares)
        print('Cantidad de bolivares:', cantidad_bolivares)

    # si la opcion es igual a 7, el usuario quiere saber cual es la cantidad de dinero
    # que ha obtenido con las ventas, el resultado se mostrar en dolares, y tambien se
    # mostrara su equivalente en bolivares
    elif opcion == '7':
        dinero_obtenido = 0

        for venta in ventas:
            # buscamos entre todos los productos el producto cuyo codigo sea igual al
            # codigo del producto de la venta 
            producto = next(p for p in productos if p.codigo == venta.codigo_producto)

            # sumar al dinero obtenido el precio del producto multiplicado por la
            # cantidad de de productos que se vendieron
            dinero_obtenido += producto.precio * venta.cantidad

        # mostrando la cantida de dinero obtenido en dolares y su equivalente en
        # bolivares
        print('Dinero obtenido en ventas (dolares):', str(dinero_obtenido) + '$')
        print('Dinero obtenido en ventas (bolivares):', dinero_obtenido * TASA, 'Bs. S.')

    # si la opcion es igual a 8, el usuario quiere saber cuales son los productos
    # agotados
    elif opcion == '8':
        print('Productos agotados:\n')

        for producto in productos:
            # si la cantidad disponible del producto es 0, significa que esta agotado,
            # entonces mostraremos informacion de ese producto
            if producto.cantidad == 0:
                print(producto.obtener_informacion())

    # si la opcion es igual a 9, el usuario quiere saber cual es el producto mas
    # costoso
    elif opcion == '9':
        producto_mas_costoso = productos[0]

        # iteramos el arreglo de los productos. Para cada producto, si es mas costoso
        # que el supuesto producto_mas_costoso, ahora el producto_mas_costoso sera ese
        # producto
        for producto in productos:
            if producto.precio > producto_mas_costoso.precio:
                producto_mas_costoso = producto

        print('Producto mas costoso:\n')

        print(producto_mas_costoso.obtener_informacion())

    # si la opcion es igual a 10, el usuario quiere saber cual es el producto mas
    # economico
    elif opcion == '10':
        producto_mas_economico = productos[0]

        # iteramos el arreglo de los productos. Para cada producto, si es mas economico
        # que el supuesto producto_mas_economico, ahora el producto_mas_economico sera ese
        # producto
        for producto in productos:
            if producto.precio < producto_mas_economico.precio:
                producto_mas_economico = producto

        print('Producto mas economico:\n')

        print(producto_mas_economico.obtener_informacion())

    # si la opcion es igual a 11, el usuario quiere salir del programa
    elif opcion == '11':
        productos_como_diccionarios = []

        for producto in productos:
            # convertimos los objetos de clase Producto en dicconarios
            # para que posteriormente puedan ser pasados a string
            productos_como_diccionarios.append(producto.__dict__)

        ventas_como_diccionarios = []

        for venta in ventas:
            # convertimos los objetos de clase Venta en dicconarios
            # para que posteriormente puedan ser pasados a string
            ventas_como_diccionarios.append(venta.__dict__)

        # con el metodo json.dumps pasamos un diccionario a string
        productos_en_texto = json.dumps(productos_como_diccionarios)
        ventas_en_texto = json.dumps(ventas_como_diccionarios)

        # abrimos los archivos productos.txt y ventas.txt con permiso para modificarlos
        archivo_productos = open('productos.txt', 'w')
        archivo_ventas = open('ventas.txt', 'w')

        # reescribimos el contenido de los archivos productos.txt y ventas.txt con
        # los productos en texto y las ventas en texto, respectivamente
        archivo_productos.write(productos_en_texto)
        archivo_ventas.write(ventas_en_texto)

        # cerramos los archivos para que los cambios puedan ser guardados 
        # correctamente
        archivo_productos.close()
        archivo_ventas.close()

        # salimos del programa
        exit()

    input()
