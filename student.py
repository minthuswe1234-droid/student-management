students = []

def add_student(name):
    students.append(name)

def show_students():
    for student in students:
        print(student)

def delete_student(name):
    if name in students:
        students.remove(name)        

def search_student(name):
    if name in students:
        print(f"{name} found")       