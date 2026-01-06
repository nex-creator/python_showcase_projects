# Observer Pattern in Python Using Callbacks

## Project Summary

This project demonstrates the **Observer Design Pattern** in Python using **callback functions**. A `BankAccount` acts as the subject, notifying multiple observers (SMS, Email, Fraud Detection) whenever a deposit or withdrawal occurs. The implementation ensures **loose coupling**, event-driven design, and extensibility, allowing new observers or event types to be added without modifying the core logic. This project showcases practical application of design patterns and clean Python coding practices.

---

## Overview

The Observer Pattern allows objects to be notified automatically when the state of another object changes. In this project:

- **BankAccount** is the subject (observable)
- **SMS, Email, and Fraud Detection services** are observers
- Observers react independently to events without the subject knowing their internal logic

This pattern is ideal for building **event-driven systems** in a scalable and maintainable way.

---

## Features

- Deposit and Withdraw functionality with **balance validation**
- Observers are notified **only for valid transactions**
- Example observers:
  - **SMS Service** → prints transaction details
  - **Email Service** → prints transaction details in a different format
  - **Fraud Detection** → alerts on withdrawals >= 10,000
- Supports multiple BankAccount instances, each with its own observers
- Extensible: easily add more observers or transaction types

---

## Project Structure

observer_pattern/
│
├── bank_account.py # BankAccount class + observer functions
├── main.py # Demo: create accounts, register observers, perform transactions
└── README.md # Project documentation

---

## How It Works

1. **BankAccount** maintains a list of observer callbacks.
2. When a transaction occurs:
   - The account **updates its balance**
   - Creates an **event dictionary** containing:
     - `type` → `"deposit"` or `"withdraw"`
     - `amount` → transaction amount
     - `balance` → updated balance
   - Calls `notify_observers(event)`
3. Each registered observer receives the event and reacts independently.

---

## Getting Started

1. **Clone the repository**:

```bash
git clone <your-repo-url>
cd observer_pattern

2. **Run the Demo**:
python main.py


---
## Advantages

Demonstrates loose coupling: BankAccount does not depend on observer logic

Demonstrates event-driven programming

Extensible for new observers or event types without changing BankAccount

Ideal for teaching or showcasing design pattern implementation in Python

---

## How to Extend

Add additional observer functions in bank_account.py

Register observers to one or multiple BankAccount instances

Include more fields in the event dictionary (e.g., timestamp, account ID, currency)

---
## Author

Neha Sharma(nex-creator)
```
