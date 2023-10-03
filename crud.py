"""CRUD operations"""

from model import db, Admin, Student, Instructor, Class, StudentClass, connect_to_db

def create_user(email,password):
    """Create and return a new admin."""

    admin = Admin(email=email, password=password)

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