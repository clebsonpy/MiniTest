def criarLista(nCol):
    lista = []
    for i in range(nCol):
        n = int(input('Coluna %s: ' % (i+1)))
        lista.append(n)
    return lista

def CriarMatriz(nLin, nCol):
    matriz = []
    for i in range(nLin):
        print('Linha %s:' % (i+1))
        m = criarLista(nCol)
        matriz.append(m)
    return matriz

def ordenaMatriz(matriz):
    lista = []
    for i in matriz:
        for j in i:
            lista.append(j)

    return lista

matriz = CriarMatriz(2,2)
print(ordenaMatriz(matriz))