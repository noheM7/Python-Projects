class User:
    name= 'nohe'
    email='nmesfien@gmail.com'
    password= '123'
    account_nnumber=2

def getLogininfo(self):
    entry_name= input("enter your name: ")
    entry_email= input("enter your email: ")
    entry_password=input("Enter your password: ")
    if (entry_email==self.email and entry_password==self.password):
        print("Welcome Back, {}".format(entry_name))
    else:
        print("The pasword and email is incorrect")

class Employee(User):
    base_pay=6
    department= "General"
    pin_number= "1234"


def getLogininfo(self):
    entry_name= input("enter your name: ")
    entry_email= input("enter your email: ")
    entry_pin=input("Enter your password: ")
    if (entry_email==self.email and entry_pin==self.pin_number):
        print("Welcome Back, {}".format(entry_name))
    else:
        print("The pasword and email is incorrect")

    customer=User()
    customer.getLogininfo()

    manager= Employee()
    manager.getLogininfo()



