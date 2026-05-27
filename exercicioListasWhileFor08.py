import time

print("Iniciando sequencia de lançamento")

time.sleep(1)
print("T menos 15 segundos: Orientação é interna. ")
time.sleep(1)

for i in range(-14,-10,1):
    print(i)
    time.sleep(1)

print("T menos 9 segundos: Início da sequência de ignição.")
time.sleep(1)

for i in range(-8,0,1):
    print(i)
    time.sleep(1)

print("T menos 0 segundos: Todos os motores funcionando")
time.sleep(1)
print("Decolagem! Nós temos uma decolagem, a Apollo 11 está em direção a Lua! ")

