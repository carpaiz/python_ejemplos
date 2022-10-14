nombre = 'armando'
print ("Primera Letra:", nombre[0])
for i in range (len(nombre)) :
    print (nombre[i] )

for ii in nombre :
    print ("(",ii,")")  

#Rebanado de cadenas (slicing)
print (nombre[0:2]) # empiece en la pocisio 0 y tome 2 caracteres
print (nombre[5:7])  # empiece en la pocisio 5 tome 3 caracteres
print (nombre[:4])  # tome 4 caracteres desde el inicio de la cadena

print(nombre.upper())
print(nombre.lower())


