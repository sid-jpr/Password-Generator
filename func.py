from string import ascii_letters, digits
import random

"""Generate Password for Given Size"""
def pwGenerate(size = 5):
    s1 = ascii_letters
    s2 = digits
    s3 = "!$%^&*- _~"
    s = s1 + s2 + s3

    length = size.get()
    new_pw = ""
    colorVal = ""

    for c in range(length):
        new_pw += random.choice(s)

    if length <= 8:
        msg = 'VERY WEAK'
        color = "#6d0001"
    elif length <= 10:
        msg = 'WEAK'
        color = "#cc0000"
    elif length <= 12:
        msg = 'DECENT'
        color = "#fc8600"
    elif length <= 14:
        msg = 'GOOD'
        color = "#eae200"
    elif length <= 16:
        msg = 'STRONG'
        color = "#9ff400"
    elif length <= 18:
        msg = 'VERY STRONG'
        color = "#007715"
    elif length > 18:
        msg = 'EXCELLENT'
        color = "#001fef"
    else:
        pass

    return new_pw, msg, color
