#CAPITULO XXXIII DICCIONARIOS II

#CAPITULO XXXIII

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

del teclado1 #Utilizamos del de esta forma para elminiar todo el diccionario

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}


teclado2.pop("Categoría")
teclado2.pop("Precio")
print(teclado2["Modelo"])