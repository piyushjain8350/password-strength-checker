import re
import math
import random
import string

COMMON_PASSWORDS = set()
with open("common_passwords.txt", "r", encoding="utf-8") as file:

    for line in file:
        COMMON_PASSWORDS.add(line.strip())

def password_entropy(password):
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`" for c in password):
        charset += 32
    entropy = len(password) * math.log2(charset) if charset else 0
    return entropy

def check_password_strength(password):
    if password in COMMON_PASSWORDS:
        return "Weak (Common Password)"
    entropy = password_entropy(password)
    if len(password) < 6:
        return "Very Weak"
    elif len(password) < 8:
        return "Weak"
    elif entropy < 40:
        return "Moderate"
    elif entropy < 60:
        return "Strong"
    else:
        return "Very Strong"

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
