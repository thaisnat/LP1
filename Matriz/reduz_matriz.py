# Reduz Matriz

def reduz_matriz(m):
    for i in range(len(m)):
        if len(m) > 3:
                m.pop(0)
                break
    for j in range(len(m[0])-1):
        if len(m[0])> 3:
            m[j].pop(0)
    for i in range(len(m)-1,-1,-1):
        if len(m) > 3:
            m.pop(-1)
            break
    for j in range(len(m[0])-2,-1,-1):
        if len(m[0])> 3:
            m[j].pop(-1)

    return m

    m = [
        [1, 0, 0, 3, 2, 2, 0],
        [2, 1, 3, 0, 0, 1, 0],
        [0, 0, 1, 2, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 1],
        [0, 1, 2, 0, 3, 1, 2],
        [1, 2, 1, 1, 0, 0, 0],
        [2, 2, 0, 0, 1, 1, 0],
    ]

    assert reduz_matriz(m) == 24

    assert m == [
        [1, 3, 0, 0, 1],
        [0, 1, 2, 1, 0],
        [0, 1, 0, 1, 1],
        [1, 2, 0, 3, 1],
        [2, 1, 1, 0, 0],
    ]

'''b = reduz_matriz(m)
print b'''

'''
# Matriz Original
[1, 0, 0, 3, 2, 2, 0]
[2, 1, 3, 0, 0, 1, 0]
[0, 0, 1, 2, 1, 0, 0]
[0, 0, 1, 0, 1, 1, 1]
[0, 1, 2, 0, 3, 1, 2]
[1, 2, 1, 1, 0, 0, 0]
[2, 2, 0, 0, 1, 1, 0]

# Tirando a primeira linha e a primeira  coluna

[1, 3, 0, 0, 1, 0]
[0, 1, 2, 1, 0, 0]
[0, 1, 0, 1, 1, 1]
[1, 2, 0, 3, 1, 2]
[2, 1, 1, 0, 0, 0]
[2, 0, 0, 1, 1, 0]

# Tirando a ultima linha e a ultima coluna
[1, 3, 0, 0, 1]
[0, 1, 2, 1, 0]
[0, 1, 0, 1, 1]
[1, 2, 0, 3, 1]
[2, 1, 1, 0, 0]

# Asserts

# Matriz Original
[1, 0, 0, 3, 2, 2, 0]
[2, 1, 3, 0, 0, 1, 0]
[0, 0, 1, 2, 1, 0, 0]
[0, 0, 1, 0, 1, 1, 1]
[0, 1, 2, 0, 3, 1, 2]
[1, 2, 1, 1, 0, 0, 0]
[2, 2, 0, 0, 1, 1, 0]

assert reduz_matriz(m) == 24

# Matriz Modificada
[1, 3, 0, 0, 1]
[0, 1, 2, 1, 0]
[0, 1, 0, 1, 1]
[1, 2, 0, 3, 1]
[2, 1, 1, 0, 0]'''
