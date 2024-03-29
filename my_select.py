from sqlalchemy import func, desc, create_engine, select, and_
from models import Teacher, Group, Student, Subject, Grade
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:567123@localhost/hw07')

Session = sessionmaker(bind=engine)
session = Session()



def select_1():
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Student).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result


def select_2():
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                                .join(Grade).join(Subject)\
                                .group_by(Student.id).order_by(desc(func.avg(Grade.grade))).first()
    return result

def select_3():
    result = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
            .join(Student, Group.id == Student.group_id).join(Grade, Student.id == Grade.student_id)\
            .join(Subject, Grade.subject_id == Subject.id)\
            .group_by(Group.id).all()
    return result

def select_4():
    result = session.query(func.round(func.avg(Grade.grade), 2).label('overall_avg_grade')).scalar()
    return result

def select_5():
    result = session.query(Subject.name).join(Teacher).all()
    return result

def select_6():
    result = session.query(Student.fullname).join(Group).all()
    return result

def select_7():
    result = session.query(Student.fullname, Grade.grade).all()
    return result

def select_8():
    result = session.query(func.round(func.avg(Grade.grade), 2).label('teacher_avg_grade'))\
                                .join(Subject).join(Teacher).scalar()
    return result

def select_9():
    result = session.query(Subject.name).join(Grade).join(Student).distinct().all()
    return result

def select_10():
    result = session.query(Subject.name).join(Teacher).join(Grade).join(Student)\
                                        .distinct().all()
    return result

def select_11():
    subquery = (select(func.max(Grade.date_of)).join(Student).filter(and_(
        Grade.subject_id == 2, Student.group_id == 3
    ))).scalar_subquery()
    result = session.query(Student.id, Student.fullname, Grade.date_of)\
            .select_from(Grade)\
            .join(Student)\
            .filter(and_(Grade.subject_id == 2, Student.group_id == 3, Grade.date_of == subquery))
    return result

if __name__ == "__main__":
    print(select_1())
    # print(select_2())
    # print(select_3())
    # print(select_4())
    # print(select_5())
    # print(select_6())
    # print(select_7())
    # print(select_8())
    # print(select_9())
    # print(select_10())
    # print(select_11())
