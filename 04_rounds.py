import random



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
    choose = int(input("enter a number"))

    

    rounds_played += 1

    # end game if # of rounds requested have been played
    if rounds_played == rounds:
        break
    
print("Thank you for playing")