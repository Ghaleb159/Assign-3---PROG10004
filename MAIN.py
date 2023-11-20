class Account:

    def __init__(self, Account_Number, Account_Holder_Name, Rate_Interest, Current_Balance)
        self.Account_Number = Account_Number
        self.Account_Holder_Name = Account_Holder_Name
        self.Rate_Of_Interest = Rate_Interest
        self.Current_Balance = Current_Balance

    def getAccount_Number(self):
        return self.Account_Number
        
    def getAccount_Holder_Name(self):
        return self.Account_Holder_Name
        
    def getRate_Of_Interest(self):
        return self.Rate_Of_Interest
        
    def getCurrent_Balance(self):
        return self.Current_Balance
        
    def setAccount_Holder_Name(self, name):
        self.Account_Holder_Name = name
        
    def setRate_Of_Interest(self, rate):
        self.Rate_Of_Interest = rate

    def deposit (self, amount):
        self.Current_Balance += amount
        return f"CAD has been successfully deposited {amount}"

    def withdraw(self, amount):
        self.Current_Balance += amount
        return f"CAD has been successfully withdrawn {amount}"
    
    

        

            
        
        
        
        