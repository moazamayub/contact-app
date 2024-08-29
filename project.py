from datetime import datetime
from person import Person
from emploeefile import Employe
from studentfile import Student

class Contacts:
    def __init__(self):
        self.contacts = []

    def printcontacts(self):
        i = 1
        for x in self.contacts:
            x.printinfo()

            i = i + 1

    def addcontact(self, contract):
        self.contacts.append(contract)

    def delete(self, name):
        for x in self.contacts:
            if x.name == name:
                self.contacts.remove(x)
                break


one = 3
x = Contacts()


dic = {}
while one != 0:
    print("press 1 for new contact ")
    print("press 2 to show all contacts")
    print("press 4 to edit a contact")
    print("press 5 to delete a contact")
    one = input()

    if one == "1":
        name = input("give contact name ")
        number = input("give contact number ")
        print("print date of bith in day/month/year format")
        print("for example 02/10/2004")
        dateofbirth = input()

        formateddate = datetime.strptime(dateofbirth, "%d/%m/%Y").date()


        print("done")
        print("now time for specific data bitch")
        print("press 1 if he is a emploee")
        print("press 2 if he is a student")
        specific_data = input()
        if specific_data == "1":
            id = input("what is employee id")
            work = input("what does employee do")
            salary = input("how much he is payed")
            info = Employe(name, number, formateddate, id, work, salary)
            x.addcontact(info)
        if specific_data == "2":
            gpa = input("whats his gpa")
            roll_num = input("whats his roll number")
            father_name = input("whats his daddy name")
            info = Student(name, number, formateddate, gpa, roll_num, father_name)
            x.addcontact(info)
        one = input("press 0 to go back ")
    if one == "2":
        x.printcontacts()
        one = input("press 0 to go back ")
    if one == "4":
        array = []
        content = {}
        selected_content = None
        newname = input("who`s info you want to change")
        for contact in x.contacts:
            if newname == contact.name:
                array = contact.editable_atributes()
                selected_content = contact
                break

        for i in array:
            if i == 'dateofbirth':
                print("enter in 2/04/2005 format")
            data = input(f"enter {i}")

            if data != '':
                content[i] = data

        selected_content.editable_stuff(content)


        print("done")
        one = input("press 0 to go back")
    if one == "5":
        delc = input("who do you want ro delete")
        x.delete(delc)
        print(x.contacts)
        one = input("press 0 to go back")
