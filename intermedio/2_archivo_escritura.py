try :
    #fh = open("archivo.txt", "w") escribir en el archivo
    fh = open("archivo.txt", "a") #fh = open("archivo.txt", "a") abrir al final y con 
    fh.write("Nombre: Maria Patricia Lopez Paz\n")
    fh.write("Direccion: Guatemala zona 11\n")
    fh.write("Telefono: 2222222\n")
    fh.close()

except :
    print ('Error el archivo.')
    exit()