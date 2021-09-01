print('It is simple calculator') # without cycle
x = 'start'
while x != '=':
    a = float(input('enter the number: '))
    x = input('choose operator: (+, -. *, / or =)')
    b = float(input('enter next number: '))
    if x == '+':
        print('result: ', a, '+', b, '=', a + b)
    elif x == '-':
        print('result: ', a, '-', b, '=', a - b)
    elif x == '*':
        print('result: ', a, '*', b, '=', a * b)
        if b != 0:
            res = a / b
            print('result: ', a, '/', b, '=', a / b)
        else:
            print('ERROR! Cannot be divided by 0')
print('Thank you!!!')
