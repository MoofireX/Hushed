from bs4 import BeautifulSoup
import requests
import urllib
from pydub import AudioSegment as audio
from pydub.playback import play

headers = {
	"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

url = input("What type of bg music would you like? The choices are Lofi, Electrical, and Instrumental. ")

link = f"https://www.chosic.com/free-music/{url.lower()}"
link = urllib.request.urlopen(link)

content = link.read()
soup = BeautifulSoup(content, "html.parser")

for mp3 in soup.find_all('audio'):
	print(mp3)
