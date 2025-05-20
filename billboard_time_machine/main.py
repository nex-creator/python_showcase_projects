import os
import requests
import timedelta
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

#Load environment variable
load_dotenv()
# Spotify credentials from .env file
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
print("CLIENT_ID:", CLIENT_ID)
#Step1 get user input for dat
input_date = input("Enter a date (YYYY-MM-DD): ")



# Step 2: Convert to the most recent Saturday
date_obj = datetime.strptime(input_date, "%Y-%m-%d")
days_to_subtract = (date_obj.weekday() + 2) % 7  # Saturday = 5
saturday_date = date_obj - timedelta(days=days_to_subtract)
formatted_date = saturday_date.strftime("%Y-%m-%d")
print(f"Fetching Billboard Hot 100 for the week of {formatted_date}")


#Step 3 Scrap billboard
URL= f"https://www.billboard.com/charts/hot-100/{formatted_date}"
#here the useragent ells the server which browser and operating system you're using
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
#initiate a get request to billboard url
response = requests.get(url=URL,headers=headers)
website_html= response.text #store the response for further steps
soup = BeautifulSoup(website_html,"html.parser") # here parse the html website us BS


#Step 4: Extract song name
song_name_span= soup.select("li h3.c-title")
song_names = [song.getText().strip()for song in song_name_span]
if not song_names:
    print("No songs found for this date. Billboard chart may not exist.")
    exit()

#Step 5 Authenticate with spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
))
#GET USERID
user_id = sp.current_user()["id"]


#Step 6 Search song on spotify

song_uris=[]
year=saturday_date.year
#get the uri of each song in the songs list
for song in song_names:
    query=f"track:{song} year:{year}"
    result = sp.search(query,type = "track",limit =1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"Song not found on Spotify: {song}")

#Step 7 Create a playlist on Spotify
playlist = sp.user_playlist_create(user=user_id,name = f"{formatted_date} Billboard100",public=False)
sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)

print(f"Playlist '{playlist['name']}' created with {len(song_uris)} songs.")