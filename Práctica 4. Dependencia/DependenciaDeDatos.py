import time

start_time = time.time()
a = 2

def subtarea2():
    u = a + 2
    return u

def subtarea3():
    v = a * 7
    return v

u=subtarea2()
v=subtarea3()
x = u + v
print("Respuesta: " + str(x) + "\n")

end_time = time.time()
final_time = round(end_time - start_time,1)

print("Execution time: " + str(final_time) + "\n")
