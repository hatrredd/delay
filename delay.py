import random
import time

def print_random_line(lines, delay):
    while True:
        random_line = random.choice(lines)
        time.sleep(delay)
        print(random_line)

text = [
    "qwerty",
    "asdfgj",
    "yuiioppoi",
    "zxcvvnb",
    "po[p[gfd",
    "1234568",
    "9898tufd"]

delay = 0.5
print_random_line(text, delay)