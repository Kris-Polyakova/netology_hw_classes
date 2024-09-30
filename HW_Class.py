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
        gpa = sum(grades_list) / len(grades_list)
        return gpa

    def __str__(self):
        return ('Имя: ' + self.name + '\n' + 
                'Фамилия: ' + self.surname + '\n' + 
                'Средняя оценка за домашние задания: ' + str(self.get_gpa()) + 
                '\n' + 'Курсы в процессе изучения: ' +  ', '.join(self.courses_in_progress) +
                '\n' + 'Завершенные курсы:' + ', '.join(self.finished_courses))

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