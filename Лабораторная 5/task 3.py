from random import randint
import random

n = 15
def get_unique_list_numbers() -> list[int]:
    new_list = []
    for i in range(n):
        new_i = random.randint(-10, 10)
        while new_list.count(new_i) > 0:
            new_i = random.randint(-10, 10)
        new_list.append(new_i)
    return new_list

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
