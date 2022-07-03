# takes 2 random integers and adds them then asks for answer
from random import randint

def questions():
    num1 = randint(10, 99)
    num2 = randint(10, 99)
    answer = num1 + num2
    quest1 = int(input("What is {} + {}? ".format(num1, num2)))
    print(quest1)

questions()