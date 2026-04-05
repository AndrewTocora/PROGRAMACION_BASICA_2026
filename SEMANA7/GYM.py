#PSEUDOCODIGO
#PARTE A
#ESCRIBIR "Ingrese su edad"
#LEER a
#ESCRIBIR "¿Tiene carnet de membresia vigente? (si/no)"
#LEER b
#Si edad >14 Y tiene carnet == "si" ENTONCES
#ESCRIBIR "Bienvenido al gym"
#Sino
#ESCRIBIR "Acceso denegado"
#FIN
#PARTE B
#ESCRIBIR "¿Tienes carnet de invitado? (si/no)"
#LEER c
#ESCRIBIR "¿Viene con miembro? (si/no)"
#LEER d
#Si c == "si" O d == "si" ENTONCES
#ESCRIBIR "Puede ingresar al gym"
#SINO
#ESCRIBIR "No puede ingresar al gym")
#FIN
#PARTE A
a = int(input("Ingrese su edad: "))
b = input("¿Tiene carnet de membredia vigente? (si/no): ")
if a > 14 and b == "si":
  print("Bienvenido al gym")
else:
  print("Acceso denegado")
#PARTE B
c = input("¿Tiene carnet de invitado? (si/no): ")
d = input("¿Viene con miembro activo?: ")
if c == "si" or d == "si":
  print("Puede ingresar al gym")
else:
  print("No puede ingresar al gym")
