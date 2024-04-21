#Números complejos

numeroComplejo=5j #crea un número complejo con parte real 5 y parte imaginaria seria j

#datos de tipo rango o range
#crea un objeto con el rango  desde el cero hasta el 9 en este caso

rango= range(9)

#mostrar el range

print(rango)

#mostrar el tipo de dato

print(type(rango))

"""otro tipo de datos "Frozenset: es un tipo de coleccion similat a un set() regular, con la diferencia que los datos no se pueden modificar, eliminar o actualizar"""

frutas=frozenset({"Arándano","Manzana","Sandia"}) #creamos un fronzenset

print(frutas)
print(type(frutas))


"""Bytes: es un tipo inmutable y representa una secuencia de datos desde el numero 0 hasta el 255, se puede crear a partir de una cadena de caracteres, una lista, enteros o un objeto byte existente (principalmente se utiliza para almacenar datos binarios como achivos o datos de red)"""

#crea un objeto byte a partir de una cadena de caracteres.
#Crea un objeto byte a partir de una cadena utilizando la codificacion utf-8
tipoByte= bytes("Hooooola","utf-8")
print(tipoByte)
print(type(tipoByte))

#crear un objeto bytes a partir de una lista de numeros enteros

objetosByte= bytes([72,111,108,97])
print(objetosByte)

"""Abecedario en Byte
A: 65
B: 66
C: 67
D: 68
E: 69
F: 70
G: 71
H: 72
I: 73
J: 74
K: 75
L: 76
M: 77
N: 78
O: 79
P: 80
Q: 81
R: 82
S: 83
T: 84
U: 85
V: 86
W: 87
X: 88
Y: 89
Z: 90

a: 97
b: 98
c: 99
d: 100
e: 101
f: 102
g: 103
h: 104
i: 105
j: 106
k: 107
l: 108
m: 109
n: 110
o: 111
p: 112
q: 113
r: 114
s: 115
t: 116
u: 117
v: 118
w: 119
x: 120
y: 121
z: 122 """

"""otro tipo de datos: byteArray: un tipo de dato inmutable es quiere decir que se puede modificar. va desde el 0 al 255
se utiliza cuando tenemos que manipular datos de forma dinamica como en lectura y ecrituta del flujo de datos."""


#crear un bytearray
byteArray= bytearray("holiwi","utf-8")
print(byteArray)
print(type(byteArray))

byteArray[0]=87
print(byteArray)




"""
¿qué es utf-8?
UTF-8 es un formato de codificación de caracteres Unicode e ISO 10646 que utiliza símbolos de longitud variable.
"""

"""Memoryview: es un tipo de dato que nos permite acceder y manipular de forma eficiente la memoria subyacente de un objeto"""
"""crear un vista de memoria"""

vista=memoryview(byteArray)
print(vista)
print(type(vista))

#imprimir el primer objeto del Array
vista = memoryview(byteArray)
print(vista[0])

#modificar un elemento del Array

vista[0]= 74
print(vista[0])

#otro tipo de dato es el "None", es un tipo de dato que representa la ausencia de valor.

variableNone= None
print(variableNone)
print(type(variableNone))

#Funciones se definen conla palabra reservada "def"

def saludar(nombre):
    return"!Hola"+nombre+" !"

#mensaje de saludo personalizado

mensajeSaludo = saludar(" Estudiante")

print(mensajeSaludo)

"""activdad practica, crear 2 archivos distintos con el .py

el primero: solicitar datos al usuario de temperatura y el programa debera convertir de grados fahrenjeit a celcius ye iprimir el mensaje por consola


el segundo: calculadora con funciones básicas +,-,*,/ utilizando las funciones de python def.


al terminar se suben al repositorio de github "acumulativas-modulo-2"""
