def entrada():
    return int(input(''))

def numerosImpares():
    lista2 = []
    n = 1
    impar = 1
    while n <= 55 :
        lista1 = []
        for i in range(n):
            lista1.append(impar)
            impar += 2

        lista2.append(lista1)
        n += 2

    return lista2

def soma(linha, lista):
    soma = 0
    lis = lista[linha-1]

    for i in range(3):
        soma += lis[(i+1)*-1]

    return soma

e = entrada()
so = soma(e, numerosImpares())
print(so)