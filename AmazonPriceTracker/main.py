import os
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


# 📌 Load environment vars #

load_dotenv()
TO_EMAIL = os.getenv("TO_EMAIL")
FROM_EMAIL = os.getenv("FROM_EMAIL")
PASSWORD = os.getenv("PASSWORD")


# 🌐 Target Amazon product URL #

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"


# 🧠 Custom headers   #

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
}


# 🛒 Scrape product price       #

response = requests.get(url=URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "html.parser")

try:
    price_text = soup.find(name="span", class_="a-offscreen").getText()
    price_without_dollar = price_text.split("$")[1]
    current_price = float(price_without_dollar)
    print(f"[INFO] Current Price: ${current_price}")
except Exception as e:
    print(f"[ERROR] Couldn't extract price: {e}")
    current_price = None


#  Check for price drop & email  #

BUY_PRICE = 95.00

if current_price is not None and current_price <= BUY_PRICE:
    try:
        subject = "Price Drop Alert"
        body = f"The price has dropped to ${current_price}!\nCheck it here: {URL}"
        message = f"Subject: {subject}\n\n{body}"

        with smtplib.SMTP("smtp.gmail.com") as server:
            server.starttls()
            server.login(user=FROM_EMAIL, password=PASSWORD)
            server.sendmail(from_addr=FROM_EMAIL, to_addrs=TO_EMAIL, msg=message)
            print("[✅] Email sent successfully.")
    except Exception as e:
        print(f"[❌] Failed to send email: {e}")
else:
    print(f"[INFO] No price drop. Current price: ${current_price}")
