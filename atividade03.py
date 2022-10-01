a = float(input("Primeiro numero:"))
b = float(input("Segundo numero:"))
operação = input("digite a operação a realizar (+,-,* ou /):")
if operação == "+":
    resultado = a + b
elif operação == "-":
    resultado = a - b
elif operação == "*":
    resultado = a * b
elif operação == "/":
    resultado = a / b
else:
    print("operação inválida!")
    resultado = 0
print("Resultado: ", resultado)