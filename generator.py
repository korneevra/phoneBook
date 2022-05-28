import string
import random
from random import randint


def listGen(n):
    lst = []
    for i in range(n):
        note = nameGen() + ';' + nameGen() + ';' + phoneGen(10) + ';' + commentGen(randint(1, 5))
        lst.append(note)
    return lst


def nameGen():
    letters = string.ascii_lowercase
    uplet = string.ascii_uppercase
    return random.choice(uplet) + ''.join(random.choice(letters) for i in range(randint(1, 10)))


def commentGen(words):
    letters = string.ascii_lowercase
    comment = nameGen()
    for i in range(1, words):
        comment += ' ' + ''.join(random.choice(letters) for i in range(randint(1, 15)))
    return comment


def phoneGen(length):
    return '+7' + ''.join(random.choice(string.digits) for i in range(length))



