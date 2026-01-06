# bank_account.py

class BankAccount:
    def __init__(self):
        self._balance = 0
        self._observers = []

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def register_observer(self, callback):
        self._observers.append(callback)

    def unregister_observer(self, callback):
        self._observers.remove(callback)

    def notify_observers(self, event):
        for callback in self._observers:
            callback(event)

    def deposit(self, amount):
        self._balance += amount
        event = {'type': 'deposit', 'amount': amount, 'balance': self._balance}
        self.notify_observers(event)

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            event = {'type': 'withdraw', 'amount': amount, 'balance': self._balance}
            self.notify_observers(event)
        else:
            print("Insufficient balance")


# Observer functions
def sms_service(event):
    print(f"SMS: Type: {event['type']}, Amount: {event['amount']}, Balance: {event['balance']}")

def email_service(event):
    print(f"Email: Type: {event['type']}, Amount: {event['amount']}, Updated Balance: {event['balance']}")

def fraud_detection_service(event):
    if event['type'] == 'withdraw' and event['amount'] >= 10000:
        print(f"Possible Fraud Detected \nType: {event['type']}\nAmount: {event['amount']}")
