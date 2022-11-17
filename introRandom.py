import random
import time

for i in range(0,9):
    #num = random.random() #Numero Aleatorio entre 0 y 1
    #num = random.randint(0,100) #Numero Aleatorio entre a y b
    #num = random.random()*random.randint(0,90)
    #num = random.randrange(0,100,3)
    #print(round(num,3))
    for j in range(0, 3):
        print(".")
        time.sleep(2)
    alumnos = random.choice(["Humberto","jovana","Melissa"])
    print(alumnos)