students = ['Harry', 'Hermione','Ron','Luna']
students2 = ['Maria', 'Rose', 'John', 'Daniel']

def wizard(students_list):
    for name in students_list:
        print(f'{name}, you are a wizard')

wizard(students2)

def student_house():
    for i, name in enumerate(students):
        students[i] = f'{name} - house: Griffyndor'

student_house()
print(students)





