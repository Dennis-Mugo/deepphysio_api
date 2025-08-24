from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
import json
import database
import utils
import mail_html
import dynamic_mail
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config.update(utils.MAIL_CONFIG)
mail = Mail(app)



def hello():
    res = {
        "data": {},
        "errors": [],
        "status": 200
    }
    res["data"] = {"hello": "world"}
    return jsonify(res)

def pre_create_user():
    res = {
        "data": {},
        "errors": [],
        "status": 200
    }

    try:

        body = json.loads(request.data)
        email = body.get("email")
        if not email:
            res["errors"].append("Email is required.")
            res["status"] = 400
            return jsonify(res)
        user = database.get_user(email=email)
        if user:
            res["errors"].append("Email already exists.")
            res["status"] = 400
            return jsonify(res)
        res["data"] = {"success": True}
        return jsonify(res)

    except Exception as e:
        res["errors"].append(str(e))
        res["status"] = 400
        return jsonify(res)

def create_user():
    res = {
        "data": {},
        "errors": [],
        "status": 200
    }
    try:
        body = json.loads(request.data)
        user_id = database.create_user(body)
        res["data"] = {"userId": user_id}
    except Exception as e:
        res["errors"].append(str(e))
        res["status"] = 400
    return jsonify(res)

def sign_in_user():
    res = {
        "data": {},
        "errors": [],
        "status": 200
    }
    try:
        body = json.loads(request.data)
        user_obj = database.sign_in_user(body["email"], body["password"])
        del user_obj["password"]
        res["data"] = user_obj
    except Exception as e:
        res["errors"].append(str(e))
        res["status"] = 400
    return jsonify(res)

def send_verification_email():
    res = {
        "data": {},
        "errors": [],
        "status": 200
    }

    try:
        body = json.loads(request.data)
        email = body.get("email")
        token = body.get("token")

        msg = Message(
            subject="PhysioGuide Email Verification",
            recipients=[email]
        )
        email_body = mail_html.email_verification(email, token)
        msg.html = email_body
        mail.send(msg)
        res["data"] = {"success": True}
        return jsonify(res)
    
    except Exception as e:
        res["errors"].append(str(e))
        res["status"] = 400
        return jsonify(res)
    

def public_mail_send():
    res = {
        "data": {},
        "errors": [],
        "status": 200
    }

    try:
        body = json.loads(request.data)
        api_key = body.get("apiKey", None)
        if not api_key or api_key not in dynamic_mail.mapping:
            res["errors"].append("Invalid API key.")
            res["status"] = 400
            return jsonify(res)

        email = body.get("recipientEmail", None)
        subject = body.get("subject", None)
        app_name = body.get("appName", None)
        sender_email = body.get("senderEmail", None)

        if not all([email, subject, app_name, sender_email]):
            res["errors"].append("Missing required fields.")
            res["status"] = 400
            return jsonify(res)

        html = body.get("html", None)
        email_body = body.get("emailBody", None)
        if not html and not email_body:
            res["errors"].append("Missing email content.")
            res["status"] = 400
            return jsonify(res)

        result = dynamic_mail.send_dynamic_email(
            sender_email=sender_email,
            sender_name=app_name,
            sender_password=dynamic_mail.mapping[api_key],
            recipient_email=email,
            subject=subject,
            html=html,
            body=email_body
        )

        if "error" in result:
            res["errors"].append(result["error"])
            res["status"] = 400
        else:
            res["data"] = {"success": True}
        return jsonify(res)

    except Exception as e:
        res["errors"].append(str(e))
        res["status"] = 400
        return jsonify(res)


app.add_url_rule("/", "hello", hello, methods=["GET"])
app.add_url_rule("/create_user", "create_user", create_user, methods=["POST"])
app.add_url_rule("/sign_in_user", "sign_in_user", sign_in_user, methods=["POST"])
app.add_url_rule("/send_verification_email", "send_verification_email", send_verification_email, methods=["POST"])
app.add_url_rule("/pre_create_user", "pre_create_user", pre_create_user, methods=["POST"])
app.add_url_rule("/public_mail_send", "public_mail_send", public_mail_send, methods=["POST"])

if __name__=='__main__':
    app.run(debug=True)
