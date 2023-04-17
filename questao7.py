#Faça um programa que leia 3 números e calcule a média ponderada entre eles.
#Considere que o maior número recebe peso 5 e os outros dois recebem peso
#2,5.

num1 = float (input("Digite o primeiro numero:"))
num2 = float (input("Digite o segundo numero:"))
num3 = float (input("Digite o terceiro numero:"))

media_pond1 = (num1 * 5 + num2* 2.5 + num3 * 2.5) / 10
media_pond2 = (num1 * 2.5  + num2* 5 + num3 * 2.5) / 10
media_pond3 = (num1* 2.5 + num2 * 2.5 + num3 * 5) / 10


if num1 > num2 and num1 > num3:
    print (media_pond1)

elif num2 > num1 and num2 > num3:
    print (media_pond2)

elif num3 > num1 and num3 > num2:
    print (media_pond3)