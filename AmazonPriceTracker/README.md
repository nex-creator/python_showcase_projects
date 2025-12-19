# 🛍️ Amazon Price Tracker 📉📧

A simple Python script that monitors the price of a product on Amazon and sends an email alert when the price drops below your desired threshold.

## 🚀 Features

- Scrapes Amazon product price using `requests` and `BeautifulSoup`.
- Sends email alerts using `smtplib` when price drops below a defined value.
- Uses `.env` file for securely storing email credentials.
- Includes realistic browser headers to bypass basic scraping protection.

## 📦 Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `python-dotenv`

Install dependencies using:

```bash
pip install -r requirements.txt


📁 Project Structure

AmazonPriceTracker/
│
├── main.py                # Main script to run the tracker
├── .env                   # Stores your email credentials (not pushed to GitHub)
└── README.md              # Project documentation



🔐 .env File Setup
Create a .env file in the root directory with the following keys:

.env

FROM_EMAIL=your_email@gmail.com
TO_EMAIL=recipient_email@gmail.com
PASSWORD=your_email_password_or_app_password
⚠️ For Gmail users, consider using an App Password if 2FA is enabled.

🧠 How It Works
Fetches the Amazon product page.

Parses the product price using BeautifulSoup.

Checks if the price is lower than your defined BUY_PRICE.

Sends an email notification if the condition is met.

✏️ Usage
Edit the following in main.py:

URL — to track a different Amazon product.

BUY_PRICE — your target price to trigger an alert.

Run the script:

python main.py
🧪 Sample Output

$ python main.py
$89.95
89.95
Message sent successfully
📬 Example Email

Subject: Price Drop Alert

The price has dropped to $89.95.
📌 Notes
This script uses static HTML scraping. If Amazon heavily obfuscates content or uses JavaScript, consider using Selenium.

Always respect website Terms of Service when scraping.

💻 Author
Neha Sharma
