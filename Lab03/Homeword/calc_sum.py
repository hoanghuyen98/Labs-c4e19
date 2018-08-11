def calc_sum(x, y) :
    sums = x + y
    print("{0} {1} {2} = {3}".format(x, "+", y, sums))


x = int(input('first num: '))
y = int(input('second num: '))

calc_sum(x, y)