class Person:
    def __init__(self, fullname, age, is_married):
        self.fulname = fullname
        self.age = age
        self.married = is_married

    def introduce_myself(self):
        print(
            f'{self.fulname} \n {self.age}\n {self.married}\n')


Person_Info = Person('Rusya Buralkiev', 15, 'no')
Person_Info.introduce_myself()


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = {
            'key_work': 29-1,
            'grade': 8,
        }


Student_info = Student('Adil Baigaziev', 11, 'yes', 'da')
print(
    f'{Student_info.fulname}\n {Student_info.age}\n {Student_info.married}\n {Student_info.marks}')


# * 7-8 pynkt
class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = 30000

    def calculator_salary(self):
        bonus = 0
        if self.experience > 3:
            bonus = 0.05 * (self.experience - 3)
        return self.salary + (self.salary * bonus)


class Teache(Person):
    def __init__(self, fullname, age, is_married, experience, salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary

    def calculator_salary(self):
        starting_salary = self.salary
        if self.experience > 3:
            bonus = 0.05 * (self.experience - 3)
            return starting_salary * (1 + bonus)
        else:
            return starting_salary


teacher = Teache("Джонни Деп", 35, True, 8, 30000)
teacher.introduce_myself()
print("Зарплата:", teacher.calculator_salary())


def create_students():
    student1 = Student("Robert Dauni Mladshii", 16, False, {
                       "Math": 95, "History": 85, "English": 92})
    student2 = Student("Bob Brown", 17, False, {
                       "Math": 80, "History": 75, "English": 88})
    student3 = Student("Charlie White", 16, True, {
                       "Math": 90, "History": 88, "English": 94})
    print(student1, student2, student3)
    return [student1, student2, student3]


create_students()
