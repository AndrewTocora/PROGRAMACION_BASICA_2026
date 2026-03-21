#ALGORITMO
#Solicitar al usuario su nombre completo
#Solicitar al usuario digitar su consumo de agua mensual en metros cúbicos (m³)
#Identificar si el consumo generado mensualmente por el usuario es <0 o >45
#Identificar si el consumo es <=0
#Identificar si el consumo es >=1
#Identificar si el usuario tiene un tipo de consumo "Bajo" o "Alto"
#Informar al usuario su tipo de consumo

print("Bienvenido a la EAAB (Empresa de Alcantarillado y Acueducto de Bogota)")
Pnm=input("Ingrese su nombre completo: ")
print("Bienvenido", Pnm)
CS=float(input("Por favor, digite su consumo de agua en metros cúbicos (m³): "))
if CS < 1:
    print("Error: el consumo debe ser mayor a 0")
elif CS == 1:
    print("Usted tiene un bajo consumo, es usted un ciudadano ejemplar")
elif CS <= 29:
    print("Usted tiene un consumo moderado")
elif CS > 29:
    print("Usted presenta un alto consumo, por favor revisar posibles fugas")
