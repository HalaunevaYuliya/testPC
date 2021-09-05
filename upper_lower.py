def caps(phrase:str) -> str:
    phrase_lit = list(phrase)
    little = list('abcdefghijklmnopqrstuvwxyz')
    big = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    c1 = 0
    for letter in phrase_lit:
        if letter in little:
            c2 = 0
            for letter_litle in little:
                if letter == letter_litle:
                    index_l = c2
                c2 += 1
            phrase_lit[c1] = big[index_l]
        c1 = c1 + 1
    return ''.join(phrase_lit)


def uncaps(phrase:str) -> str:
    phrase_lit = list(phrase)
    little = list('abcdefghijklmnopqrstuvwxyz')
    big = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    c1 = 0
    for letter in phrase_lit:
        if letter in big:
            c2 = 0
            for letter_big in big:
                if letter == letter_big:
                    index_b = c2
                c2 += 1
            phrase_lit[c1] = little[index_b]
        c1 = c1 + 1
    return ''.join(phrase_lit)


methods = ['caps', 'uncaps']
phrase = input('Enter phrase: ')
print('Enter method for modification ', methods, ': ')
method = input()
while method not in methods:
    method = input('Error! Please reenter: ')
if method == 'caps':
    res = caps(phrase)
elif method == 'uncaps':
    res = uncaps(phrase)
print(res)





