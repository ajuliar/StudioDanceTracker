from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined 

@app.route('/')
def homepage():
    """View homepage"""

    return render_template('homepage.html')

@app.route("/students")
def all_students():
    """view all students"""

    students = crud.get_all_students()

    return render_template("all_students.html", students=students)


@app.route("/students/<student_id>") 
def show_student(student_id):
    """show details on a student"""
    
    student = crud.get_student_by_id(student_id)


    return render_template("student_details.html", student=student)
    

@app.route("/classes")
def all_classes():
    """View all classes"""

    classes = crud.get_all_classes()

    return render_template("all_classes.html", classes=classes)

@app.route("/classes/<class_id>")
def get_class(class_id):
    """Show details on a class"""

    a_class = crud.get_class_by_id(class_id)

    return render_template("class_details.html", a_class=a_class)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)