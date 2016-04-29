n = int(input(''))

def fatorial(numero):
    fat = 1
    for i in range(1,numero+1):
        fat*=i
    return fat

soma = 0
sinal = 1
x = 1
for i in range(1,n+1):
    fat = fatorial(i)
    soma += (fat/x)*sinal
    sinal *= -1
    x = (x*2) + 1

print(round(soma,2))