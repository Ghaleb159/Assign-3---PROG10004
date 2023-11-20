from MAIN import Account

class Saving_Account(Account):
    def __init__(self, Account_Number, Account_Holder_Name, Rate_Interest, Current_Balance, Minimum_Balance):
        self.Minimum_Balance = Minimum_Balance
        super().__init__(Account_Number, Account_Holder_Name, Rate_Interest, Current_Balance)

    def withdraw(self, amount):
        if self.Current_Balance - amount < self.Minimum_Balance:
            return f"INSUFFICIENT FUNDS OF WITHDRAWL AMOUNT OF {amount} (SAVING ACCOUNT)"
        
        else:
            super().withdraw(amount)
            return f"WITHDRAWL AMOUNT OF {amount} HAS BEEN SUCCESSFUL (SAVING ACCOUNT)"
        
    