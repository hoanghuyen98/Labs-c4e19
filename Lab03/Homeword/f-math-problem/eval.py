# define
# arguments : tham số đầu vào
def calc (x, y, op):

    res = 0

    if op == "+":
        res = x + y
    elif op == "-":
        res = x - y
    elif op == "*":
        res = x * y
    elif op == "/":
        res = x / y
    
    return res



# call function
# calc(3, 7, "+")
# res = calc(3, 7, "+")
# print(res)