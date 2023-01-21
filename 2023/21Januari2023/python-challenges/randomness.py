import random

def random_number():
    selectedValue   =   random.choice(range(1, 100))
    return selectedValue

randomNumber    =   random_number()
print(randomNumber)