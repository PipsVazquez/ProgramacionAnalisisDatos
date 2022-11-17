password = "casanova5"
#La indentación(sangría) permite saber que intrucción está relacionada con otras 
# = es asignar un valor
# == es comparar dos valores
passwordUsuario = input("Ingresa la contraseña: ")

if password == passwordUsuario:
    print("Bienvenido al chat")
else:
    print("Acceso Denegado")

