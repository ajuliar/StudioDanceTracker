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



admin = crud.create_admin(email, password)
model.db.session.add(admin)
model.db.session.commit()



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