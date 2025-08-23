import bcrypt
import random
import os

from dotenv import load_dotenv

load_dotenv()

MAIL_CONFIG = {
    "MAIL_SERVER": "smtp.gmail.com",
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USERNAME": "dennismthairu@gmail.com",
    "MAIL_PASSWORD": os.getenv("MAIL_PASS"),
    "MAIL_DEFAULT_SENDER": ("PhysioGuide", "dennismthairu@gmail.com")
}


def hash_password(password: str) -> str:
    password = password.encode("utf-8")
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed.decode("utf-8")

def check_password(password: str, hashed: str) -> bool:
    password = password.encode("utf-8")
    hashed = hashed.encode("utf-8")
    return bcrypt.checkpw(password, hashed)



# password = input("Enter password: ")
# hashed = hash_password(password)
# print("Hashed password:", hashed)

# new_password = input("Re-enter password: ")
# if check_password(new_password, hashed):
#     print("Password match!")
# else:
#     print("Password does not match.")