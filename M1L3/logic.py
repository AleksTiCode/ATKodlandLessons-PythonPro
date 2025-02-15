import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def smile_pass(pass_length):
    elements = "❤️🪂🐷🍴👖🐈⏳☠️👋🎉❌➕👀👁️❓🔑📒🎨😭🏡👿🤣"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password