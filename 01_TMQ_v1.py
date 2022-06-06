

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

def decorator(text, decoration, lines):

    ends = decoration * 5
    statement = "{} {} {}".format(ends, text, ends)
    text_length = len(statement)

    if lines == "3":
        print(decoration * text_length)
        print(statement)
        print(decoration * text_length)
        return ""

    elif lines == "2":
        print("|",statement,"|")

    elif lines == "1":
        print(statement)
        return ""

    else:
        return ""

def boundary_check(question, low=None, high=None, exit_code = None):
    
    situation = ""


    if low is not None and high is not None:
        situation = "both"

    elif low is not None and high is None:
        situation = "low only"
    
    while True:

        response = input(question).lower()
        if response == exit_code:
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

def check_rounds():
    while True:
        
        print()
        num_rounds = input("\nRounds: ")

        round_error = "Please Type Either [enter] for Endless Mode\n or an Integer That is More Than 0"
        # check rounds is an integer more than 0 for finite mode
        if num_rounds != "":
            try:
                num_rounds = int(num_rounds)

                # if num_rounds less than 1 go back to start of loop
                if num_rounds < 1:
                    print(round_error)
                    print()
                    continue
            
            # if num_rounds is not an integer go back to start of loop
            except ValueError:
                print(round_error)
                print()
                continue

        return num_rounds

def instructions():
  print("instructions")


# main routine
# code for colour
print("\x1b[38;2;0;255;255m")

# lists of valid responses
yes_no_list = ["yes", "no"]
diff = ["Easy", "Normal", "Hard", "Asian"]

# list to hold game history / summary
game_summary = []

# asks if the user has played before, if not shows instructions
intro = choice_checker("Is This Your First Time Playing? ", yes_no_list, "Please Type Yes(y) Or No(n)")
if intro == "yes":
  instructions()

rounds = check_rounds()

difficulty = choice_checker("What Difficulty Would You Like To Play On? ", diff, "Please Type Easy(E), Normal(N), Or Hard(H)")

end_game = "no"
while end_game == "no":
    yuyj = 1
