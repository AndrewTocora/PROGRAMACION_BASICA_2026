Uc= "admin"
Pc= 1987
usuario= input ("Escribe el nombre de usuario: ")
contraseña= int(input("Escribe tu contraseña: "))
if usuario == Uc and contraseña == Pc:
    print ("Acceso concedido. ¡Bienvenido!")
    print ("Cargando tu perfil...")
else:
    print ("Acceso denegado. Datos incorrectos.")
