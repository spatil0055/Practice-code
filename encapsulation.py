class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self,amt):
        self.balance += amt
        
    def show(self):
        print(self.balance)
    
B = Bank("Somnath",20000)
B.deposit(4000)
B.show()