class Person:
    def __init__(self, name, number, dateofbirth):
     self.name = name
     self.number = number
     self.dateofbirth = dateofbirth


    def printinfo(self):
        print(f"name is {self.name}")
        print(f"number is {self.number}")
        print(f"date of birth is {self.dateofbirth}")

    def editable_stuff(self, new):


        self.name = new["name"]
        self.number = new["number"]
        self.dateofbirth = new["dateofbirth"]

    def editable_atributes(self):
        return ['name', 'number', 'dateofbirth']




