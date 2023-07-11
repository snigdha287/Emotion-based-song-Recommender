import pandas as pd
import requests as re

import pafy
import vlc

url = "https://youtu.be/61Odj2pGuSI"
video = pafy.new(url)
best = video.getbest()
playurl = best.url

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()
