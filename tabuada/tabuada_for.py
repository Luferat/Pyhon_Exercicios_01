"""
Tabuada de multiplicação usando `for` aninhados e `range()`
"""
for x in range(10):
    for y in range(10):
        print(x, 'x', y, '=', x*y)
    print('---------------------')
