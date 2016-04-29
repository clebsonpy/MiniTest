dic = {"Nome": '',
       "Idade": '',
       "Telefone": '',
       "Endereço": ''}

def entrada(dic):
    for i in dic:
        dic[i] = input('%s: ' % i)

print(entrada(dic))