def PosMaior(n):
    #posMaior = 0
    Maior = n[0]
    for pos, e in enumerate(n):
        if e>Maior:
            Maior = e
            posMaior = pos

    return posMaior

print(PosMaior([2, 3, 11, 8, 10]))
