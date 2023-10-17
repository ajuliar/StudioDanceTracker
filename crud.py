"""CRUD operations"""

from model import db, Admin, Student, Instructor, Class, StudentClass, connect_to_db

def create_admin(fname, lname, email,password):
    """Create and return a new admin."""

    admin = Admin(fname=fname, lname=lname, email=email, password=password)

    return admin

def create_student(f_name, l_name, email, phone, address):
    """Create and return a new student"""

    student = Student(
        f_name=f_name,
        l_name=l_name,
        email=email,
        phone=phone,
        address=address,
    )

    return student


def create_instructor(first_name, last_name, email, phone):
    """Create and return a new instructor"""

    instructor = Instructor(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
    )

    return instructor


def create_class(class_name, instructor_id, schedule, start_date, end_date):
    """Create a new class"""

    a_class = Class(
        class_name=class_name,
        instructor_id=instructor_id,
        schedule=schedule,
        start_date=start_date,
        end_date=end_date,
        
    )

    return a_class


def get_all_admin():

    return Admin.query.all()

def get_admin_by_id(admin_id):
    
    return Admin.query.get(admin_id)


def get_student_by_id(student_id):
    

    return Student.query.get(student_id)



def get_instructor_by_id(instructor_id):

    return Instructor.query.get(instructor_id)


def get_class_by_id(class_id):

    return Class.query.get(class_id)

def get_all_students():
    """Return all students"""

    return Student.query.all()

def get_all_instructors():
    """Return all instructors"""

    return Instructor.query.all()

def get_all_classes():
    """return all classes"""

    return Class.query.all()

def get_all_classes_by_date(start_date, end_date):

    return Class.query.filter(Class.start_date >= start_date, Class.end_date <= end_date).all()

def get_admin_by_email(email):

    return Admin.query.filter(Admin.email == email).first()



def update_student(student_id, f_name, l_name, email, phone, address):

    student= Student.query.get(student_id)

    student.f_name = f_name
    student.l_name = l_name
    student.email = email
    student.phone = phone
    student.address = address

    db.session.commit()
    
    return student
    

def update_class(class_id, class_name, schedule, start_date, end_date, instructor_id):

    a_class = Class.query.get(class_id)

    a_class.class_name = class_name
    a_class.instructor_id = instructor_id
    a_class.schedule = schedule
    a_class.start_date = start_date
    a_class.end_date = end_date
    

    db.session.commit()
    
    return a_class

def update_instructor(instructor_id, first_name, last_name, email, phone):

    instructor = Instructor.query.get(instructor_id)

    instructor.first_name = first_name
    instructor.last_name = last_name
    instructor.email = email
    instructor.phone = phone

    db.session.commit()

    return instructor




if __name__ == '__main__':
    from server import app
    connect_to_db(app)