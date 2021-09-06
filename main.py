from bs4 import BeautifulSoup
import requests

choice = input("Which year would you like to travel to? Type the date in this format YYYY-MM-DD: ")

song_year = (f"https://www.billboard.com/charts/hot-100/{choice}")

response = requests.get(song_year)

bb_site = (response.text)

soup = BeautifulSoup(bb_site, "html.parser")

song_names = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
artist_names = soup.find_all(name="span", class_="chart-element__information__artist text--truncate color--secondary")

all_songs = []
all_artists = []

for text in song_names:
    song = text.getText()
    all_songs.append(song)

for text in artist_names:
    artist = text.getText()
    all_artists.append(artist)

your_top_100 = []

with open(f"{choice}-billboard_top_100.txt", mode="w") as file:
    for song, artist in zip(all_songs, all_artists):
        song_list = (f'"{song[::]}"')
        artist_list = artist[::]
        your_top_100 = [f'{song_list} by {artist_list}']
        for song in your_top_100:
            file.write(f"{song}\n")
        print(your_top_100)


