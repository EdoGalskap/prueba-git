#para escribir comentarios se ocupa este simbolo "#"
#comentarios de una linea
""" para escribir comentarios de mas lineas triple comilla
o dobles o simples"""

"""normalmente se usa para 
explicar funciones """
""" algunas exteciones toman los comentarios como parte de la documentacion"""

"""una variable es una caja vacia donde podemos meter datos, numero, listas, etc"""
"""una variable es un espacio de memoria reservado para almacenar datos
que pueden cambiar en el transcurso del programa"""
"""python es un enguaje de programacion dinamico, no es nacesario declarar
explicitamente el tipo de variable antes de utilizarla"""

#variables de python
"""deben contener letras, numeros o guiones bajos"""
"""deben comenzar con una letra"""

variable=1

#python es "case sensitive"

variable=1
Variable=1

"""para declarar una variable no se pude utilizar un palabra reservada"""

"""palabras reservadas"""

"""False,None,True, and,as,assert, await, break, class, continue,def,del,elif, else, except finally
for, from, global, if, import, in, is, lambda, nonlocal,not,or,pass, raise, try, while, with, yield. 
"""
#tipos de datos

entero=2
decimalFloat=2.5
cadenaTexto=" hola wey, soy una cadena"
suma= 2+2
resta=4-2
multiplicacion=3*3
division=10/2


#imprimir datos

print(suma, resta, multiplicacion)
print(resta)
print(multiplicacion)
print(division)


mensaje= "hola"
nombre= "edo"

print(mensaje,nombre)
#concatenar variables mas texto
print(mensaje+ "texto extra" +nombre)


"""booleanos"""

edad=18
esEstudiante=True
estaTrabajando=False

#operacion logica con booleanos
esMayorDeEdad= edad>=18
puedeVotar= esMayorDeEdad and estaTrabajando
print(esMayorDeEdad)
print(puedeVotar)

#listas
"""colecciones de datos ordenados y modificables, pueden contener
distintos tipos de datos"""
"""se defines con los corchete []"""

numeros=[1,2,3,4,5,6,7,8,9]
nombres=["edo","andy","campo","profe","gato"]

#lista mixta

mixta=[1,"gato",True,2,5]

"""cuando aparace una pelota blanca arriba al lado del nombre de mi documento
quiere decir que no se ha guardado """

print(numeros)
print(numeros[6])
print(numeros[-3])



#Tuplas

"""al igual que las listas son colecciones de datos ordenados e inmutables en las 
listas se pueden modificar pero en las tuplas no"""

coordenadas=(10,20)
meses=("Enero","Febrero","Marzo")

print(meses)
print(meses[-1])
print(meses[2])