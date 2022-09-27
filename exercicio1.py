print ("[!]PROMOÇÃO[!]")
print ("maçãs por 1,30r$ ou acima de 12 por apenas 1,00r$ !")

maçãs = int(input("digite quantas maçãs quer comprar:"))

preçoPromoção = 1.00
preçocomum = 1.30

valorPromoçao = maçãs * preçoPromoção
valorComum = maçãs * preçocomum


print ("VALOR A PAGAR:")
if maçãs >=12:
    print (valorPromoçao)
elif maçãs <= 11:
    printe(valorComum)