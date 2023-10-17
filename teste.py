#Entrada

print('    Estações do ano    ')

a = input('Escreva a estação do dia que deseja: ')
aa = input('Escreva o mês que deseja: ')
a.title()

b = '20''março'
c = '21''junho'
d = '23''setembro'
e = '22''dezembro'

if a and aa in b:
    print('outono - 18:25h')
if a in c:
    print('inverno- 03:50h')
if a in d:
    print('primavera - 11:58h')
if a in e:
    print('verão - 00:27h')

