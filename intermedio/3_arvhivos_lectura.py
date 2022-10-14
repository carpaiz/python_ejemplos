try :
    fh = open("archivo.txt", "r")
    for linea in fh:
    # print(linea.strip())
        if linea.startswith('Nombre:') :
            print (linea)
except :
    print ('No se pudo abrir el archivo.')
    exit()