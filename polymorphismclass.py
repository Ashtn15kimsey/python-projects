#parent class user
class user:
    name = "Ash"
    email = "ash19@gmail.com"
    password = "3421abc"


    def getLoginInfo(self):
        entry_name = input("Enter your name:")
        entry_email = input("Enter your email here:")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#child class Employee
class Employee(user):
    base_pay = 18.00
    department = "Mechanic"
    pin_number = "2323"

#This is the same method in the parent class "User".
#The difference is that, instead of suing entry_password we're using entry_pin.

    def GetLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("The pin or email is incorrect")

#The following code invokes the methods inside each class for User and Employee.

customer = user()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()
