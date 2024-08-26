from person import Person

class Employe(Person):
    def __init__(self, name, number, dateofbirth, emploee_id, work, salary):
        super().__init__(name, number, dateofbirth)
        self.emploee_id = emploee_id
        self.work = work
        self.salary = salary
        

    def printinfo(self):
        super().printinfo()

        print(f"emploees id is {self.emploee_id}")
        print(f"emploees  is {self.work}")
        print(f"emploees salary is {self.salary}")


