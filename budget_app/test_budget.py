from budget import Category, create_spend_chart

def run_demo():
    # Create categories
    food = Category("Food")
    clothing = Category("Clothing")
    auto = Category("Auto")

    # Deposits
    food.deposit(1000, "initial deposit")
    clothing.deposit(500, "deposit")
    auto.deposit(300, "deposit")

    # Withdrawals
    food.withdraw(105.55, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    clothing.withdraw(75.50, "clothes")
    auto.withdraw(50, "fuel")

    # Transfers
    food.transfer(50, clothing)

    # Print ledgers
    print("\n--- Food Ledger ---")
    print(food)
    print("\n--- Clothing Ledger ---")
    print(clothing)
    print("\n--- Auto Ledger ---")
    print(auto)

    # Print spending chart
    print("\n--- Spending Chart ---")
    print(create_spend_chart([food, clothing, auto]))


if __name__ == "__main__":
    run_demo()
