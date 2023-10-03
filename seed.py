"""Script to seed database."""

import os
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb students")
os.system('createdb students')
model.connect_to_db(server.app)
model.db.create_all()

fname = "Anna"
lname = "Test"
email = "admin@test.com"
password = "test123"
admin = crud.create_admin(fname,lname,email, password)
model.db.session.add(admin)
model.db.session.commit()


students = [
    {
        "f_name": "Tara",
        "l_name": "Davis",
        "email": "tara@student.com",
        "phone": "123-345-6789",
        "address": "123 Oak St",
    },
    {
        "f_name": "Alice",
        "l_name": "Smith",
        "email": "alice@student.com",
        "phone": "123-345-9876",
        "address": "123 Myrtle St",
    },
    {
        "f_name": "John",
        "l_name": "Williams",
        "email": "john@student.com",
        "phone": "123-345-3344",
        "address": "123 Main St",
    }
]

students_in_db = []
for student in students:
    f_name, l_name, email,phone, address = (
        student["f_name"],
        student["l_name"],
        student["email"],
        student["phone"],
        student["address"],
    )

    db_student = crud.create_student(f_name, l_name, email, phone, address)
    students_in_db.append(db_student)

model.db.session.add_all(students_in_db)
model.db.session.commit()


instructors = [
    {   
        "first_name": "Jane",
        "last_name": "Johnson",
        "email": "jane@instructor.com",
        "phone": "123-543-6789",  

        },
    {   
        "first_name": "Sarah",
        "last_name": "Smith",
        "email": "sarah@instructor.com",
        "phone": "321-345-6789",  

    }
        
        
]

instructors_in_db = []
for instructor in instructors:
    first_name, last_name, email, phone = (
        instructor["first_name"],
        instructor["last_name"],
        instructor["email"],
        instructor["phone"],
    )

    db_instructor = crud.create_instructor(first_name, last_name, email, phone)
    instructors_in_db.append(db_instructor)

model.db.session.add_all(instructors_in_db)
model.db.session.commit()

db_classes = [
    {   
        "class_name": "Ballet Beginner",
        "schedule": "Mon, Wed, Fri - 2pm to 3pm",
        "start_date": "2023,01,25",
        "end_date": "2023,07,05",

    },
    {
        "class_name": "Jazz",
        "schedule": "Wed, Fri - 4pm to 5pm",
        "start_date": "2023,01,25",
        "end_date": "2023,07,05",
    },
    {
        "class_name": "Zumba",
        "schedule": "Tue, Thu - 4pm to 5pm",
        "start_date": "2023,01,25",
        "end_date": "2023,07,05",
    }
]

classes_in_db = []
for db_class in db_classes:
    class_name, schedule, start_date, end_date = (
        db_class["class_name"],
        db_class["schedule"],
        db_class["start_date"],
        db_class["end_date"],
    )

    class_database = crud.create_class(class_name, schedule, start_date, end_date)
    classes_in_db.append(class_database)

model.db.session.add_all(classes_in_db)
model.db.session.commit()
