# cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
# 	# print(car)
# 	if car == 'bmw':
# 		print(car.upper())
# 	else:
# 		print(car.title())


# respuesta = 17

# if respuesta != 42:
# 	print("Esta respuesta no es correcta")


# usuarios_baneados = ['pepe charly', 'jose', 'maria']

# # py2.7 raw_input()
# # p3.X input()

# name = input('Ingresa un nombre de usuario: ')

# if name not in usuarios_baneados:
# 	print(name.title() + " no esta baneado.")
# else:
# 	print(name.title() + " si esta baneado.")


# # validar si eres mayor de edad (18) puedes votar
# edad = int(input("Damne tu edad "))

# """
# if - elif - else
# La entrada para menores de 4 años es gratuita.
# La entrada para cualquier persona entre las edades de 4 y 18
# años es de $ 50.
# La entrada para cualquier persona mayor de 18 años es de $ 100.
# """

# if edad < 4:
#     precio = 0
# elif edad < 18:
#     precio = 50
# else:
#     precio = 100

# print("La entrada te va a costar $" + str(precio))


# print('''
#     Programa de operaciones aritmeticas
#     Teclee una operacion, ejem: suma, resta, division, multiplicación
#     y dos números que desee evaluar
#     ''')

# operacion = input("Teclee la operacion: ")
# num1 = int(input("Teclee el primer numero"))
# num2 = int(input("Teclee el segundo numero"))

# if operacion == "suma":
# 	resultado = num1 + num2
# elif operacion == "resta":
# 	resultado = num1 - num2
# elif operacion == "division":
# 	resultado = num1 / num2
# else:
# 	resultado = num1 * num2

# print("El resultado de la operacion " + str(operacion) + " es " + str(resultado))
# print("El resultado de la operacion {0} es {1}").format(operacion, resultado)


# --- diccionarios --- 
participantes = {
	'nombre': 'Edder',
	'edad': 37,
	'cursos': ['Python', 'React', 'Django'],
}

print(participantes['nombre'])
print(participantes['edad'])
print(participantes['cursos'])

participantes['telefono'] = 9811234567
participantes['ocupacion'] = 'Developer'
print("===========")
print(participantes)


jugador  = {}

jugador['nickname'] = 'noobmaster69'
jugador['score'] = 0

print(jugador)

jugador['score'] = 60
print("El score actual de el jugador " + jugador['nickname'] + " es " + str(jugador['score']))

user = {
    'username': 'edderleonardo',
    'name': 'Edder',
    'lastname': 'Ramirez'
}

print(user.items())

for key, value in user.items():
    print("\n key: " + key)
    print("Value : " + value)



avengers = {
    'cap': {
        'name': 'Steve',
        'lastname': 'Roger',
        'avenger_name': 'Capitan America',
    },
    'stark': {
        'name': 'Anthony Edward',
        'lastname': 'Stark',
        'avenger_name': 'Ironman',
    },
    'MrGreen': {
        'name': 'Bruce',
        'lastname': 'Banner',
        'avenger_name': 'Hulk',
    }
}

for username, avenger_info in avengers.items():
    print('\n Username ' + username)
    fullname = avenger_info['name'] + " " + avenger_info['lastname']
    avenger_name = avenger_info['avenger_name']

    print("\t Nombre real " + fullname)
    print("\t Nombre de vengador " + avenger_name)

'''
funciones: which are named blocks of code that are 
designed to do one specific job

def nombreDeFuncion():
    pass

'''

def saludar():
    """ muestra un saludo """
    print("Hola que tal")

saludar()

# parametros
def saludarPorNombre(username):
    """Saludar por nombre """
    print("Hola que tal " + username)

saludarPorNombre("noobmaster")

# mostrar informacion de usuario y tipo (usuario, superuser, administrador)

# funcion suma

# valors por default
def suma(num1=1, num2=1):
    print(num1 + num2)

suma()

# return: regresando valores 
def nombreCompleto(nombre, apellido):
    return nombre + ' ' + apellido

name = nombreCompleto('Edder', 'Ramirez')
print(name)

# regresar apodo


def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)


""" 
Realiza una función que imprima “Hola mundo”
Realiza una función que sume dos números pasados por parámetros
Realiza una función que indique si un número pasado por parámetro es par o impar.
Crea una función que calcule el factorial de un número pasado por parámetro
Crea una función que dados dos números mostrará todos los números que hay entre ellos.
"""
# funcion para recorrer a este array
users = ['juan', 'oscar', 'maria', 'sara', 'leonardo']

def runNames(usersList):
    for user in usersList:
        print('Hola ' + user )

runNames(users)
# parametros arbitrarios
# es posible que una función, espere recibir un número arbitrario -desconocido- de argumentos

def usersDesconocidos(parametro_fijo, *args):
    print(parametro_fijo)

    for user in args:
        print('Hola ' + user)

usersDesconocidos('noobmaster69', 'user1', 'user2', 'user3')


# Es posible también, obtener parámetros arbitrarios como pares de clave=valor.
# En estos casos, al nombre del parámetro deben precederlo dos astericos (**):

def recorrer_parametros_arbitrarios(parametro_fijo, *args, **kwargs):
    print(parametro_fijo)

    for argumento in args:
        print("Argumento ", argumento)
    
    for key in kwargs:
        print("Clave valor ", key)

print('==================')

recorrer_parametros_arbitrarios(
    "parametro fijo", "arbitrario 1", "arbitrario 2", "arbitrario 3", clave1="valor uno",
clave2="valor dos")

# Desempaquetado de parámetros

def calcular(importe, descuento):
    return importe - (importe * descuento / 100)

datos = [1500, 10]
print('Descuento ', calcular(*datos))

datos = {"descuento": 10, "importe": 1500}
print('Descuento 2 ', calcular(**datos))

# clases
class ClassName:
    pass