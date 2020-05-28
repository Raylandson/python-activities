expr = input('type the expression')
pi = []
for simb in expr:
    if simb == '(':
        pi.append('(')
    elif simb == ')':
        if len(pi) > 0:
            pi.pop()
        else:
            pi.append(')')
            break
if len(pi) == 0:
    print('its right')
else:
    print('its wrong')
