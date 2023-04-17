print ("Supermercado Compre mais")
print ("-"*30)
print ("Menu:")
opcoes = "1 – Frutas e Verduras\n2 – Produtos de Limpeza\n3 – Molhos\n4 – Alimentos\n5 – Higiene Pessoal\n6 – Bebidas"
print (opcoes)


#variaveis para cada opção:
frutas_e_verduras = "1 – maçã – R$4,00 kg\n2 - -tomate – R$6,00 kg\n3 – alface – R$2,00\n4 – cenoura – R$3,00 kg\n5 – cebola – R$3,50 kg \n6 – uva – R$4,50 kg\n7 – limão – R$4,80 kg\n8 – coentro – R$1,00\n9 – banana - – R$5,00 kg \n10 – mamão – R$6,20 kg"

produtos_de_limpeza = "11 – amaciante – R$10,00\n12 – detergente – R$8,00\n13 – desinfetante – R$7,50\n14 – sabão em pó – R$5,30\n15 – sabão em barra – R$2,40\n16 – sabão líquido – R$8,30\n17 – água sanitária – R$3,00\n18 – limpa vidros – R$11,00\n19 - Multiuso – R$5,20\n20 – alvejante – R$12,00"

molhos = "21 – molho de tomate – R$7,30\n22 – extrato de tomate – R$8,30\n23 – molho shoyo – R$10,40\n24 – molho caesar – R$18,00\n26 – molho rosé – R$18,70\n27 – molho quatro queijos – R$20,30\n28 – molho bechamel – R$20,30\n29 – molho italiano – R$21,80\n30 – molho balsâmico – R$10,20"

alimentos = "31 – arroz – R$9,00\n32 – feijão – R$8,00\n33 – macarrão espaguete – R$5,00\n34 – macarrão parafuso – R$5,40\n35 – farinha de trigo – R$3,50\n36 – massa para cuscuz – R$2,30\n37 – massa para tapioca – R$4,80\n38 – açúcar – R$10,10\n39 – sal – R$3,00\n40 – café – R$9,70"

higiene_pessoal = "41 – shampoo – R$29,00\n42 – condicionador – R$32,00\n43 – sabonete – R$5,00\n44 – pasta de dente – R$2,50\n45 – escova de dente – R$5,40\n46 – fio dental – R$1,30\n47 – desodorante – R$20,10\n48 – creme de cabelo – R$25,40\n49 – absorvente – R$30,30\n50 – sabonete líquido – R$34,80"

bebidas = "51 – agua – R$4,00\n52 – cerveja – R$6,80\n53 – refrigerante – R$8,00\n54 – suco – R$11,00\n55 – vinho – R$63,00\n56 – whisky – R$100,00\n57 – cachaça – R$40,00\n58 – vodka – R$75,00\n59 – rum – R$40,00\n60 - espumante – R$80,00"

#acaba aqui


escolha = input("Digite a escolha que você deseja:")


if escolha == "Frutas e verduras" or escolha == "1" or escolha ==  "frutas e verduras":
    print (frutas_e_verduras)

elif escolha == "produtos de limpeza" or escolha == "2" or escolha == "produtos de Limpeza":
    print (produtos_de_limpeza)

elif escolha == "Molhos" or escolha == "3" or escolha == "molhos":
    print (molhos)

elif escolha == "Alimentos" or escolha == "4" or escolha == "alimentos":
    print (alimentos)

elif escolha == "Higiene Pessoal" or escolha == "5" or escolha == "higiene pessoal":
    print (higiene_pessoal)

elif escolha == "Bebidas" or escolha == "6" or escolha == "bebidas":
    print (bebidas)

else:
    print ("Digite a o numero da lista ou o nome corretamente.")