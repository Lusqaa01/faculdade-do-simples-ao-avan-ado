numeros = []
pares = []
impares = []

for i in range (20):
    numero = int (input("Digite os 20 numeros:"))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    elif numero % 2 == 1:
        impares.append (numero)

print (f"Numeros digitados: {numeros}")
print (f"Numeros pares: {pares}")
print (f"Numeros impares: {impares}")