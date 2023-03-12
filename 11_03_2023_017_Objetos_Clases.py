#CAPITULO XXXVII,XXXVIII,XXXIX y XL CLASES Y OBJETOS


#CAPITULO XXXVII 
class Usuario: #Creamos una clase con la palarbra reservada  class llamada usuario
	nombre = ''
	apellidos = ''

	def imprime_datos(self): #Esta clase solo tiene un metodo
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario() #Creamos un objeto de la clase usuario llammado usuario001

usuario001.nombre = 'Enrique' #Aginamos valores a los atributos
usuario001.apellidos = 'Barros Fernández'

usuario001.imprime_datos() #Ejecutamos el metodo de usuraio con el objeto usuario001


#CAPITULO XXXVIII

class Usuario2: #Utilizamos init para tener valore iniciales en una clase
    def __init__(self,nombre,apellidos):
        self.nombre = input("Ingrese el nombre del usuario")
        self.apellidos = input("Ingrese el apellido")
        
    def imprime_datos(self): #Metodo de la clase para imprimir datos
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)
        

usuario002 = Usuario2('','') #Pasamos argumentos vacios para que no exista error
usuario002.imprime_datos() #Llamamos a la funcion imprimir datos

#CAPITULO  XXXIX 
#Podemos cambiar el contenido de los atributos de la siguiente manera
usuario002.nombre = "Fulanito"
usuario002.apellidos = "Cabeza de vaca"
usuario002.imprime_datos() #Imprimimos para combrobar que se han cambiado


#CAPITULO XLI

del usuario002 #Utilizamos del para eliminar un objeto
del usuario001.apellidos #También la podemos utilizar para eleminar un atributo de un objeto