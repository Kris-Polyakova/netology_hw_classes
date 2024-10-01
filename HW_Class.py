class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress 
                      and course in lecturer.courses_attached and 1 <= grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]         
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_gpa(self):
        grades_list = [mark for marks in self.grades.values() for mark in marks]
        if len(grades_list) == 0:
            return 0
        else:
            gpa = sum(grades_list) / len(grades_list)
            return gpa
            
    def __str__(self):
        return ('Имя: ' + self.name + '\n' + 
                'Фамилия: ' + self.surname + '\n' + 
                'Средняя оценка за домашние задания: ' + str(self.get_gpa()) + 
                '\n' + 'Курсы в процессе изучения: ' +  ', '.join(self.courses_in_progress) +
                '\n' + 'Завершенные курсы: ' + ', '.join(self.finished_courses))

    def __eq__(self, other):
        return self.get_gpa() == other.get_gpa()

    def __ne__(self, other):
        return not self.get_gpa()

    def __lt__(self, other):
        return self.get_gpa() < other.get_gpa()

    def __le__(self, other):
        return self.get_gpa() <= other.get_gpa()

    def __gt__(self, other):
        return self.get_gpa() > other.get_gpa()

    def __ge__(self, other):
        return self.get_gpa() >= other.get_gpa()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def get_gpa(self):
        grades_list = [mark for marks in self.grades.values() for mark in marks]
        if len(grades_list) == 0:
            return 0
        else:
            gpa = sum(grades_list) / len(grades_list)
            return gpa

    def __str__(self):
        return ('Имя: ' + self.name + '\n' + 
                'Фамилия: ' + self.surname + '\n' + 
                'Средняя оценка за лекции: ' + str(self.get_gpa()))

    def __eq__(self, other):
        return self.get_gpa() == other.get_gpa()

    def __ne__(self, other):
        return not self.get_gpa()

    def __lt__(self, other):
        return self.get_gpa() < other.get_gpa()

    def __le__(self, other):
        return self.get_gpa() <= other.get_gpa()

    def __gt__(self, other):
        return self.get_gpa() > other.get_gpa()

    def __ge__(self, other):
        return self.get_gpa() >= other.get_gpa()


class Reviever(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached 
                      and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname


student1 = Student('Мария','Романова','жен.')
student2 = Student('Евгений','Семёнов','муж.')

lector1 = Lecturer('Станислав','Комаров')
lector2 = Lecturer('Оксана','Щукина')

reviever1 = Reviever('Сергей','Возницкий')
reviever2 = Reviever('Александр','Борисов')

reviever1.courses_attached.append('ООП и работа с API')
reviever2.courses_attached.append('ООП и работа с API')

lector1.courses_attached.append('ООП и работа с API')
lector2.courses_attached.append('Основы Python')

student1.courses_in_progress.append('ООП и работа с API')
student1.courses_in_progress.append('Основы Python')
student1.finished_courses.append('Как учиться онлайн')

student2.courses_in_progress.append('ООП и работа с API')
student2.finished_courses.append('Основы Python')

reviever1.rate_hw(student1, 'ООП и работа с API', 6)
reviever1.rate_hw(student2, 'ООП и работа с API', 8)
reviever2.rate_hw(student1, 'ООП и работа с API', 7)   
reviever2.rate_hw(student2, 'ООП и работа с API', 10)

student1.rate_lecturer(lector1,'ООП и работа с API', 9)
student2.rate_lecturer(lector1,'ООП и работа с API', 6)

average_grade_student1 = student1.get_gpa()
average_grade_lector1 = lector1.get_gpa()

print(f'СТУДЕНТ \n{student1}')
print(f'ЛЕКТОР \n{lector1}')
print(f'ЭКСПЕРТ \n{reviever1}')

print(student1 < student2)
print(lector1 == lector2)

students_list = [student1, student2]
course_name = 'ООП и работа с API'
lecturer_list = [lector1, lector2]

def get_gpa_students(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            grades_list = [marks for marks in student.grades[course]]
            all_grades += grades_list
    if len(all_grades) != 0:
        return sum(all_grades) / len(all_grades)
    else:
        return 0
    
print(get_gpa_students(students_list, course_name))

def get_gpa_lecturer(lectors, course):
    all_grades = []
    for lector in lectors:
        if course in lector.grades:
            grades_list = [marks for marks in lector.grades[course]]
            all_grades += grades_list
    if len(all_grades) != 0:
        return sum(all_grades) / len(all_grades)
    else:
        return 0
    
print(get_gpa_lecturer(lecturer_list, course_name))