from person import Person

class Student(Person):
    def __init__(self, name, number, dateofbirth, gpa, roll_num, father_name):
        super().__init__(name, number, dateofbirth)

        self.gpa = gpa
        self.roll_num = roll_num
        self.father_name = father_name

    def printinfo(self):
        super().printinfo()

        print(f"gpa is {self.gpa}")
        print(f"roll number is {self.roll_num}")
        print(f"father is {self.father_name}")













