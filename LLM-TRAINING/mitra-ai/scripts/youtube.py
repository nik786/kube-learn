from pytubefix import YouTube
from IPython.display import Audio



url = "https://www.youtube.com/watch?v=zAjJYkUnTEs" #short
#url = "https://www.youtube.com/watch?v=suQYoqqomX8"
#url = "https://www.youtube.com/watch?v=VqspygBClOg"
#url = "https://www.youtube.com/watch?v=T-D1OfcDW1M"
#url = "https://www.youtube.com/watch?v=3x4zM7O8pZI" #bb
#url = "https://www.youtube.com/watch?v=4Prc1UfuokY" #thisissparta
yt = YouTube(url)
audio = yt.streams.filter(only_audio=True).first().download()
Audio(audio, rate = 22050)
