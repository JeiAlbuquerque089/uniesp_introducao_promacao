peso = float(input("Qual é seu peso? (kg) "))
altura = float(input("Qual é sua altura? (m)"))
imc = peso / (altura ** 2)
print(" O IMC dessa pessoa é de {:.1f}".format(imc))
if imc < 18.5:
    print("Você está ABAIXO DO PESO nonormal ")
elif 18.5 <= imc < 25:
    print("PARABÉNS, você esta na faixa de PESO NORMAL")
elif 25 <= imc < 30:
    print ("Você esta em SOBREPESO")