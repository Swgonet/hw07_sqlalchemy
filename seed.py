from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from models import Teacher, Group, Student, Subject, Grade
import datetime
import random
from faker import Faker

engine = create_engine('postgresql://postgres:567123@localhost/hw07')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

groups = []
for _ in range(3):
    group = Group(name=fake.word())
    session.add(group)
    groups.append(group)

teachers = []
for _ in range(3):
    teacher = Teacher(fullname=fake.name())
    session.add(teacher)
    teachers.append(teacher)

students = []
for _ in range(30):
    student = Student(fullname=fake.name(), group=random.choice(groups))
    session.add(student)
    students.append(student)

subjects = []
subject_names = [fake.word() for _ in range(5)]
for name in subject_names:
    subject = Subject(name=name, teacher=random.choice(teachers))
    session.add(subject)
    subjects.append(subject)

for student in students:
    for subject in subjects:
        grade = Grade(
            grade=random.randint(1, 100),
            date_of=fake.date_between(start_date='-1y', end_date='today'),
            student=student,
            subject=subject
        )
        session.add(grade)


if __name__ == '__main__':
    try:
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()