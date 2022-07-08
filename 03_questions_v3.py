# takes 2 random integers and a random operator to applies it to them then asks for answer
from audioop import add
import operator
import random

def choice_checker(question, valid_list, error):

    valid = False
    while not valid:
        
        # asks user for choice
        response = input(question).lower()

        # checks if input is in list
        for item in valid_list:
            if response == item[0] or response == item:
                return item
        
        print(error)
        print()

difficulty = ["easy", "normal", "hard"]

# asks user for the difficulty they wish to play on
diff_check = choice_checker("What Difficulty Would You Like To Play On? ", difficulty, "Please type Easy(e), Normal(n), Hard(h)")
print()

# easy mode - addition + subtraction + multiplication (no negatives and no decimals)
if diff_check == "easy":
    # add_inc and mult_inc multiply the range of the random integers
    add_inc = 1
    mult_inc = 1
    # takes strings and makes them operators (from stack overflow)
    ops = {'+':operator.add, '-':operator.sub, '𝑥':operator.mul}

# normal mode - addition + subtraction + multiplication + division (allow negatives and no decimals)
if diff_check == "normal":
    # comment: line 129
    add_inc = 10
    mult_inc = 2
    # comment: line 132
    ops = {'+':operator.add, '-':operator.sub, '𝑥':operator.mul, '/':operator.truediv}

# hard mode - addition + subtraction + multiplication + division + powers + modulus (allow negatives and allow decimals)
if diff_check == "hard":
    # comment: line 129
    add_inc = 1000
    mult_inc = 3
    # comment: line 132
    ops = {'+':operator.add, '-':operator.sub, '𝑥':operator.mul, '/':operator.truediv, '^':operator.pow, '%':operator.mod}


# randomly takes an operator from dictionary
op = random.choice(list(ops.keys()))
# generates numbers based on operator
if op == "+" or op == "-":
    num1 = random.randint(10, 50 * add_inc)
    num2 = random.randint(10, 50 * add_inc)

elif op == "*" or op == "//" or op == "%":
    num1 = random.randint(2, 12 * mult_inc)
    num2 = random.randint(2, 12 * mult_inc)

else:
    num1 = random.randint(3, 10)
    num2 = random.randint(3, 5)

default_question = ("What is {} {} {}?\n".format(num1, op, num2))
invert_question = ("What is {} {} {}?\n".format(num2, op, num1))

# gets operator and applies to the 2 numbers
answer = ops.get(op)(num1,num2)
if diff_check == "easy":
    if answer < 0:
        answer = ops.get(op)(num2,num1)
        question = invert_question

    else:
        question = default_question

elif diff_check == "normal":
    if op == "/":
        num3 = num2 * num1
        answer = num3/num2
        question = ("What is {} {} {}?\n".format(num3, op, num2))

    else:
        question = default_question


else:
    question = default_question

user_input = int(input(question))
if user_input == answer:
    print("Correct")
else:
    print("Incorrect")