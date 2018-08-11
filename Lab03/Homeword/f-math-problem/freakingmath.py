from random import *
from eval import calc 
def generate_quiz():

    op = ["+", "-", "*", "/"]
    op = choice(op)

    x = randint(0, 10)

    if op == "/":
        y = randint(1, 10)
    else:
        y = randint(0, 10)


    error = [-1, 0, 1, 0]
    error = choice(error)

    display_result = calc(x, y, op) + error

    # Hint: Return [x, y, op, display_result]
    return [x, y, op, display_result]

def check_answer(x, y, op, display_result, user_choice):

    if user_choice == True :
        if display_result == calc(x, y, op):
            return True
        else:
            return False
    else:
        if display_result == calc(x, y, op):
            return False
        else:
            return True




