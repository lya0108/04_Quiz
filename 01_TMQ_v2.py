import random
import operator

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

def boundary_check(question, low=None, high=None, code = None, truefalse = None):

    situation = ""


    if low is not None and high is not None:
        situation = "both"

    elif low is not None and high is None:
        situation = "low only"
    
    while True:

        response = input(question).lower()
        if response == code:
            return response

        elif truefalse is not None:
            response = float(response)
            return response

        else:
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

def decorator(text, decoration, lines):

    ends = decoration * 5
    statement = "{} {} {}".format(ends, text, ends)
    text_length = len(statement)

    if lines == 3:
        print(decoration * text_length)
        print(statement)
        print(decoration * text_length)
        return ""

    elif lines == 2:
        print("|",statement,"|")
        return ""

    elif lines == 1:
        print(statement)
        return ""

    else:
        return ""

def instructions():
    print()
    print("You Will Be Asked For The Difficulty Of The Quiz\nYou Can Choose From 3 Difficulties")
    print("Easy(e), Normal(n), and Hard(h)")
    print()
    print("Then You Will Need To Type The Amount Of Rounds You Wish To Play")
    print("You Can Press Enter For Endless Mode And To Exit Endless Type 'xxx'")
    print("Then The Quiz Will Start :)\n")
    print("Here Are The Definitions For The Symbols")
    print("'+' = Addition\n'-' = Subtraction\n'𝑥' = Multiplication\n'/' = Division\n'^' = Powers\n'%' = Modulus\n")
    print("Easy = Addition, Subtraction, Multiplication")
    print("Normal = Addition, Subtraction, Multiplication, Division")
    print("Hard = Addition, Subtraction, Multiplication, Powers, Modulus\n")
    print("FYI: Modulus is Remainder\nGood Luck Have Fun\n\n")

# main routine
# color (personal preference)
print("\x1b[38;2;0;255;255m")

# lists for valid responses
maybe = ["yes", "no"]
difficulty = ["easy", "normal", "hard"]

# list to hold game history
game_history = []

# game intro
decorator("Welcome To Andy's Math Quiz", "=", 2)
print()

# asks user if they want the instructions
first_time = choice_checker("Would You Like To See The Instructions? ", maybe, "Please Enter Yes Or No")
if first_time == "yes":
    instructions()

# asks user for the difficulty they wish to play on
print()
diff_check = choice_checker("What Difficulty Would You Like To Play On? ", difficulty, "You Sure You've Read The Instructions? (Easy, Normal, Hard)")
print()

# easy mode - addition + subtraction
if diff_check == "easy":
    add_inc = 1
    mult_inc = 1
    # takes strings and makes them operators (from stack overflow)
    ops = {'+':operator.add, '-':operator.sub, '𝑥':operator.mul}

# normal mode - addition + subtraction + multiplication + floor division
if diff_check == "normal":
    add_inc = 10
    mult_inc = 2
    ops = {'+':operator.add, '-':operator.sub, '𝑥':operator.mul, '/':operator.truediv}

# hard mode - addition + subtraction + multiplication + floor division + powers + modulus
if diff_check == "hard":
    add_inc = 1000
    mult_inc = 3
    ops = {'+':operator.add, '-':operator.sub, '𝑥':operator.mul, '^':operator.pow, '%':operator.mod}


# main loop
end_game = "yes"
while end_game == "yes":

    # asks user for number of rounds
    rounds = boundary_check("How Many Rounds? <enter> For Endless\n", 1, None, "", None)

    rounds_played = 0

    num1 = 0
    num2 = 0

    game = ""
    while game == "":

        # ends game if you run out of rounds
        if rounds_played == rounds:
            print("You've Run Out Of Rounds!")
            break

        rounds_played += 1

        # randomly takes an operator from dictionary
        op = random.choice(list(ops.keys()))
        # generates numbers based on operator
        if op == "+" or op == "-":
            num1 = random.randint(10, 50 * add_inc)
            num2 = random.randint(10, 50 * add_inc)

        elif op == "𝑥" or op == "/" or op == "%":
            num1 = random.randint(2, 12 * mult_inc)
            num2 = random.randint(2, 12 * mult_inc)

        else:
            num1 = random.randint(3, 10)
            num2 = random.randint(3, 5)

        # gets operator and applies to the 2 numbers
        answer = ops.get(op)(num1,num2)
        # rounds to 1 decimal place
        true_answer = round(answer, 1)
        question = ("What is {} {} {}?\n".format(num1, op, num2))

        # headings
        if rounds == "":
            print()
            heading = decorator("Question {}".format(rounds_played), "=", 1)
        
        else:
            print()
            heading = decorator("Question {} of {}".format(rounds_played, rounds), "=", 1)

        # uses boundary_check as an integer checker
        # if op = division will allow decimals
        if op == "/":
            guess = boundary_check(question, None, None, "xxx", "")

        else:
            guess = boundary_check(question, None, None, "xxx", None)

        if guess == "xxx":
            break
        
        elif guess == true_answer:
            correct = "\x1b[38;2;0;255;100mCorrect\x1b[38;2;0;255;255m"
            print(correct)
        
        # tells user if they answered wrong then appends their mistake into the history
        elif guess != true_answer:             
            any_incorrect = 1
            incorrect = "\x1b[38;2;255;0;0mIncorrect\x1b[38;2;0;255;255m"
            print(incorrect)
            outcome = ("{}{}: {}\n{} is The Answer".format(question, guess, incorrect, true_answer))
            game_history.append(outcome)
        
    # if yes, restarts game
    print()
    end_game = choice_checker("Would You Like To Play Again ", maybe, "Please Type Yes Or No")



if any_incorrect == 1:
    # asks user if they want to see their mistakes
    print()
    results = choice_checker("Would You Like To See Your Mistakes? ", maybe, "Please Type Yes or No")
    
    if results == "yes":
        for item in game_history:
            print()
            print(item)

print()
decorator("Thank You For Playing", "=", 2)