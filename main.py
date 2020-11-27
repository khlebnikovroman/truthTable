
# Здесь ввод логического выражения (* and, + or, - not), не использовать имена переменных состоящих более чем из одного знака
ob="-(a+b)*-(a+b+c)"

ob=" ".join(list(ob))

print(ob)
# устранение импликации в данный момент не работает
while ob.count('->') > 0:
    b = [ob[:ob.index('->') - 1:], ' +' + ob[ob.index('->') + 2:]]

    s = list(b[0])
    if s[-1] != ')':
        s.insert(-2, '-')
    else:
        h = s[-1]
        prav = 1
        lev = 0
        i = 1
        while prav != lev:
            i += 1
            h += s[-i]
            prav = h.count(')')
            lev = h.count('(')

        s.append(' ')
        s.append(')')
        s.insert(-i - 2, '(')
        s.insert(-i - 3, '- ')

    b[0] = ''.join(s)
    ob = b[0] + b[1]
    print(ob)

# print(ob)


# подготовка к эвалу
kal = {' ', '(', ')', '-', '+', '*', '='}
mno = list(set(ob) - kal)
mno.sort()
k = len(mno)
ob = ob.replace('*', 'and').replace('+', 'or').replace('=', '==').replace('-', 'not')
g = []
print(ob)
# заполнение массива значений
for i in range(2 ** k):
    p = '0' * (k - 1) + str(bin(i))[2:]
    p = p[-k:]
    p = list(map(int, list(p)))
    g.append(p)
ans = []

# обработка логичсекого выражения
for i in range(2 ** k):
    for j in range(k):
        ppp = mno[j]
        exec('{} = g[i][j]'.format(ppp))
    ans.append(int(eval(ob)))

print(' '.join(mno), 'F')
for i in range(2 ** k):
    print(' '.join(map(str, g[i])), str(ans[i]))