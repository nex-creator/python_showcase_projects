# Budget App

A simple Python application for managing budgets across multiple categories and visualizing spending using a text-based bar chart.

---

## Overview

The Budget App allows users to:

- Track deposits, withdrawals, and transfers across multiple categories.
- Maintain a ledger for each category, showing all transactions.
- Check balances and ensure sufficient funds before spending or transferring.
- Generate a bar chart illustrating the percentage of spending in each category.

The app is designed to be lightweight and easy to use, while demonstrating Python classes, methods, and string formatting.

---

## Features

- **Category Class**: Represents a budget category with its own ledger.

  - Supports deposits and withdrawals.
  - Transfers between categories with automatic ledger updates.
  - Checks available funds before transactions.
  - Provides a formatted string representation of transactions and total balance.

- **Spending Chart**: Generates a vertical bar chart showing the percentage of spending in each category.
  - Only withdrawals are considered for percentage calculation.
  - Percentages are rounded down to the nearest 10.
  - The chart displays category names vertically and maintains proper spacing for readability.

---

## Usage

- Create `Category` instances for each budget category.
- Use the `deposit()`, `withdraw()`, and `transfer()` methods to manage funds.
- Use `print()` to display category ledgers.
- Call `create_spend_chart(categories)` to visualize spending across categories.

---

## Design Notes

- Transactions are stored as dictionaries in each category’s ledger.
- The `create_spend_chart` function works for any number of categories (tested up to four).
- Emphasis is placed on **string formatting** to meet exact spacing requirements for printing ledgers and charts.

---

## Testing

A simple demo script (`test_budget.py`) is included to illustrate the functionality of the Budget App. It creates sample categories, performs transactions, and prints the ledgers and spending chart.

---

## License

This project is open-source and free to use.

---

## Author

Neha Sharma(nex-creator)
