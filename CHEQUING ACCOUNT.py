from MAIN import Account

class Chequing_Account(Account):
    def __init__(self, Account_Number, Account_Holder_Name, Rate_Interest, Current_Balance, Over_Draft_Limit):
        self.Over_Draft_Limit = Over_Draft_Limit
        super().__init__(Account_Number, Account_Holder_Name, Rate_Interest, Current_Balance)

    def withdrawl(self, amount):
        if self.Current_Balance + self.Over_Draft_Limit < amount:
            return f"WITHDRAWL OF {amount} HAS BEEN DECLINED DUE TO OVERDRAFT LIMIT (Chequing Acount)"
        
        else:
            super().withdraw(amount)
            return f"WITHDRAWL OF {amount} HAS BEEN APPROVED (Chequing Acount)"
        

