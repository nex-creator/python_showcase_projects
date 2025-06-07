# ☕️ Coffee & Wifi 💻 — Cafe Listing Flask App

A Flask web application to list and add cafes with details like coffee quality, Wi-Fi strength, and power availability, stored in a CSV file.

---

## 📌 Project Summary

This project is a web app built with Flask where users can:

- View a list of cafes and their amenities
- Add new cafes via a form
- Store and retrieve cafe data from a CSV file
- Use emoji ratings for coffee, Wi-Fi, and power

---

## 🛠 Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Forms:** Flask-WTF, WTForms
- **Storage:** CSV (no database)
- **Styling:** Flask-Bootstrap (Bootstrap 5)

---

## 📁 File Overview

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
source venv/bin/activate  # On Windows: venv\Scripts\activate
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

