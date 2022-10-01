A = int(input("Digite seu valor:"))
i = A-1
r = 0 
pos = 0
while i<=A and i >= 1:
    if pos == 0:
        r = A * i
        i -= 1
        pos += 1
    else:
        r = r * i 
        i -= 1
        pos+=1
print("Resultado: " ,r)

