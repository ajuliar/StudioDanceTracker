"""Models for Dance Studio app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Admin(db.Model):
    """A admin"""
    __tablename__ = "admins"

    admin_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(150))

    def __repr__(self):
        """Show info about the admin"""

        return f"<Admin admin_id={self.admin_id} email={self.email}>"
    


class Student(db.Model):
    """A student"""
    __tablename__ = "students"

    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    f_name = db.Column(db.String(50), nullable=False)
    l_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(25))
    address = db.Column(db.String(150))

    classes = db.relationship("Class", secondary="students_classes", back_populates="students")


    def __repr__(self):
        """Show info about the student"""

        return f"<Student name={self.f_name, self.l_name} email={self.email}>"
    

    
class Instructor(db.Model):
    """An instructor"""

    __tablename__ = "instructors"

    instructor_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(25))

    classes = db.relationship("Class", back_populates="instructor")


    def __repr__(self):
        """Show information about the instructor"""

        return f"<Instructor instructor_id={self.instructor_id} name={self.first_name}>"
    



class Class(db.Model):
    """A Class"""

    __tablename__ = "classes"

    class_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    class_name = db.Column(db.String(25), nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey("instructors.instructor_id"))
    schedule = db.Column(db.String(150))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)


    instructor = db.relationship("Instructor", back_populates="classes")
    students = db.relationship("Student", secondary="students_classes", back_populates="classes")


    def __repr__(self):
        """Show information about a class"""

        return f"<Class class_id={self.class_id} class_name={self.class_name}"
    


class StudentClass(db.Model):
    """Students and classes"""

    __tablename__ = "students_classes"

    
    student_class_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.student_id"))
    class_id = db.Column(db.Integer, db.ForeignKey("classes.class_id"))



def connect_to_db(flask_app, db_uri="postgresql:///students", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)