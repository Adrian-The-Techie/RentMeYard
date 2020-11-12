import random
import string

def genUrl():
    url=''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])

    return url