## 🎵 Billboard Time Machine: Create Spotify Playlists from Past Billboard Hot 100 Charts

This Python project allows you to generate a Spotify playlist of the **Billboard Hot 100** songs for any historical date (from the Billboard website), even if it's a weekday (by adjusting to the previous Saturday).

---

### 📁 Project Structure

```
billboard_time_machine/
├── .env                 # Environment variables for Spotify API credentials
├── main.py              # Main Python script
├── token.txt            # Spotify access token cache (auto-created)
├── README.md            # Project explanation and takeaways (this file)
```

---

## 🧠 Project Breakdown

---

### 🔐 Step 1: Load Spotify Credentials from `.env`

```python
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
```

#### ✅ Takeaway:

- Store sensitive information like API credentials securely in a `.env` file.
- Use `python-dotenv` to load them into the script.
- **Never commit your `.env` file to GitHub.** Use `.gitignore` to exclude it.

---

### 📅 Step 2: Get User Input & Convert to Billboard's Saturday Format

```python
input_date = input("Enter a date (YYYY-MM-DD): ")
date_obj = datetime.strptime(input_date, "%Y-%m-%d")
days_to_subtract = (date_obj.weekday() + 2) % 7
saturday_date = date_obj - timedelta(days=days_to_subtract)
```

#### ✅ Takeaway:

- Billboard charts are **published on Saturdays**, so we adjust any weekday input to the **most recent Saturday**.

---

### 🌐 Step 3: Scrape Billboard Hot 100 Website

```python
URL = f"https://www.billboard.com/charts/hot-100/{formatted_date}"
response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
song_name_span = soup.select("li h3.c-title")
```

#### ✅ Takeaway:

- `BeautifulSoup` and `requests` are great for web scraping.
- Use browser dev tools to find the correct HTML elements (like `h3.c-title` for song names).
- Add a **user-agent** header to mimic a real browser request and avoid 403 errors.

---

### 🔍 Step 4: Extract Song Names

```python
song_names = [song.getText().strip() for song in song_name_span]
```

#### ✅ Takeaway:

- Clean the extracted text using `.strip()`.
- Validate if the list is empty — maybe the chart for that date doesn’t exist.

---

### 🎷 Step 5: Authenticate with Spotify using Spotipy

```python
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(...))
user_id = sp.current_user()["id"]
```

#### ✅ Takeaway:

- Use the `SpotifyOAuth` flow from `spotipy` to get permission to modify playlists.
- Set `scope="playlist-modify-private"` for creating private playlists.

---

### 🔎 Step 6: Search for Songs on Spotify

```python
for song in song_names:
    query = f"track:{song} year:{year}"
    result = sp.search(query, type="track", limit=1)
```

#### ✅ Takeaway:

- Not all Billboard songs are available on Spotify.
- Wrap your Spotify search in a try-except block to handle `IndexError` when no result is found.

---

### ✅ Step 7: Create a Spotify Playlist and Add Songs

```python
playlist = sp.user_playlist_create(user=user_id, name=f"{formatted_date} Billboard100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
```

#### ✅ Takeaway:

- Use `sp.user_playlist_create()` to make a playlist.
- Add all valid URIs in bulk using `sp.playlist_add_items()`.

---

## 🔑 Final Output

```text
Playlist '2025-05-17 Billboard100' created with 89 songs.
```

---

## 📌 Key Lessons and Gotchas

| Topic                     | Tip                                                                   |
| ------------------------- | --------------------------------------------------------------------- |
| `.env` Management         | Never include `.env` in version control. Use `dotenv` to load values. |
| User Input Validation     | Always handle wrong formats and edge cases (like weekdays).           |
| Scraping Dynamic Websites | Use browser dev tools to find CSS selectors.                          |
| Spotify API Search        | Be prepared for missing songs. Log them for debugging.                |
| Playlist Creation         | Limit scope to only required permissions.                             |

---

## 🔄 Future Improvements

- Let users enter a song limit (top 10, 20, etc.).
- Search songs with artist info to improve Spotify match accuracy.
- Add a GUI using `tkinter` or `streamlit`.
- Support other Billboard charts (e.g., Top 200 Albums).
