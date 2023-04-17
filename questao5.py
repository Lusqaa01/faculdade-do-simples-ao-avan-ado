#programa que diga se é consoante ou vogal

letra = input("Digite a letra que você dejesa saber se é vogal ou consoante:")

x = letra.upper()

if x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
    print(f"{x} é vogal.")

else:
    print (f"{x} é consoante.")