#CAPITULOS XIII,XIX Y XX

#CAPITULO XIII contar elementos de una lista
colores = ['rojo', 'azul', 'verde', 'amarillo']
print(len(colores)) #Utilizamos la funcion len para contar los elementos o el tamaño de la lista
print("\n")

#CAPITULO XIX tuplas
#Las tuplas no son modificables y se identifican porque se declaran entre parentesis
colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')
print(colores[2])#Imprimimos la posición 2 de la tupla anterirmente creada

numeros = (10, 1, 5, 11) #Creamos una tupla
numeros =  (numeros[0])+(numeros[3])-(numeros[1])+(numeros[2]) #Operamos con los elementos de la tupla para conseguir 25
print("El resultado es: " + str(numeros))
print("\n")

#CAPITULO XX Tuplas a listas
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
tupla = tuple(colores) #Con el metodo tuple convertimos listas a tuplas
print(type(tupla)) #Con el metodo type podemos ver el tipo de dato que contiene una variable