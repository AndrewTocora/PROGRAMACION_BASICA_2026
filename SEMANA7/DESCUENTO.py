Ee= input("¿Eres estudiante? (si/no): ")
T= int(input("Ingrese el valor de tu compra: "))
if Ee == "si" or T> 200000:
    D= Total*0.15
    Tf= T-D 
    print ("¡Obtuviste un descuento del 23%!")
    print ("Descuento: ", D)
    print ("Total a pagar: ",Tf)
else: 
    print ("Sin descuento. Total a pagar:", )
