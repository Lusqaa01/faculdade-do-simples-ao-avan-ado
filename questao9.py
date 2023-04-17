nota1 = float (input ("Digite a primeira nota:"))
nota2 = float (input ("Digite a segunda nota:"))

media = (nota1+nota2)/2

if media > 9 and media < 10:
    print (media, ", conceito: A; aprovado!")

elif media > 7.5 and media < 9:
    print (media, ", conceito: B; aprovado!")

elif media >6.0 and media < 7.5:
    print (media, ",conceito: C; aprovado!")

elif media > 4.0 and media <6.0:
    print (media, ", conceito: D; reprovado!")

elif media >0 and media <4.0:
    print (media, ", conceito: E; reprovado!")