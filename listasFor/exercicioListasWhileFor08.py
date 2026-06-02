import time

print("Iniciando sequencia de lançamento")

time.sleep(1)
print("T menos 15 segundos: Orientação é interna. ")
time.sleep(1)
countdown = -14

while countdown < -9:
    time.sleep(1)
    print(countdown)
    countdown += 1
time.sleep(1)

print("T menos 9 segundos: Início da sequência de ignição.")

countdown += 1

while countdown <= 0:
    time.sleep(1)
    if countdown != 0:
        print(countdown)
        countdown += 1
    else:
        break

print("T menos 0 segundos: Todos os motores funcionando")
time.sleep(1)
print("\nDecolagem! Nós temos uma decolagem, a Apollo 11 está em direção a Lua! ")

