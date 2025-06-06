import random
numero = random.randint(1,2) #margenes para el random.

numeros = []

for i in range(100):      #guardamos 100 nros randoms
    numeros.append(random.randint(1,100))

print(numeros)  #imprimimos la lista con los 100 nros generados

cont = 0
for i in range(len(numeros)):
    if numeros[i]%2==0:
        cont+=1

print(f"Cantidad de pares en la lista : {cont}")