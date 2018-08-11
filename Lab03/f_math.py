from random import choice, randint
import eval 

x = randint(1, 10)
y = randint(1, 10)

op = ['+', '-', '*', '/']

op = choice(op)

res = eval.calc(x, y, op)



error = [-1, 0, 1]
rand_error = choice(error)

display_res = res + rand_error

print("* " * 20)
print("{0} {1} {2} = {3}".format(x, op, y, display_res))
print("* " * 20)

ans = input(" (Y/N)? ").upper()

if error == 0:
    if ans == "Y":
        print("Yay")
    elif ans == "N":
        print("You're wrong")
else:
    if ans == "Y":
        print("You're wrong")
    elif ans == "N":
        print(" Yay")
