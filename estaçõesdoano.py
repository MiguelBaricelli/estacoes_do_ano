dia = int(input('Informe o dia'))
mes = int(input('Informe o mes'))

verao = [1, 2, 3]
outono = [4, 5, 6]
inverno = [7, 8, 9]
primavera = [10, 11, 12]

if mes in verao and dia <= 19:
    print('Verão')
elif mes == 3 and dia >= 20:
    print('Outono')
else:
    print('erro')

if mes in outono:
    print('Outono')
elif mes == 6 and dia <= 21:
    print('Inverno')
else:
    print('Erro')

if mes in inverno and dia <= 22:
    print('Inverno')
elif mes == 9 and dia >= 23:
    print('Primavera')
else:
    print('Erro')

if mes in primavera and dia <= 21:
    print('Primavera')
elif mes == 12 and dia >= 22:
    print('Verão')
else:
    print('Erro')