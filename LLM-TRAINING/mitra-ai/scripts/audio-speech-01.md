
```

import os
import tempfile
from pytubefix import YouTube
from IPython.display import Audio as IPyAudio
import whisper
from langchain_groq import ChatGroq

# --- 1. Setup Whisper ---
model = whisper.load_model("tiny")  # use "medium" or "large" for better quality

# --- 2. Setup LLM ---
groq_key = os.getenv("GROQ_API_KEY")
if not groq_key:
    raise ValueError("GROQ_API_KEY environment variable not set.")

llm = ChatGroq(model_name="llama3-70b-8192", groq_api_key=groq_key)


def summarize_yt(url, llm):
    """Download YouTube audio, transcribe, and summarize with LLM."""
    yt = YouTube(url)
    print(f"Downloading audio from: {yt.title}")

    # Save audio to a temporary file
    with tempfile.TemporaryDirectory() as tmpdir:
        audio_path = yt.streams.filter(only_audio=True).first().download(output_path=tmpdir)
        
        # Optional: preview in Jupyter
        try:
            display(IPyAudio(audio_path, rate=22050))
        except NameError:
            pass

        # Transcribe
        transcript = model.transcribe(audio_path, fp16=False)['text']
        print("Transcript:\n", transcript)

        # LLM Summarization
        result = llm.invoke(f"Guess the movie and provide the context: {transcript}").content
        return result


# --- 3. Process multiple URLs ---
urls = [
    "https://www.youtube.com/watch?v=J-lDwmvpav0",
    "https://www.youtube.com/watch?v=yhNWsX9PjeE",
    "https://www.youtube.com/watch?v=omzW1NPIPvs"
]

for url in urls:
    summary = summarize_yt(url, llm)
    print("\n--- LLM Summary ---\n", summary)
    print("\n" + "="*60 + "\n")


```
