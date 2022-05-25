from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://artem@localhost:5432/students"

db = SQLAlchemy(app)


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(50))
    pin = db.Column(db.String(50))

    def __init__(self, id, name, city, addr, pin):
        self.id = id
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "addr": self.addr,
            "pin": self.pin
        }


def add_student():
    if request.method == "POST":
        data = request.json
        name = data["name"]
        city = data["city"]
        addr = data["addr"]
        pin = data["pin"]

        std = Students(1, name, city, addr, pin)

        db.session.add(std)
        db.session.commit()

        return "OK"

    else:
        return "Need POST"


def list_students():
    students = Students.query.all()
    students_array = [s.to_dict() for s in students]

    return {
        "students": students_array
    }


app.add_url_rule("/students/add", "add_students", add_student, methods=["GET", "POST"])
app.add_url_rule("/students", "list_students", list_students, methods=["GET"])
