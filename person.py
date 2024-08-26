class Person:
    def __init__(self, name, number, dateofbirth):
     self.name = name
     self.number = number
     self.dateofbirth = dateofbirth


    def printinfo(self):
        print(f"name is {self.name}")
        print(f"number is {self.number}")
        print(f"date of birth is {self.dateofbirth}")

