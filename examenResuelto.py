import math

print('''Quieres iniciar la calculadora de raíces? 
Presione Si para inciar y No para terminar''')
respuesta = input()
respuesta = respuesta.lower()

while respuesta == "si":
    print("Ingresa el valor de a, b y c en ese orden")
    valorA = int(input())
    valorB = int(input())
    valorC = int(input())

    discrimante = (valorB * valorB) - (4*valorA*valorC)

    if discrimante < 0:
        print("Raices negativas")

    else: 
        raizPositiva = ((-1 * valorB) + math.sqrt(discrimante))/(2 *valorA)
        raizNegativa = ((-1 * valorB) - math.sqrt(discrimante))/(2 *valorA)

        print(f'El valor de x1 ={raizPositiva} y x2 = {raizNegativa}')
 
        print(f'La ecuación factorizada es (x-{raizPositiva}) * (x-{raizNegativa})')

    respuesta=input("Quieres volver a calcular?")
    respuesta = respuesta.lower()

print('GAME OVER')