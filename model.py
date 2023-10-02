"""Models for Dance Studio app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class Admin(db.Model):
    """A admin"""
    __tablename__ = "admins"

    admin_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        """Show info about the admin"""

        return f"<Admin admin_id={self.admin_id} email={self.email}>"
    

    class Student(db.Model):
        """A student"""
    __tablename__ = "students"

    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    f_name = db.Column(db.String(25), nullable=False)
    l_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(25))
    address = db.Column(db.String)

    def __repr__(self):
        """Show info about the student"""

        return f"<Student student_id={self.admin_id} email={self.email}>"
