class Student:
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number

    def __add__(self, other_student):
        return Student("", self.number + other_student.number)

    def __lt__(self, st):
        return self.number < st.number

    def __eq__(self, st):
        return self.number == st.number

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return str(self)

    def __ne__(self, st):
        return self.number != st.number

    def __gt__(self, st):
        return self.name > st.number


a = Student('Peter', 3)
b = Student('Mike', 4)
c = Student('John', 5)
d = Student('Kelvin', 3)

print(a + b + d)
print(a != d)
print(b < c)
