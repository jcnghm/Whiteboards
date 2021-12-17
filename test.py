def calc(expression):
    expression = expression.replace(" ", "")
    chars = []
    for i in expression:
        if i in "0123456789":
            chars.append(int(i))
        else:
            chars.append(i)
    answer = ''.join(chars)
        
    print(chars)


calc("3 -(-1)")
# ("1 + 1", 2),
# ("8/16", 0.5),
#             ("3 -(-1)", 4),
#             ("2 + -2", 0),
#             ("10- 2- -5", 13),
#             ("(((10)))", 10),
#             ("3 * 5", 15),
#             ("-7 * -(6 / 3)", 14)


