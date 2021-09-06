import time


u = int(input("Ingrese un valor para U: "))
v = int(input("Ingrese un valor para V: "))
w = int(input("Ingrese un valor para W: "))
x = int(input("Ingrese un valor para X: "))

start_time = time.time()

if u == 0:
    v = w
else:
    v = w + 1
    x = x - 1

print ("El valor de U es: " + str(u) + "\n")
print ("El valor de V es: " + str(v) + "\n")
print ("El valor de W es: " + str(w) + "\n")
print ("El valor de X es: " + str(x) + "\n")

end_time = time.time()
final_time = round(end_time - start_time,1)

print("Tiempo de ejecución: " + str(final_time) + "\n")