ls1 = []
ls2 = []

print ("Digite os 15 primeiros numeros:")

for i in range (15):
    while True:
        numero = int (input(f"Digite o {i+1} numero inteiro:"))
        if numero not in ls1:
            ls1.append (numero)
            break
        else:
            print ("Numero ja existe na listam, digite outro.")

print ("Digite os 15 ultimos numeros:")

for i in range (15):
    while True:
        numero = int (input(f"Digite o {i+1} numero inteiro:"))
        if numero not in ls2:
            ls2.append (numero)
            break
        else:
            print ("Numero ja existe na listam, digite outro.")

intersecao = []

for numero in ls1:
    if numero in ls2:
        intersecao.append(numero)

print ("\nsegue a lista está a seguir.")
print (intersecao)