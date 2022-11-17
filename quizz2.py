import math

print('''
Bienvenido al calculador de pitágoras.
 ######                                                                
 #     #  #  ######  #    #  #    #  ######  #    #  #  #####    ####  
 #     #  #  #       ##   #  #    #  #       ##   #  #  #    #  #    # 
 ######   #  #####   # #  #  #    #  #####   # #  #  #  #    #  #    # 
 #     #  #  #       #  # #  #    #  #       #  # #  #  #    #  #    # 
 #     #  #  #       #   ##   #  #   #       #   ##  #  #    #  #    # 
 ######   #  ######  #    #    ##    ######  #    #  #  #####    ####  
                                                                       
''')

respuesta = input("Desea iniciar la calculadora de Pitágoras: Presione si para iniciar y no para terminar: ")
respuesta = respuesta.lower()

#Inicia ciclo de la calculadora
while respuesta == "si":
    print('''
    ¿Qué desea calcular? Presione
    ( 1 ) para Hipotenusa
    ( 2 ) para Cateto A
    ( 3 ) para Cateto B
    ''')
    seleccion = int(input())

    if seleccion == 1:
        print("Calcularemos la Hipotenusa")
        catetoA = float(input("Ingrese el valor del cateto A: "))
        catetoB = float(input("Ingrese el valor del cateto B:"))

        discriminando = (catetoA**2) + (catetoB**2)

        if discriminando < 0:
            print("Valor no válido")
        else:
            resultado = math.sqrt(discriminando)
            print("El valor del resultado es:", resultado)
    
    
    if seleccion == 2:
        print("Calcularemos el cateto A")
        hipotenusa = float(input("Ingrese el valor del hipotenusa: "))
        catetoB = float(input("Ingrese el valor del cateto B: "))

        discriminando = (hipotenusa**2) - (catetoB**2)

        if discriminando < 0:
            print("Valor no válido")
        else:
            resultado = math.sqrt(discriminando)
            print("El valor del resultado es:", resultado)
    
    if seleccion == 3:
        print("Calcularemos el cateto B")
        hipotenusa = float(input("Ingrese el valor del hipotenusa: "))
        catetoA = float(input("Ingrese el valor del cateto A: "))

        discriminando = (hipotenusa**2) - (catetoA**2)

        if discriminando < 0:
            print("Valor no válido")
        else:
            resultado = math.sqrt(discriminando)
            print("El valor del resultado es:", resultado)

    respuesta = input("Desea seguir con la calculadora de Pitágoras: Presione si para continuar y no para terminar: ")
    respuesta = respuesta.lower()



#Termina programa
print('''
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
''')