class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        """Add a deposit to the ledger."""
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        """Attempt a withdrawal; return True if successful, False otherwise."""
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        """Return the current balance based on ledger entries."""
        return sum(entry['amount'] for entry in self.ledger)

    def transfer(self, amount, category):
        """Transfer amount from this category to another category."""
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, description=f'Transfer to {category.name}')
        category.deposit(amount, description=f'Transfer from {self.name}')
        return True

    def check_funds(self, amount):
        """Check if enough balance is available."""
        return self.get_balance() >= amount

    def __str__(self):
        """Return a string representation of the category ledger."""
        title = self.name.center(30, '*')
        lines = [title]
        for entry in self.ledger:
            desc = entry['description'][:23]
            amt = f"{entry['amount']:>7.2f}"
            lines.append(f"{desc:<23}{amt}")
        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)


def create_spend_chart(categories):
    """Return a bar chart showing percentage spent by category."""
    # Step 1: calculate spending per category
    spent = []
    for category in categories:
        total = sum(-entry['amount'] for entry in category.ledger if entry['amount'] < 0)
        spent.append(total)

    total_spent = sum(spent)

    # Step 2: calculate percentage per category, rounded down to nearest 10
    percentages = [int((amount / total_spent) * 100) // 10 * 10 for amount in spent]

    # Step 3: build bar chart rows
    chart_lines = ["Percentage spent by category"]
    for i in range(100, -1, -10):
        line = f"{i:>3}| "
        for pct in percentages:
            line += "o  " if pct >= i else "   "
        chart_lines.append(line)

    # Step 4: horizontal line
    chart_lines.append("    " + "-" * (len(categories) * 3 + 1))

    # Step 5: vertical category names
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        line = "     "
        for category in categories:
            line += (category.name[i] + "  ") if i < len(category.name) else "   "
        chart_lines.append(line)

    return "\n".join(chart_lines)
