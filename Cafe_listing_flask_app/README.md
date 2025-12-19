# ☕ Coffee & Wi-Fi 💻 — Cafe Listing Flask App

A lightweight Flask web application that allows users to view and add cafes along with details such as coffee quality, Wi-Fi strength, and power socket availability.  
All data is stored using a CSV file to keep the project simple and beginner-friendly.

---

## 📌 Project Overview

This project demonstrates how to build a basic full-stack web application using Flask.

Users can:

- View a list of cafes and their amenities
- Add new cafes through a web form
- Store and retrieve cafe information from a CSV file
- Use emoji-based ratings for coffee, Wi-Fi, and power availability

The focus is on **Flask fundamentals**, form handling, and clean project structure without using a database.

---

## 🛠 Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Bootstrap 5
- **Forms:** Flask-WTF, WTForms
- **Data Storage:** CSV file (no database)
- **Styling:** Flask-Bootstrap

---

## 📁 Project Structure

coffee-wifi-cafes/
│
├── templates/
│ ├── base.html # Common layout with Bootstrap
│ ├── index.html # Landing page
│ ├── add.html # Form to add a cafe
│ └── cafes.html # Table of cafes
│
├── static/
│ └── css/
│ └── styles.css # (Optional) custom styles
│
├── cafe-data.csv # CSV file storing all cafe entries
├── form.py # WTForm class for the cafe form
├── main.py # Flask app with all routes
├── README.md # This file
└── learning-log.md # My personal learning notes

## 🚀 How to Run

1. **Clone the repo:**

git clone https://github.com/your-username/coffee-wifi-cafes.git
cd coffee-wifi-cafes

Set up a virtual environment:

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
Install dependencies:

pip install flask flask-wtf flask-bootstrap
Run the app:

python main.py
Open in browser:
http://127.0.0.1:5000/

📊 CSV Data Format
Each row in cafe-data.csv includes:

Cafe Name, Location URL, Open Time, Close Time, Coffee Rating, Wifi Rating, Power Rating
Example:

Blue Bottle, https://goo.gl/maps/xyz, 8:00 AM, 5:00 PM, ☕☕☕, 💪💪💪, 🔌🔌
💡 Features
Add cafes via form with validation

View all cafes in a styled table

Emoji rating system (☕, 💪, 🔌)

Google Maps location links

Bootstrap-powered UI

🙋‍♀️ Author

Created and maintained by nex-creator 🚀
