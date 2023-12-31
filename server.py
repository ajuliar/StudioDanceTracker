from flask import (Flask, render_template, request, flash, session, redirect)
from flask_babel import Babel, gettext
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


babel = Babel(app)

app.config['LANGUAGES'] = {
    'en': 'English',
    'pt': 'Portugues'
}


def get_locale():
    print("get_locale")

    # return 'pt'
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def homepage():
    """View homepage"""


    return render_template('homepage.html')



@app.route("/login", methods=["POST"])
def admin_login():

    email = request.form.get('email')
    password = request.form.get("password")

    admin = crud.get_admin_by_email(email)

    if admin and password == admin.password:
        session["current_admin"] = admin.email
        flash(gettext("Logged in"))
        
    else:
        flash(gettext("Login incorrect"))
        return redirect("/")

    return redirect("/admins")

@app.route("/logout", methods=["POST"])
def admin_logout():

    if session.get("current_admin"):
        del session["current_admin"]

    flash(gettext('You have been logged out!'))

    return redirect("/")


@app.route("/admins")
def get_admin():
    """View admin info"""

    if 'current_admin' not in session:
        flash(gettext("Please log in"))
        return redirect("/")
    
    else:

        admins = crud.get_all_admin()

        return render_template ("admin.html", admins=admins, current_admin=session['current_admin'])

@app.route("/students")
def all_students():
    """view all students"""

    if 'current_admin' not in session:
        flash(gettext("Please log in"))
        return redirect("/")
    
    else:

        students = crud.get_all_students()

    return render_template("all_students.html", students=students, current_admin=session['current_admin'])


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

    flash(gettext("Student information added successfully."))

    return redirect("/students")



@app.route("/students/<student_id>/edit", methods=["GET", "POST"])
def edit_student(student_id):

    student = crud.get_student_by_id(student_id)

    if request.method == 'POST':
        if student:
    
            f_name = request.form["f_name"]
            l_name = request.form["l_name"]
            email = request.form["email"]
            phone = request.form["phone"]
            address = request.form["address"]

            student = crud.update_student(student_id, f_name, l_name, email, phone, address)

            db.session.add(student)
            db.session.commit()

    return redirect (f"/students/{student_id}")

@app.route("/students/<student_id>/delete", methods=['POST'])
def delete_student(student_id):

    student = crud.get_student_by_id(student_id)

    db.session.delete(student)
    db.session.commit()

    return redirect("/students")

    

@app.route("/classes")
def all_classes():
    """View all classes"""

    if 'current_admin' not in session:
        flash(gettext("Please log in"))
        return redirect("/")
    
    else:

        classes = crud.get_all_classes()

    return render_template("all_classes.html", classes=classes, current_admin=session['current_admin'])


@app.route("/classes/<class_id>")
def get_class(class_id):
    """Show details on a class"""

    a_class = crud.get_class_by_id(class_id)

    return render_template("class_details.html", a_class=a_class)


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

    flash(gettext("Class information added successfully."))

    return redirect("/classes")


@app.route("/classes/<class_id>/edit", methods=["GET", "POST"])
def edit_class(class_id):

    a_class = crud.get_class_by_id(class_id)

    if request.method == 'POST':
        if a_class:

            class_name = request.form["class_name"]
            instructor_id = request.form["instructor_id"]
            schedule = request.form["schedule"]
            start_date = request.form["start_date"]
            end_date = request.form["end_date"]
            

            a_class = crud.update_class(class_id, class_name, schedule, start_date, end_date, instructor_id)

            db.session.add(a_class)
            db.session.commit()
    
    return redirect(f"/classes/{class_id}")

@app.route("/classes/<class_id>/delete", methods=['POST'])
def delete_class(class_id):

    a_class = crud.get_class_by_id(class_id)

    db.session.delete(a_class)
    db.session.commit()

    return redirect("/classes")



@app.route("/classes/class-statistics", methods=[ "GET","POST"])
def class_stat():
    """Filter students/classes with start date and end date"""
    
    student_total = 0

    if request.method == 'POST':
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")

        class_list = crud.get_all_classes_by_date(start_date, end_date)
    

        for a_class in class_list:
            student_total += len(a_class.students)

    
        return render_template("class_stats.html", student_total=student_total, start_date=start_date, end_date=end_date)
    else:
        return render_template("class_stats.html", student_total=student_total, start_date="", end_date="")
            


@app.route("/instructors")
def all_instructors():
    """View all instructors"""

    if 'current_admin' not in session:
        flash(gettext("Please log in"))
        return redirect("/")
    
    else:

        instructors = crud.get_all_instructors()

    return render_template("all_instructors.html", instructors=instructors, current_admin=session['current_admin'])


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

    flash(gettext("Instructor added successfully"))

    return redirect("/instructors")

@app.route("/instructors/<instructor_id>/edit", methods=["GET", "POST"])
def edit_instructor(instructor_id):

    instructor = crud.get_instructor_by_id(instructor_id)

    if request.method == 'POST':
        if instructor:

            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            phone = request.form["phone"]

            instructor = crud.update_instructor(instructor_id, first_name, last_name, email, phone)

            db.session.add(instructor)
            db.session.commit()

    return redirect (f"/instructors/{instructor_id}")


@app.route("/instructors/<instructor_id>/delete", methods=['POST'])
def delete_instructor(instructor_id):

    instructor = crud.get_instructor_by_id(instructor_id)

    db.session.delete(instructor)
    db.session.commit()

    return redirect("/instructors")


@app.route("/enroll-students")
def enroll_students():

    if 'current_admin' not in session:
        flash(gettext("Please log in"))
        return redirect("/")
    
    else:

        students = crud.get_all_students()
        classes = crud.get_all_classes()
    
    return render_template("enroll-students.html", students=students, classes=classes, current_admin=session['current_admin'])

@app.route("/enroll-students", methods=["POST"])
def add_class():

    get_student = request.json.get("get_student")
    get_class = request.json.get("get_class")

    a_class = crud.get_class_by_id(get_class)
    student = crud.get_student_by_id(get_student)

    
    if student not in a_class.students:
        a_class.students.append(student)
        
    db.session.commit()

    return {
            "success": True,
            "status": gettext("The student %(f_name)s has been enrolled to %(class_name)s class", f_name = student.f_name, class_name=a_class.class_name)
        } 

@app.route("/calendar")
def calendar():

    if 'current_admin' not in session:
        flash(gettext("Please log in"))
        return redirect("/")
    
    else:
        classes = crud.get_all_classes()
        events = []
        
        for a_class in classes:
            
            class_dict = {"title": a_class.class_name,
                        "start": a_class.start_date,
                        "end": a_class.end_date}
            events.append(class_dict)

    return render_template("calendar.html", events=events, current_admin=session['current_admin'])







if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)