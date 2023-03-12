#CAPITULO XLI, XLII Herencia

class Usuario2: #Utilizamos init para tener valore iniciales en una clase
    def __init__(self,nombre,apellidos):
        self.nombre = input("Ingrese el nombre del usuario")
        self.apellidos = input("Ingrese el apellido")
        
    def imprime_datos(self): #Metodo de la clase para imprimir datos
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)
        

usuario002 = Usuario2('','')

class Usuarios_VIP(Usuario2): #De esta forma podemos crear una clase hija
    pass

usuario003 = Usuarios_VIP("", "") #Comprobamos que la clase hija funciona

class UsuariosPremium(Usuario2): #Creamos otro objeto hijo
	def __init__(self, nombre, apellidos, instagram): #Definimos los atributos de la calse
         Usuario2.__init__(self,nombre,apellidos)#Definimos los atributos que queremos que se hereden
         self.instagram = "" #Podemos agregar mas atributos de esta manera
         
