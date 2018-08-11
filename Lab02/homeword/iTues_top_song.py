from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
# Part 1 

url = "https://www.apple.com/itunes/charts/songs/"

conn = urlopen(url)
# read data
data = conn.read()
# decode
html = data.decode("utf-8")
# save to file
# html_file = open("iTues_top_Song.html", "wb")
# html_file.write(data)
# html_file.close

# 2: Extract ROI (region of interest)
soup = BeautifulSoup(html, "html.parser")
section = soup.find("section", "section chart-grid")
# print(section.prettify())

# 3: Extract info
songs = []
li_list = section.find_all("li")
for li in li_list:
    song = {}
    song['name'] = li.h3.string
    song['artist'] = li.h4.string
    songs.append(song)
pyexcel.save_as(records = songs, dest_file_name = "top_song.xlsx") 

# ***************************************************************************************************

# Part 2 : Search and download to youtube

from youtube_dl import YoutubeDL

options = {
    'default_search': 'ytsearch', # tell download to search instead of directly downloading
    'max_download': 1  # tell download to download only the first entry(video)
}
new_song = []
dl = YoutubeDL(options)
for li in li_list:
    song_name = li.h3.string
    song_artist = li.h4.string
    new_song.append(song_name + song_artist)
dl.download(new_song)


