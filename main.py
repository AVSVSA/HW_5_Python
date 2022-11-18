class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lect(self, prepod, course, grade):
        if isinstance(prepod, Lecturer) and course in prepod.courses_attached and course in self.courses_in_progress and grade<=10 and grade > 0:
            if course in prepod.grades:
                prepod.grades[course] += [grade]
            else:
                prepod.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_gr(self):
        sum_gr = 0
        count_gr = 0
        for course in self.grades.items():
            for gr in course[1]:
                sum_gr += gr
                count_gr += 1
        if count_gr:
            return (sum_gr / count_gr)
        else:
            return (0)

    def __str__(self):
        res = f'Имя: {self.name}  \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.__average_gr()} \nКурсы в процессе изучения:' + ','.join(self.courses_in_progress) + '\nЗавершенные курсы:' + ','.join(self.finished_courses)
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не сравнивайте яйцо с курицей')
            return
        return self.__average_gr() < other.__average_gr()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and grade<=10 and grade > 0:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}  \nФамилия: {self.surname}'
        return res

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average_gr(self):
        sum_gr = 0
        count_gr = 0
        for course in self.grades.items():
            for gr in course[1]:
                sum_gr += gr
                count_gr += 1
        if count_gr:
            return (sum_gr / count_gr)
        else:
            return (0)

    def __str__(self):
        res = f'Имя: {self.name}  \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.__average_gr()} '
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не сравнивайте курицу с яйцом')
            return
        return self.__average_gr() < other.__average_gr()


def course_students_rate (stud_list, course_name):
    sum_gr = 0
    count_gr = 0
    for student in stud_list:
        if course_name in student.grades:
            sum_gr += sum(student.grades[course_name])
            count_gr += len(student.grades[course_name])
    if count_gr:
        print(f'Средняя оценка студентов по курсу {course_name}: {round(sum_gr/count_gr,2)}')
    else:
        print(f'По курсу {course_name} нет оценок')

def course_lectors_rate (lector_list, course_name):
    sum_gr = 0
    count_gr = 0
    for lector in lector_list:
        if course_name in lector.grades:
            sum_gr += sum(lector.grades[course_name])
            count_gr += len(lector.grades[course_name])
    if count_gr:
        print(f'Средняя оценка лектора по курсу {course_name}: {round(sum_gr/count_gr,2)}')
    else:
        print(f'По лекциям курса {course_name} нет оценок')

# Полевые испытания

reviewer_1 = Reviewer('John', 'Pupkin')
reviewer_2 = Reviewer('Jack', 'Daniels')
lector_1 = Lecturer('Nikolas', 'Martini')
lector_2 = Lecturer('Vasily', 'Ivanov')
student_1 = Student('Ruoy', 'Eman', 'M')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['JavaScript']
student_1.finished_courses += ['GIT']
student_2 = Student('Lora', 'Palmer', 'W')
student_2.courses_in_progress += ['GIT']
student_2.courses_in_progress += ['Python']

lector_list = [lector_1, lector_2]
students_list = [student_1, student_2]

reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['GIT']
reviewer_2.courses_attached += ['JavaScript']
lector_1.courses_attached += ['JavaScript']
lector_1.courses_attached += ['GIT']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2,'Python', 9)
reviewer_2.rate_hw(student_1, 'JavaScript', 10)
student_1.rate_lect(lector_1, 'JavaScript', 10)
student_2.rate_lect(lector_1, 'GIT', 10)
reviewer_1.rate_hw(student_2, 'GIT', 8)

print(reviewer_2.__str__())
print(lector_1.__str__())
print(student_1.__str__())
print(student_2.__str__())

print(student_2.__lt__(student_1))
print(lector_1.__lt__(student_1))
print(student_1.__lt__(lector_2))

course_students_rate(students_list, 'Python')
course_lectors_rate(lector_list, 'GIT')
course_lectors_rate(lector_list, 'Python' )