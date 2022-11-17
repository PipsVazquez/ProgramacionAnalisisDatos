import math

respuesta = "si"


while respuesta == "si":
    valorA = float(input("Valor A: "))
    valorB = float(input("Valor B: "))
    valorC = float(input("Valor C: "))

    discriminante = valorB**2 - (4 * valorA* valorC)

    if discriminante < 0:
        print("Raíces negativas")
    else:
        valorX1 = (-valorB + math.sqrt(discriminante))/(4*valorA)

        valorX2 = (-valorB - math.sqrt(discriminante))/(4*valorA)
        print(f'Los valores de las raíces son x1 = {valorX1} y x2= {valorX2}')

        print(f'La ecuación es (x {valorX1})*(x {valorX2}) =0')



    print('''
        Desea volver a calcular otra ecuación cuadrática...
        Presione
        
        Si - para calcular otra ecuación
        No - para salir del programa"
     ''')
    respuesta = input()

print("Programa finalizado")