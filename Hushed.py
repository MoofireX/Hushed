from bs4 import BeautifulSoup
import requests
import urllib
from pydub import AudioSegment as audio
from pydub.playback import play

url = input("What type of bg music would you like? The choices are Lofi, Electrical, and Instrumental. ")

link = f"https://www.chosic.com/free-music/{url.lower()}"
link = urllib.request.urlopen(url)

content = link.read()
soup = BeautifulSoup(content, "html.parser")

