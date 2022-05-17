from flask import request


def hello_world(name: str):
    if request.method == "POST":
        data = request.json

        name = data["name"]
        surname = data["surname"]
        age = int(data["age"])

        return f"Hello, {name} {surname}, you're {age} years old"

    else:
        return f"Hello, {name}"
