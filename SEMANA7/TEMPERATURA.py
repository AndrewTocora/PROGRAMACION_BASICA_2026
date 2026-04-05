Temperatura= float(input("Ingrese la temperatura en grados Celsius: "))
if Temperatura < 0:
  print("Bajo Cero, dirijase al hospital a mas cercano")
elif Temperatura >= 0 and Temperatura < 30:
  print("Frio regule su temperatura")
elif Temperatura >= 30 and Temperatura <=36:
  print("Templada, esta en una temperatura perfecta")
elif Temperatura > 36 and Temperatura <= 40:
  print("Calida, este alerta a esta temperatura")
else:
  print("Extremo Calor, dirijase al hospital a mas cercano")
