#ALGORITMO
#Pedir el NUM1
#Pedir el NUM2
#Suma de NUM1 y NUM2
#Resta NUM1 y NUM2
#Multiplicación NUM1 y NUM2
#Division NUM1 y NUM2
#Division entera de NUM1 y NUM2
#Residuo de NUM1 y NUM2
#Potencia de NUM1 y NUM2
#Comparar si la suma es mayor a 100
#Mostrar el resultado

#PSEUDOCODIGO 
#LEER NUM1
#LEER NUM2
#Suma <- NUM1 + NUM2
#Resta <- NUM1 - NUM2
#Multiplicacion <- NUM1 * NUM2
#Division <- NUM1 / NUM2
#Division Entera<-NUM1 // NUM2
#Residuo <- NUM1 % NUM2
#Potencia<-NUM1 ** NUM2
#PRINT "Suma: ", Suma
#PRINT "Resta: ", Resta
#PRINT "Multiplicacion: ", Multiplicacion
#PRINT "Division: ", Division
#PRINT "Division Entera: ", Division Entera
#PRINT "Residuo: ", Residuo
#PRINT "Potencia: ", Potencia
#PRINT "¿La suma es mayor a 100?: ", Suma>100


NUM1 = int(input("Ingrese el primer número entero: "))
NUM2 = int(input("Ingrese el segundo número entero: "))

print("La suma es: ", NUM1+NUM2)
print("La resta es: ", NUM1-NUM2)
print("La multiplicación es: ", NUM1*NUM2)
print("La división es: ", NUM1/NUM2)
print("La división entera es: ", NUM1//NUM2)
print("El residuo es: ",NUM1%NUM2)
print("La potencia es: ", NUM1**NUM2)

print("¿La suma es mayor que 100: ", NUM1+NUM2>100)
