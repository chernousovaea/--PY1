from random import choice
import random, string

n = 8
pas_char = string.ascii_letters + string.digits

def get_random_password() -> str:
    password = ""

    for i in range(n):
        password = password + random.choice(pas_char)

    return password

print(get_random_password())
