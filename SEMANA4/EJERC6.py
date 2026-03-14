#ALGORITMO
#Pedir el nombre
#Pedir el peso en kilogramos
#Pedir la altura en metros
#Calcular el IMC
#Mostrar el peso
#Mostrar la altura
#Mostrar el IMC
#Comparar si el rango del IMC esta dentro del rango normal
#Mostrar el resultado
#PSEUDOCODIGO
#Nombre
#Peso
#Altura
#IMC=Peso/(Altura*Altura)
#Rangonormal=IMC >= 18.5 Y IMC <= 24.9
#PRINT "Nombre:", Nombre
#PRINT "Peso (kg):", Peso
#PRINT "Altura (m):", Altura
#PRINT "IMC:", IMC
#PRINT "¿Esta en el rango normal?:", Rangonormal
Nombre=input("Ingrese su nombre:")
Peso= float(input("Ingrese su peso(kg):"))
Altura= float (input("Ingrese su altura(m):"))
print ("El rango normal esta entre 18.5 y 24.9")
IMC= Peso/(Altura*Altura)
RangoNormal= IMC >= 18.5 and IMC <= 24.9
print("Nombre:", Nombre)
print("Peso:", Peso)
print("Altura:", Altura)
print("IMC:", IMC)
print("¿Esta en el rango normal?:", RangoNormal)
