import sys

host = str(sys.argv[1])

class Bank_Account:

    def __init__(self, filePath):
        self.path = filePath
        with open(filePath, 'r') as f:
            self.balance = int(f.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.path, 'w') as f:
            f.write(str(self.balance))

account = Bank_Account(host)
print(account.balance)
