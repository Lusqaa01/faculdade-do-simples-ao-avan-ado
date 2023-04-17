turno = str (input("Digite a inicial do turno que você estuda(M, V ou N):"))


if turno == "m" or turno == "M":
    print ("Bom dia!")

elif turno == "v" or turno == "V":
    print ("Boa tarde!")

elif turno == "n" or turno == "N":
    print ("Boa noite!")

else:
    print("Valor inválido!")
