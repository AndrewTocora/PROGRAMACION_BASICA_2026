#ALGORITMO
#PEDIR EL VALOR DE LA BASE DEL TRIANGULO
#PEDIR EL VALOR DE LA ALTURA DEL TRIANGULO
#CALCULAR EL AREA
#COMPARAR RESULTADO CON NUMERO 100
#EL AREA ES MAYOR QUE 100 TRUE
#EL AREA ES MENOR O IGUAL A 100 FALSE

#PSEUDOCODIGO
#LEER LA BASE DEL TRIANGULO
#LEER LA ALTURA DEL TRIANGULO
#ESCRIBIR ES MAYOR QUE 100
#ESCRIBIR SI EL AREA ES MENOR O IGUAL A 100

base=float(input("Ingrese el valor de la base:"))
altura=float(input("Ingrese el valor de la altura:"))
area=(base*altura)/2
print("El area de el triangulo es:",area)
print ("¿El area es mayor que 100?",area,area>100)
print("¿El area es menor o igual que 100?",area, area<=100)
