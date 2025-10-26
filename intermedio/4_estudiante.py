try :
 continuar = 's'
 while True:
   
   if continuar.lower() == 's':
    nombres = input("Ingrese sus nombres:")
    apellidos = input("Ingrese sus apellidos:")
    direccion = input("Ingrese su direccion:")
    fh = open("archivo.txt", "a") #fh = open("archivo.txt", "a") abrir al final y con 
    fh.write("Nombre: "+ nombres + "\n")
    fh.write("Apellidos: "+ apellidos + "\n")
    fh.write("Direccion: "+ direccion + "\n")   
    fh.close()
    continuar = input('Desea continuar? (s/n): ')
    continue
   elif continuar.lower() == 'n':
    fh = open("archivo.txt", "r")
   
    for linea in fh:
        print (linea)
    fh.close()
    break

except :
    print ('Error el archivo.')
    exit()