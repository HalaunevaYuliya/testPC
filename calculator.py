print('It is simple calculator')
x = 'start'
while x != '=':
    a = float(input('enter the number: '))
    x = input('choose operator: (+, -. *, / or =)')
    b = float(input('enter next number: '))
    if x == '+':
        #res = res
        print('result: ', a, '+', b, '=', a + b)
    elif x == '-':
        print('result: ', a, '-', b, '=', a - b)
    elif x == '*':
        print('result: ', a, '*', b, '=', a * b)
    elif x == '/':
        print('result: ', a, '/', b, '=', a / b)

print('Thank you!!!')
