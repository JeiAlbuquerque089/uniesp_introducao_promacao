#Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer, 
 #calcular e escrever quantas vezes esse número aparece no vetor.


numeros = [10,20,30,40,50,60,70,80,90,77,1,2,3,4,5,6,77,8,9,10,11,12,13,14,15,16,17,18,19,77]
numero = int(input('digite um numero: '))
count = 0
for num in numeros:
    if num == numero:
        count += 1
print(f'{numero} apareceu {count} vezes')