#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify, request, redirect, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    """return a JSON"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user():
    """register user"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Login user"""
    email = request.form.get("email")
    password = request.form.get("password")

    # Check login credentials
    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)

    # Set session_id as a cookie
    response = jsonify({'email': email, 'message': 'logged in'})
    response.set_cookie("session_id", session_id)

    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logout user"""
    session_id = request.cookies.get("session_id")

    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
