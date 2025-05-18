


!pip install -q -U pytubefix

```

from pytubefix import YouTube


url = "https://www.youtube.com/watch?v=zAjJYkUnTEs" #short
#url = "https://www.youtube.com/watch?v=suQYoqqomX8"
#url = "https://www.youtube.com/watch?v=VqspygBClOg"
#url = "https://www.youtube.com/watch?v=T-D1OfcDW1M"
#url = "https://www.youtube.com/watch?v=3x4zM7O8pZI" #bb
#url = "https://www.youtube.com/watch?v=4Prc1UfuokY" #thisissparta
yt = YouTube(url)
audio = yt.streams.filter(only_audio=True).first().download()

```

```

#Test if the Audio plays before we use whisper
from IPython.display import Audio
Audio(audio, rate = 22050)

```

## Trancribe Audio with Whisper

#First we will setup whisper
! pip install git+https://github.com/openai/whisper.git -q
import whisper
model = whisper.load_model("tiny") #for higher quality go for medium or large
transcript = model.transcribe(audio,fp16=False)['text']


## Clean the sentences and summarize with LLMs

!pip -q install langchain-groq

```

from google.colab import userdata
import os
os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")
from langchain_groq import ChatGroq
llm = ChatGroq(model_name="llama3-70b-8192")

```

```

response = llm.invoke("Can you summarize and provide context to this audio.I'm new to LLMs: "+transcript).content
response

```

```

def summarize_yt(url, llm):
  yt = YouTube(url)
  audio = yt.streams.filter(only_audio=True).first().download()
  print("Audio downloaded")

  transcript = model.transcribe(audio,fp16=False)['text']
  print(transcript)

  result = llm.invoke("Guess the movie and provide the context:"+transcript).content

  return result

```
```

text = summarize_yt("https://www.youtube.com/watch?v=J-lDwmvpav0", llm)
text

```



