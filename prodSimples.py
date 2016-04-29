import sys

prod = 1
for line in sys.stdin:
    prod *= int(line)
    print(prod)
print('Prod = %s' % prod)

'''
i = int(input(''))

prod = 1
while i != None:
    try:
        prod *= i
        i = int(input(''))
    except ValueError:
        i = None

print('Prod = %s' % prod)
'''