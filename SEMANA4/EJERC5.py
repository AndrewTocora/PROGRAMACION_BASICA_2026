#ALGORITMO 
#Pedir el nombre del producto
#Pedir el precio por unidad
#Pedir la cantidad del producto
#Calcular el precio
#Calcular el IVA
#Calcular el total
#Mostrar precio
#Mostrar IVA
#Mostrar el total a pagar
#Comparar si el total >= 50000 para aplicar el descuento

#PSEUDOCODIGO 
#print P
#print Pr
#print C
#S=Pr*C
#IVA=S*0.19
#T=S+IVA
#print "Subtotal:", S
#print "IVA:", IVA
#print "El total a pagar es:", T
#print "¿Tiene descuento?:", Total >=50000

P = input("Ingrese el nombre del producto:")
Pr = float(input("Ingrese el precio por unidad:"))
C = int(input("Ingrese la cantidad:"))
S = Pr * C
IVA = S * 0.19
T = S + IVA 
print ("Producto:", P)
print ("Precio por unidad:", Pr)
print ("Cantidad:", C)
print ("Subtotal:", S)
print ("IVA (19%):", IVA)
print ("Total a pagar:", T)
print ("¿Tiene descuento?:", Total >= 50000)
