from uuid import uuid4 as v4
import time
from firebase_config.config import db
import utils

def create_user(data):
    user_id = str(v4())
    email = data.get("email")
    if not email:
        raise ValueError("Email is required")
    if get_user(email=email):
        raise ValueError("Email already exists")
    if "password" not in data or not data["password"]:
        raise ValueError("Password is required")
    
    data["userId"] = user_id
    data["createdAt"] = time.time()
    data["password"] = utils.hash_password(data["password"])

    db.collection("deepphysio_users").document(user_id).set(data)
    return user_id

def get_user(user_id="", email=""):
    if user_id:
        user_ref = db.collection("deepphysio_users").document(user_id)
    elif email:
        user_ref = db.collection("deepphysio_users").where("email", "==", email).limit(1)
    else:
        return None

    user_list = user_ref.stream()

    for user in user_list:
        doc = user.to_dict()
        return doc
    return None

def sign_in_user(email, password):
    user = get_user(email=email)
    if not user:
        raise ValueError("User not found")
    if not utils.check_password(password, user["password"]):
        raise ValueError("Invalid password")
    return user
