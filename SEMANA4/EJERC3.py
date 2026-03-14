#ALGORITMO 
#Pedir la temperatura en Celsius
#(Celsius *9/5) + 32
#Mostrar la temperatura en Fahrenheit
#Celsius + 273.15
#Mostrar la temperatura en Kelvin
#Comparar si la temperatura en Celsius supera los 37 grados
#Mostrar el resultado

#PSEUDOCODIGO
#LEER Celsius
#Fahrenheit <- (Celsius * 9/5) + 32
#Kelvin <- Celsius + 273.15
#PRINT "La temperatura en Celsius es:", Celsius
#PRINT "La temperatura en Fahrenheit es: ", Fahrenheit
#PRINT "La temperatura en Kelvin es: ", Kelvin
#PRINT "¿La temperatura es mayor a 36.5 grados?: ", Celsius > 36.5

print ("CONVERSOR DE TEMPERATURA")
Celsius= float(input("Ingrese la temperatura en Celsius:"))
Fahrenheit= (Celsius *9/5) + 32
Kelvin = Celsius + 273.15
print("La temperatura en Celsius es: ", Celsius)
print("La temperatura en Fahrenheit es: ", Fahrenheit)
print("La temperatura en  Kelvin es: ", Kelvin)
print("¿La temperatura es mayor a 36.5 grados?: ", Celsius>36.5)
