
import secrets
import string


def generate_login():
    
    random_digits = f"{secrets.randbelow(1000):03d}"
    return f"alexey_mironov56{random_digits}@gmail.com"


def generate_password(length=6):
    
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))