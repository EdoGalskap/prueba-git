import os

ruta_archivo="nuevo_docmento.txt"

contenido= "este es el nuevo contenido del documento.\n ¡creando código con Python!"

with open (ruta_archivo,"w")as archivo:
    archivo.write(contenido)

    print("archivo en el directorio actual")
    print(os.listdir("."))

    with open(ruta_archivo,"r")as archivo:
        contenido_leido= archivo.read ()
        print(f"\n contenido_leido=archivo:\n{contenido_leido}")
