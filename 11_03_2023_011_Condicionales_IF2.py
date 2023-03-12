#CAPITULO XXIV y XXV 


#CAPITULO XXIV buscar datos en tuplas o listas
colores = input('Introduce un color:\n')
tuplac = ("azul", "rojo", "naranja", "verde")
#if in se utiliza para verificar si una variavle se encuentra dentro de una lista
if colores in tuplac[0]:
	print("El color azul se encuentra en la tupla")
elif colores in tuplac[1]: 
	print("El color rojo se encuentra en la tupla")
elif colores in tuplac[2]:
	print("El color naranja se encuentra en la tupla")
elif colores in tuplac[3]:
	print("El color verde se encuentra en la tupla")
else:
	print("El color elegido no se encuentra en la tupla\n")
    
#CAPITULO XXV y XXVI Multiples if
print("\n")
print("Bienvenido a la dulceria que desea comprar")
print("Cacahuates 10$")
print("Chiles 2$")
print("Gomitas 7$")
print("Chocolate 10$")

opcion = [1]
propina = [1]
#También podemos utilizar multiples if como sustituos de elif
if 1 in opcion:
    print("Le quedan 0 pesos")
    
if 2 in opcion:
    print("Le quedan 8 pesos")
    
if 3 in opcion:
    print("Le quedan 3 pesos")
    
if 4 in opcion:
    print("Le quedan 0 pesos")
    
if 1 in opcion and 1 in propina: #And se utiliza para que un if se vuelva true solo si todas las condiciones se cumplen
    print("Gracias por la propina")
if 1 in opcion or 0 in propina:
    print("Vuelva pronto") #Or se utilizia para que un if se vuelva true si alguna de las condiciones se cumplen