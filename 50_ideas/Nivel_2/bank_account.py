class BankAccount():
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self):
        add = int(input('¿Cuánto dinero va a agregar?'))
        self.balance = self.balance + add
        print('Su saldo es de $' + str(self.balance))
    
    def withdraw(self):
        less = int(input('¿Cuánto va a retirar?'))
        self.balance = self.balance - less
        print('Su saldo es de $' + str(self.balance))
    
    def display_balance(self):
        print('Su saldo es de $' + str(self.balance))

Adonai = BankAccount('Adonai', 'Vazquez', 123, 'debito', 9797, 10000)


Adonai.deposit()
print('-'*30)
Adonai.withdraw()
print('-'*30)
Adonai.display_balance()

