from datetime import datetime
class Contacts:
    def __init__(self):
        self.contacts = []

    def printcontacts(self):
        i = 1
        for x in self.contacts:
            print(f"{i}. Name is {x['name']}")
            print(f"number is {x['phone number']}")
            print(f"date of birth is {x['date of birth']}")
            print("")
            i = i + 1


    def addcontact(self, contract):
        self.contacts.append(contract)

    def delete(self,name):
        for x in self.contacts:
            if x["name"] == name:
                self.contacts.remove(x)
                break

    def edit(self,dic):
        for x in self.contacts:
            if x["name"] == dic["name"]:
                x["name"] = dic["name"]
                x["phone number"] = dic["phone number"]
                x["date of birth"] = dic["date of birth"]
















one = 3
x = Contacts()
dic = {}
while one != 0:
    print("press 1 for new contact ")
    print("press 2 to show all contacts")
    print("press 4 to edit a contact")
    print("press 5 to delete a contact")
    one = input( )

    if one == "1":
        name = input("give contact name ")
        number = input("give contact number ")
        print("print date of bith in day/month/year format")
        print("for example 02/10/2004")
        dateofbirth = input()

        formateddate = datetime.strptime(dateofbirth, "%d/%m/%Y").date()
        dic = {"name" : name,
               "phone number" : number,
               "date of birth" : formateddate}
        x.addcontact(dic)
        print("done")
        one = input("press 0 to go back ")
    if one == "2":
        x.printcontacts()
        one = input("press 0 to go back ")
    if one == "4":
        newname = input("who`s info you want to change")
        newnum = input("newnumber?")
        newage = input("changed birth year in d/m/y format?")
        formateddate = datetime.strptime(newage, "%d/%m/%Y" ).time()
        
        dic = {"name":newname,
               "phone number": newnum,
               "date of birth": newage}

        x.edit(dic)
        print("done")
        one = input("press 0 to go back")
    if one == "5":
        delc = input("who do you want ro delete")
        x.delete(delc)
        print(x.contacts)
        one = input("press 0 to go back")














































