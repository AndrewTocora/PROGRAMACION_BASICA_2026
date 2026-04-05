P= input("¿Tiene pasaporte vigente?(si/no): ")
V= input("Tiene visa (si/no): ")
E= input("Su país tiene el beneficio de exento de Visa: ")
if P == "si" and (V == "si" or E == "si"): 
    print ("Puedes contuniar a su puerta de vuelo, que tenga feliz viaje")
else:
    print ("No puede viajar. Dirijase a migracion para verificar sus documentos")
