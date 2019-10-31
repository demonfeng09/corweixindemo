import random

def get_random_char(number):
    val_list = []
    for num in range(0,number):
        val_list.append(chr(random.randint(0x4e00,0x9fbf)))
    return "".join(val_list)

print(get_random_char(3))