#CAPITULO XXXI, XXXII DICCIONARIOS


#CAPITULO XXXI creaccion de diccionarios
#Creamos un diccionario con 3 elementos diferentes
teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

modelo = teclado2["Modelo"] #Obtenemos un elemento del diccionario de esta forma
precio = teclado2["Precio"]

print("El modelo "+ modelo + "cuesta " + precio)

#CAPITULO XXXII diccionarion y bucle for

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

for x,y in teclado1.items(): #Uitilizamos el metodo items para obtener los elementos del diccionario asi como su contenido
    print(x+" = "+ y+".")
    
#teclado1 arroja los elementos
#teclado1.value() arroja el contenido de los elementos