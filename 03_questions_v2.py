# takes 2 random integers and a random operator to applies it to them then asks for answer
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

# easy mode - addition + subtraction
if diff_check == "easy":
    print("You Chose Easy Mode")
    diff_mult = 1
    # takes strings and makes them operators (from stack overflow)
    ops = {'+':operator.add, '-':operator.sub}

# normal mode - addition + subtraction + multiplication + floor division
if diff_check == "normal":
    print("You Chose Normal Mode")
    diff_mult = 10
    mult_inc = 2
    ops = {'+':operator.add, '-':operator.sub, '*':operator.mul, '//':operator.floordiv}

# hard mode - addition + subtraction + multiplication + floor division + powers + modulus
if diff_check == "hard":
    print("You Chose Hard Mode")
    diff_mult = 100
    mult_inc = 3
    ops = {'+':operator.add, '-':operator.sub, '*':operator.mul, '//':operator.floordiv, '**':operator.pow, '%':operator.mod}

# randomly takes an operator from dictionary
op = random.choice(list(ops.keys()))
# generates numbers based on operator
if op == "+" or op == "-":
    num1 = random.randint(10, 50 * diff_mult)
    num2 = random.randint(10, 50 * diff_mult)

elif op == "*" or op == "//" or op == "%":
    num1 = random.randint(2, 12 * mult_inc)
    num2 = random.randint(2, 12 * mult_inc)

else:
    num1 = random.randint(3, 10)
    num2 = random.randint(3, 5)

# gets operator and applies to the 2 numbers
answer = ops.get(op)(num1,num2)
question = ("What is {} {} {}?\n".format(num1, op, num2))
user_input = int(input(question))
if user_input == answer:
    print("Correct")
else:
    print("Incorrect")