dia = int(input('Informe o dia'))
mes = int(input('Informe o mes'))

verao = [1, 2, 3]
outono = [4, 5, 6]
inverno = [7, 8, 9]
primavera = [10, 11, 12]

if mes in verao and dia <= 21:
    print('Verão')
if mes in outono and dia <= 21:
    print('Outono')
if mes in inverno and dia <= 21:
    print('Inverno')
if mes in primavera and dia <= 21:
    print('Primavera')
else:
    print()