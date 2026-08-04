#Create Acccount class with 2 Attributes - balance and account no.
#Create methods for debit,credit and printing the balance

class Account:
    def __init__(self,balance,account_number):
        self.balance = balance
        self.acc_no = account_number

    #debit method
    def debit(self,withdraw):
        self.balance -=withdraw
        print("Rs.",withdraw,"was debited")
        print("Total balance=",self.balance)

    #credit
    def credit(self,withdraw):
        self.balance+=withdraw
        print("RS.",withdraw,"was credited")
        print("Total balance=",self.balance)

    # Print the blance
    def get_balance(self):
        print("Total balance = ",self.balance)

acc1 = Account(250255,1257854)
print(acc1.balance)
print(acc1.acc_no)
acc1.debit(50000)
acc1.credit(25000)
acc1.get_balance()
        