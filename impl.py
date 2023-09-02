from flask import request

users = []


def get_greeting():
    return "Hello, world!", 200


def get_basic():
    return "test", 200


def create_user():
    user_data = request.json  # Assuming the request is in JSON format
    firstname = user_data['firstname']
    lastname = user_data['lastname']

    # Perform any additional processing or validation here
    # For now, let's just store the user in the users list
    users.append({'firstname': firstname, 'lastname': lastname})

    return 'User created successfully', 200


def get_users():
    return users, 200

