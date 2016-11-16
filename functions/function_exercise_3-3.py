# This exercise will draw a 4x4 grid with '+' and '-'



def plus_dash_plus():
    plus = print('+', end=' ')
    lines = print('- ' * 4, end='')
    plus_2 = print('+')

def side_mid():
    print('| ' + ' ' * 8 + '|')
    print('| ' + ' ' * 8 + '|')
    print('| ' + ' ' * 8 + '|')
    print('| ' + ' ' * 8 + '|')

plus_dash_plus()
side_mid()
plus_dash_plus()
