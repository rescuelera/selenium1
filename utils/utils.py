import random
import string


def random_string(string_len=7):
    sets = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.choices(sets, k=string_len))


def random_email():
    return 'ex_test_' + random_string(string_len=12) + "@yopmail.com"