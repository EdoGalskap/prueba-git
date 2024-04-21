#Conjuntos:
"""son colecciones de datos desordenados y no indexados de elementos unicos.
se definen utilizando llaves {} o tambien la funcion "set()" """

#conjunto de numeros
numerosPrimos={2,3,5,7,11}

#conjunto de letras
lenguaje= set("Python3")

#agregar elementos a un conjunto 
numerosPrimos.add(13)
print(numerosPrimos)

numerosPrimos.remove(3)
print(numerosPrimos)

lenguaje.remove("3")
print(lenguaje)

#Diccionarios
"""son colecciones de datos pares mediante la logica clave:valor 
tambien se declaran mediante {}"""

alumno={
    "Nombre": "Juanito",
    "Edad": 30,
    "Beca": True,
    "Ciudad": "Puerto Montt",
    "Provincia": "Llanquihue",
    "Comuna": "Llanquihue"
}
print(alumno)

#para imprimir un dato especifico de un diccionario

print(alumno["Beca"])

#Modificar un dato especifico de un diccionario

alumno["edad"]=50
print(alumno)

#agregar un nuevo dato clave:valor

alumno["altura"]=1.80
print(alumno)

alumno["Nombre"]="miguelo"
print(alumno)


#como saber de que tipo es un variable con type

print (type(numerosPrimos))

print(type(alumno))

#como obtener un dato del usuario

datoUsuario= input("ingrese un numero")
print(datoUsuario)

print(type(datoUsuario))







