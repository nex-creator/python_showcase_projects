# 📘 Learning Log — Billboard Top 100 Scraper Project

## ✅ What I Learned

- How to use `requests` to send HTTP requests to a webpage.
- How to parse and navigate HTML content using `BeautifulSoup`.
- How to inspect web pages using browser DevTools to locate relevant tags and classes.
- The difference between `.find()` and `.select()` or `.find_all()`, and when to use which.
- String cleaning and formatting for scraped content.
- Basics of exception handling to make the script more robust.

---

## ⚠️ Challenges Faced

- **Website structure differences**: Billboard’s HTML structure is different depending on the date and page, so selecting the right tags/classes required trial and error.
- **Data Not Found Errors**: Some elements were missing or returned `None`, leading to `AttributeError`.
  - Fixed by adding checks like `if element is not None:` before accessing `.text`.
- **Understanding CSS selectors vs tag-based navigation** in BeautifulSoup.
- Ensuring scraped song titles were clean and without unnecessary white spaces.