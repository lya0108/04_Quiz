import random

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

def num_guess():
    while True:

        response = input("How Many Rounds Would You Like ")

        round_error = "Please type either <enter> or an integer more than 0"
        
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    print()
                    continue

            except ValueError:
                print(round_error)
                print()
                continue

        return response


# main routine

rounds_played = 0

# ask user for # number of rounds, <enter> for infinite mode
rounds = num_guess()

end_game = "no"
while end_game == "no":

    # rounds heading
    print()
    if rounds == "":
        heading = "Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose = boundary_check("enter a number", None, None, "xxx", None)
    if choose == "xxx":
        break

    rounds_played += 1

    # end game if # of rounds requested have been played
    if rounds_played == rounds:
        break
    
print("Thank you for playing")