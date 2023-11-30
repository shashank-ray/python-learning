class Account:
    def __init__(self,Title=None,Balance=0):
        self.Title=Title
        self.Balance=Balance

class SavingsAccount(Account):
    def __init__(self,Title=None,Balance=0,InterestRate=0):
        super().__init_(Title,Balance)
        self.InterestRate=InterestRate
    