import random
import operator
import time

# functions
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

def boundary_check(question, low=None, high=None, code = None):
    
    situation = ""


    if low is not None and high is not None:
        situation = "both"

    elif low is not None and high is None:
        situation = "low only"
    
    while True:

        response = input(question).lower()
        if response == code:
            return response

        try:
            response = int(response)

            # checks input is not too high or low if both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print("Please Enter a Number Between {} and {}".format(low, high))
                    continue

            elif situation == "low only":
                if response < low:
                    print("Please Enter a Number That is More Than or Equal to {}".format(low))
                    continue

            return response

        # checks input is an integer
        except ValueError:
            print("Please Enter an Integer (ie: a Number Which Does Not Have a Decimal)")
            continue

def instructions():
    print("Math")
    print()
    print()


# main routine
# color (personal preference)
print("\x1b[38;2;0;255;255m")

# lists for valid responses
maybe = ["yes", "no"]
difficulty = ["easy", "normal", "hard"]

# list to hold game history
game_history = []

# game intro
print("Welcome To Andy's Math Quiz")
print()

# asks user if they want the instructions
first_time = choice_checker("Would You Like To See The Instructions? ", maybe, "Please Enter Yes Or No")
if first_time == "yes":
    instructions()

# asks user for the difficulty they wish to play on
diff_check = choice_checker("What Difficulty Would You Like To Play On? ", difficulty, "You Sure You've Read The Instructions?")
print()

# easy mode - addition + subtraction
if diff_check == "easy":
    diff_mult = 1
    mult_inc = 1
    # takes strings and makes them operators (from stack overflow)
    ops = {'+':operator.add, '-':operator.sub, '*':operator.mul}

# normal mode - addition + subtraction + multiplication + floor division
if diff_check == "normal":
    diff_mult = 10
    mult_inc = 2
    ops = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv, '//':operator.floordiv}

# hard mode - addition + subtraction + multiplication + floor division + powers + modulus
if diff_check == "hard":
    diff_mult = 100
    mult_inc = 3
    ops = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv, '//':operator.floordiv, '**':operator.pow, '%':operator.mod}


# main loop
end_game = "yes"
while end_game == "yes":

    # asks user for number of rounds
    rounds = boundary_check("How Many Rounds? ", 1, None, "")

    rounds_played = 0

    num1 = 0
    num2 = 0

    game = ""
    while game == "":

        if rounds_played == rounds:
            print("You've Run Out Of Rounds!")
            break

        rounds_played += 1

        # randomly takes an operator from dictionary
        op = random.choice(list(ops.keys()))
        # generates numbers based on operator
        if op == "+" or op == "-":
            num1 = random.randint(10, 50 * diff_mult)
            num2 = random.randint(10, 50 * diff_mult)

        elif op == "*" or op == "/" or op == "//" or op == "%":
            num1 = random.randint(2, 12 * mult_inc)
            num2 = random.randint(2, 12 * mult_inc)

        else:
            num1 = random.randint(3, 10)
            num2 = random.randint(3, 5)

        # gets operator and applies to the 2 numbers
        answer = ops.get(op)(num1,num2)
        round(answer)
        question = ("What is {} {} {}?\n".format(num1, op, num2))

        # headings
        if rounds == "":
            print()
            heading = ("Question {}".format(rounds_played))
            print()
        
        else:
            print()
            heading = ("Question {} of {}".format(rounds_played, rounds))
            print()

        # uses boundary_check as an integer checker
        guess = boundary_check(question)

        if guess == answer:
            print("\x1b[38;2;0;255;100mCorrect")
            print("\x1b[38;2;0;255;255m")

        elif guess != answer:
            print("\x1b[38;2;255;0;0Incorrect")
            print("\x1b[38;2;0;255;255m")
        
    
    end_game = choice_checker("Would You Like To Play Again ", maybe, "Please Type Yes Or No")

        