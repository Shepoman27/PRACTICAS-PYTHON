#CAPITULO XXXIV,XXXV y XXXVI FUNCIONES


#CAPITULO XXXIV FUNCIONES I
def suma(num1,num2): #Se utiliza def para crear una funcion, entre parentesis se le pasan los argumentos deseados a la hora de llamar la función
    print(num1+num2)
    
suma(15,15) #Llamamos a la función pero le damos de valor deferentes argumentos
suma(25,25)
suma(50000,7000)


#CAPITULO XXXV FUNCIONES II

#Parte 1
def colores(*args): #Se utiliza args como argumento para no tener definido el numero de elementos a pasasar a la función
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores("Rojo","Verde")

#Parte 2
def suma2(*args): 
    suma3 = 0
    for x in args: #Se crea un ciclo for para sumar los numeros que contenga el argumento
        suma3 += x
    print("El resulatado de la sumas es "+str(suma3))

numeros = [1,2,3,4,5]
suma2(*numeros) #Se le pasa al función suma la lista numeros

#Parte 3
def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo') # 4 Argumentos
colores('lila', 'negro', 'rojo') # 3 Argumentos
colores('rosa') # 1 Argumento
colores('marrón', 'naranja') # 2 Argumentos


#CAPITULO XXXVI FUNCIONES III

def colores(**kwargs):
    print("Mis colores favoritos son"+ kwargs["color1"]+" y "+ kwargs["color2"])
    
colores(color1 = "rojo", color2 = "verde")
#De esta manera utilizamos funciones con kwargs

