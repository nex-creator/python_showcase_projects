from bank_account import BankAccount, sms_service, email_service, fraud_detection_service

def main():
    # Create accounts
    ba1 = BankAccount()
    ba2 = BankAccount()

    # Register observers
    for ba in [ba1, ba2]:
        ba.register_observer(sms_service)
        ba.register_observer(email_service)
        ba.register_observer(fraud_detection_service)

    # Transactions for ba1
    ba1.deposit(15000)
    ba1.withdraw(10000)

    # Transactions for ba2
    ba2.deposit(500)
    ba2.withdraw(1000)
    ba2.withdraw(400)


if __name__ == "__main__":
    main()
