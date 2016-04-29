def separaPartes(binario):
    binI = ''
    binF = ''
    aux = ''
    for i in binario:
        if i == ',':
            aux = ','
        elif aux == '':
            binI += i
        elif aux == ',':
            binF += i

    return binI, binF

def binIn2dec(binario):
    dec = 0
    cont = len(binario)
    for i in binario:
        dec += int(i)*2**(cont-1)
        cont -= 1

    return dec

def binFr2dec(binario):
    fra = 0
    cont = -1
    for i in binario:
        fra += int(i)*2**(cont)
        cont -= 1

    return fra

def bin2dec(binario):
    binario = separaPartes(binario)
    a = binIn2dec(binario[0])
    b = binFr2dec(binario[1])
    return a + b

def imprimi(binario, decimal):
    print('Binário: %s\nDecimal: %s' % (binario, decimal))

def entrada():
    return str(input('Binário: '))

binario = entrada()
print(binario.split(','))