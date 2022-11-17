print('''
    Bienvenido al juego de Pips
    Tienes que ingresar número hasta llegar al 100
 ''')
total = 0
iteracion = 0
while total <100 and total >0:
    numero = int(input("Escribe un número"))
    total = total + numero
    iteracion = iteracion + 1
    print("Repetición: ",iteracion, "El total es ", total)
    print("*"*10)

print("Ciclo terminado") 