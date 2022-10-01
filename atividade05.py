
a = b = c = d = f = num = 0
while num >= 0:
    num = int(input('> '))

if num >= 0 and num <= 25:
    a += 1
elif num >= 26 and num <= 50:
    b += 1
elif num >= 51 and num <= 75:
    c += 1
elif num >= 76 and num <= 100:
    d += 1
else:
    f += 1
    
    print(f'Intervalo entre 0 e 25: {a}')
    print(f'Intervalo entre 26 e 50: {b}')
    print(f'Intervalo entre 51 e 75: {c}')
    print(f'Intervalo entre 76 e 100: {d}')
    print(f'Fora dos intervalos: {f}')