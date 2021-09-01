print('It is simple calculator')  # program with zero

a = float(input('enter the number: '))
x = input('choose operator: (+, -. *, / or =)')
while x != '=':
    b = float(input('enter next number: '))
    if x == '+':
        res = a + b
        print('result: ', a, '+', b, '=', a + b)
    elif x == '-':
        res = a - b
        print('result: ', a, '-', b, '=', a - b)
    elif x == '*':
        res = a * b
        print('result: ', a, '*', b, '=', a * b)
    elif x == '/':
        if b != 0:
            res = a / b
            print('result: ', a, '/', b, '=', a / b)
        else:
            print('ERROR! Cannot be divided by 0')
    a = res
    x = input('choose operator: (+, -. *, / or =)')
print('Thank you!!!!')