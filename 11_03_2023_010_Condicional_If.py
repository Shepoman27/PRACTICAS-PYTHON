#CAPITULO XXI,XXII y XXIII CONDICIONALES

#CAPITULO XXI IF
num1 = 15
num2 = 20

if num1 != num2: #Para que la condición sea verdadera podemos decir que ambos numeros son diferentes
	print('Se ejecuta el if.')
    
    
num1 = 1450
num2 = 60

if num1 > num2: #Si el num1 es mayor que num2 sera verdadera la condicion
	print('Se ejecuta el if.')
    
num1 = 1450
num2 = 60

if num1 == num2:#Decir que ambas variables son iguales hara que la condición no se cumpla
	print('Se ejecuta el if.')

#CAPITULO XXII IF ELSE

color = "rojo"

if color != "rojo": #Si el string es diferente de rojo se cumple la condicion
    print("El color no es rojo.") 
else:              #De lo contrario se ejecuta esta condición
    print("El color es rojo.") 
print("\n")

#CAPITULO XXIII IF ELIF ELSE

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 17:
	print('Eres muy chico.')
elif edad >= 18 and edad <= 45:
	print('Eres un adulto.')
elif edad >= 100 and edad <= 120:
	print('Eres muy viejo.')
else:
	print('Edad no válida.')