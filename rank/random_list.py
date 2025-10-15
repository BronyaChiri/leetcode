import random

def random_list(n):
    b = []
    for i in range(n):
        a = random.randint(1,100)
        b.append(a)
    print(b)
    return b

random_list(30)
