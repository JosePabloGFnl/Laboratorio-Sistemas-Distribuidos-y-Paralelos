from multiprocessing import Process
import os
import math

def calc():
    for i in range(0,70000000):
        math.sqrt(i)

procesos = []

#a diferencia de usar threads, este programa corre todos los procesos a la vez, haciéndolo paralelo

for i in range(os.cpu_count()):
    print('Proceso: %d ' % i)
    procesos.append(Process(target=calc))

for proceso in procesos:
    proceso.start()

for proceso in procesos:
    proceso.join() #esto evita que al llegar al final del código se cierre la consola