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


    def editable_stuff(self, new):
        super().editable_stuff(new)

        if new.get("emploee_id") != None:
            self.emploee_id = new["emploee_id"]
        if new.get("work") != None:
            self.work = new["work"]
        if new.get("salary") != None:
            self.salary = new["salary"]

    def editable_atributes(self):

        return super().editable_atributes()+ ['emploee_id', 'work', 'salary']






