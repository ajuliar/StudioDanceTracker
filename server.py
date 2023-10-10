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


@app.route("/admins")
def get_admin():
    """View admin info"""

    admins = crud.get_all_admin()

    return render_template ("admin.html", admins=admins)



# @app.route("/admins", methods=["POST"])
# def register_admin():
#     """Create an admin"""

#     email = request.form.get("email")
#     password = request.form.get("password")

#     admin = crud.get_admin_by_email

#     if admin:
#         flash("Cannot create account with that email. Please try again")
    
#     else:
#         admin = crud.create_admin(email,password)
#         db.session.add(admin)
#         db.session.commit()
#         flash("Account created! Please log in.")
    
#     return redirect("/")


@app.route("/login", methods=["POST"])
def admin_login():

    email = request.form.get('email')
    password = request.form.get("password")

    admin = crud.get_admin_by_email(email)

    if not admin and password != admin.password:
        flash("Login incorrect")
    else:
        session["current_admin"] = admin.email
        flash("Logged in")

    return redirect("/")




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


@app.route("/students/create-student", methods=["POST"])
def create_student():
    """Create a new student"""

    f_name = request.form.get("f_name")
    l_name = request.form.get("l_name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    address = request.form.get("address")

    student = crud.create_student(f_name, l_name, email, phone, address)

    db.session.add(student)
    db.session.commit()

    flash("Student information added successfully.")

    return redirect("/students")



@app.route("/students/<student_id>/edit", methods=["POST"])
def edit_student(student_id):



    

@app.route("/classes")
def all_classes():
    """View all classes"""

    classes = crud.get_all_classes()

    return render_template("all_classes.html", classes=classes)



@app.route("/classes/create-classes", methods=["POST"])
def create_classes():
    """create a new class"""

    class_name = request.form.get("class_name")
    instructor_id = request.form.get("instructor_id")
    schedule = request.form.get("schedule")
    start_date = request.form.get("start_date")
    end_date = request.form.get("end_date")

    a_class = crud.create_class(class_name, instructor_id, schedule, start_date, end_date)

    db.session.add(a_class)
    db.session.commit()

    flash("Class information added successfully.")

    return redirect("/classes")


@app.route("/classes/<class_id>")
def get_class(class_id):
    """Show details on a class"""

    a_class = crud.get_class_by_id(class_id)

    return render_template("class_details.html", a_class=a_class)


@app.route("/instructors")
def all_instructors():
    """View all instructors"""

    instructors = crud.get_all_instructors()

    return render_template("all_instructors.html", instructors=instructors)


@app.route("/instructors/<instructor_id>")
def get_instructor(instructor_id):
    """Show instructors details"""

    instructor = crud.get_instructor_by_id(instructor_id)

    return render_template("instructor_details.html", instructor=instructor)


@app.route("/instructors/create-instructor", methods=["POST"])
def create_instructor():
    """Add a new instructor"""

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    phone = request.form.get("phone")

    instructor = crud.create_instructor(first_name, last_name, email, phone)

    db.session.add(instructor)
    db.session.commit()

    flash("Instructor added successfully")

    return redirect("/instructors")








if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)