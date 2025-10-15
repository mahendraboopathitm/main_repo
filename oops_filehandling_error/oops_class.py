class employee:
    def __init__(self,name,age,id,phn,address):
        self.name=name
        self.age=age
        self.id=id
        self.phn=phn
        self.address=address
    def welcome(self):
        print(f"welcome this is {self.name} and i am {self.age} years old")
    def getaddress(self):
        print(f"hi i am {self.name} and I'm {self.age} years old.this my employee {self.id}and this is my contact number {self.phn} and currently i resided in{self.address}")

s2=employee("boopathi",22," id db054","987654321","pg hostel in hosur near bus stand")
 
s2.getaddress()   
class Bank_account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount  
            # print(self.balance)
            print(f"{self.owner}:{self.balance}")
    def withdraw(self,amounts):
        if amounts<self.balance:
            self.balance-=amounts
            print(f"{self.owner}:{self.balance}")

        else:
            print("transaction inavalid")   
a=Bank_account("boopathi")
b=Bank_account("jai")

b.deposit(100)
b.withdraw(56)
a.deposit(1000)
