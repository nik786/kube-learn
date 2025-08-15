import whisper
model = whisper.load_model("tiny") #for higher quality go for medium or large

transcript = model.transcribe(audio,fp16=False)['text']


