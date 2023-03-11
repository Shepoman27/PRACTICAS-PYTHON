#CAPITULO XV,XVI y XII INSERTAR Y ORDENAR ELEMENTOS EN LISTAS

#CAPITULO XV
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.append("fluxia") #Con el metodo append añadimos elementos a una lista a la ultima posición
colores.append("celeste")

for i in colores:
    print(i)
#Comprobamos que se han añadido los nuevos elementos mediante un for

print("\n")
#CAPITULO XVI

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.insert(-4, 'magenta')#Con el metodo insert añadimos elementos a una lista en una posición especifica
colores.insert(-1, 'turquesa') 
for i in colores:
    print(i)
#Comprobamos que se han añadido los nuevos elementos mediante un for
print("\n")

#CAPITULO XVII
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.sort(reverse=True) #Con este metodo ordenamos los elementos de manera AZ O ZA de forma permanente

for i in colores:
    print(i)
#Comprobamos que se se ordenaron los elementos mediante el for