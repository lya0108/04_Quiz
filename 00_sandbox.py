import random
import operator

diff_check = input("diff? ")

ops = {'-':operator.sub}
op = random.choice(list(ops.keys()))
num1 = random.randint(3, 10)
num2 = random.randint(3, 5)

# gets operator and applies to the 2 numbers
answer = ops.get(op)(num1,num2)
if diff_check == "easy":
    if answer < 0:
        answer = ops.get(op)(num2,num1)

question = int(input("what is {} {} {}".format(num1, num2)))