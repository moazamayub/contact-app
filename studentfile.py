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


    def editable_stuff(self, new):
        super().editable_stuff(new)

        self.gpa = new["gpa"]
        self.roll_num = new["roll_num"]
        self.father_name = new["father_name"]

    def editable_atributes(self):
        return super().editable_atributes() + ['gpa', 'roll_num', 'father_name']







