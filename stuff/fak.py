from faker import Faker
import re


def name():
    pattern = r' '
    fake = Faker()
    fake.pystr(min_chars=10, max_chars=12)
    username = fake.name()
    final_username = re.sub(pattern, 'xyz', username)

    return final_username
