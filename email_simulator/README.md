# 📧 Simple Email System (Python)

## Overview

This project is a **console-based email system simulation** written in Python. It demonstrates **Object-Oriented Programming (OOP)** concepts such as:

- Classes and objects
- Encapsulation
- Interaction between objects
- Real-world modeling (users, emails, inbox)

The system allows users to:

- Send emails
- Receive emails in an inbox
- List emails (read/unread)
- Read full email content
- Delete emails

This is an excellent beginner-to-intermediate level project for learning **Python OOP** to understand class-based design.

---

## 🔧 Technologies Used

- **Python 3**
- Built-in module: `datetime`

No external libraries are required.

---

## 🏗️ Project Structure

The program consists of **four main classes**:

1. `Email` – Represents a single email
2. `Inbox` – Stores and manages received emails
3. `User` – Represents a system user
4. `main()` – Demonstrates how the system works

---

## 📦 Class-by-Class Explanation

---

### 1️⃣ Email Class

#### Purpose

Represents an individual email with metadata and behavior.

#### Attributes

| Attribute   | Description                        |
| ----------- | ---------------------------------- |
| `sender`    | User object who sent the email     |
| `receiver`  | User object who receives the email |
| `subject`   | Email subject line                 |
| `body`      | Email message content              |
| `timestamp` | Date & time when email was created |
| `read`      | Boolean flag (Read / Unread)       |

#### Constructor

```python
self.timestamp = datetime.datetime.now()
self.read = False
```

- Automatically records when the email was created
- Marks email as **Unread** by default

#### Methods

##### `mark_as_read()`

Marks the email as read.

##### `display_full_email()`

- Marks the email as read
- Displays complete email details (From, To, Subject, Time, Body)

##### `__str__()` (Special Method)

Controls how the email appears when printed:

Example output:

```
[Unread] From: Tory | Subject: Hello | Time: 2025-12-18 14:30
```

This is used when listing emails in the inbox.

---

### 2️⃣ Inbox Class

#### Purpose

Manages a collection of emails for a user.

#### Attribute

```python
self.emails = []
```

A list that stores `Email` objects.

#### Methods

##### `receive_email(email)`

Adds a new email to the inbox.

##### `list_emails()`

- Displays all emails with index numbers
- Uses the `__str__()` method of Email
- Shows Read/Unread status

##### `read_email(index)`

- Validates index
- Displays full email
- Automatically marks it as read

##### `delete_email(index)`

- Deletes email by index
- Performs validation checks

All index handling is **1-based** for user-friendliness.

---

### 3️⃣ User Class

#### Purpose

Represents a system user who can send and receive emails.

#### Attributes

| Attribute | Description                       |
| --------- | --------------------------------- |
| `name`    | User name                         |
| `inbox`   | Inbox object assigned to the user |

Each user automatically gets their own inbox.

#### Methods

##### `send_email(receiver, subject, body)`

- Creates an Email object
- Sends it to receiver’s inbox

##### `check_inbox()`

Displays inbox contents.

##### `read_email(index)`

Reads a specific email.

##### `delete_email(index)`

Deletes a specific email.

This class acts as a **facade** between the user and inbox.

---

## ▶️ main() Function

Demonstrates the system behavior step by step:

```python
tory = User('Tory')
ramy = User('Ramy')
```

Creates two users.

### Sample Flow

1. Tory sends an email to Ramy
2. Ramy replies
3. Ramy checks inbox
4. Ramy reads email
5. Ramy deletes email
6. Ramy checks inbox again

This simulates a real email workflow.

---

## 📌 Sample Output (Simplified)

```
Email sent from Tory to Ramy!

Ramy's Inbox:
1. [Unread] From: Tory | Subject: Hello | Time: 2025-12-18 14:30

--- Email ---
From: Tory
To: Ramy
Subject: Hello
Received: 2025-12-18 14:30
Body: Hi Ramy, just saying hello!
------------

Email deleted.

Your inbox is empty.
```

---

## 🎯 Key OOP Concepts Demonstrated

- **Encapsulation** – Each class has a single responsibility
- **Object interaction** – Users send Email objects to other users
- **Abstraction** – User doesn’t manage inbox internals directly
- **Special methods** – `__str__()` for readable output

---

## 🚀 Possible Enhancements

- Add email search
- Add multiple inbox folders (Sent, Spam)
- Persist emails to file/database
- Add authentication (username/password)
- Add attachment support

---

## ✅ Who Should Use This?

- Python beginners
- Interview preparation (OOP & design questions)

---

## 🧠 Learning Tip

Try extending this project by:

- Writing unit tests
- Adding menu-driven input
- Converting it into a REST API

This will significantly strengthen your Python fundamentals.

---

Happy Coding! 🚀
