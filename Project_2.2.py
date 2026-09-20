def lex_insert(L, a, b):

    new_tuple = (a, b)

    postion = 0
    while postion < len(L) and L[postion] < new_tuple:
        postion += 1
    L.insert(postion, new_tuple)
L = []
lex_insert(L, 3, 1)
lex_insert(L, 1, 10)
lex_insert(L, 8, 11)
lex_insert(L, 8, 9)
lex_insert(L, 2, 5)
print(L)