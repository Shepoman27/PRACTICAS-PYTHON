#CAPITULO XXVII BUCLE WHILE

x = 0 #Bucle que se repetira hasta que x sea mayor que 15 con un incremento de 5 en x
while x <= 15:
    print(x)
    x +=5
    
x = 0
while x >= -100: #Bucle que se repetira hasta que x sea menor que -100 con un decremento de -20 en x
	print(x)
	x -= 20
    
x = 10  #Bucle que se repetira hasta que x sea mayor que 0 con un decremento de 1 en x
while x >= 0:
	print('El valor de x es: ', x)
	x -= 1
print("\n")    

#CAPITULO XXVII BUCLE WHILE 2
x = 0
while x <= 30:
    x += 1
    if x == 4 or x == 6 or x == 10:
        print("Se salto el valor: "+str(x))
        continue
    if x == 15:
        print("Se ha salido del bucle")
        break
    print ("El valor del bucle es: " + str(x))  
