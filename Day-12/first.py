class BankAccount:
    intreset_rate = 3

    def __init__(self,acc_holder,balance = 0):
        self.acc_holder = acc_holder
        self.balance = balance
        

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited INR {amount} \nCURRENT BALANCE INR {self.balance}")


    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"Debited INR {amount} \nCURRENT BALANCE INR {self.balance}")
    # When you call this function on an object it runs only for that function
    # Instance method
    def set_intrest_rate(self, new_rate):
        pass
    # But intrest rate should be changed to all 
    # objects so we can write it as a class variable

    def set_intrest_rate(cls, new_rate):
        cls.intreset_rate = new_rate
        print(f"The updated intrest rate to {cls.intreset_rate} pct")

    set_intrest_rate = classmethod(set_intrest_rate)

    def validate_account_number(account_number):
        if len(str(account_number)) == 12 and str(account_number).isdigit():
            return True
    
    validate_account_number = staticmethod(validate_account_number)


if __name__ == "__main__":

    acc1 = BankAccount("Anil",5000)

    if(BankAccount.validate_account_number('854796230123')):

        # acc1 = ("Anil",5000)
        acc1.deposit(500)
        acc1.withdraw(200)

        BankAccount.set_intrest_rate(6)
