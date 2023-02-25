class User:
    name= 'no name provided'
    email=''
    password= '123'
    account_nnumber=2


class Employee(User):
    base_pay=6
    department= 'general'

class Customer(User):
    mailing_home= ''
    mailing_list= True
