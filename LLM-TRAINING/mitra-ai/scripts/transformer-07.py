import os
import locale
import logging
import warnings
import pandas as pd
from transformers import pipeline
from PIL import Image

# Suppress unwanted logs/warnings
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Hide TensorFlow logs
logging.getLogger("transformers").setLevel(logging.ERROR)
warnings.filterwarnings("ignore")

# Fix encoding issue
locale.getpreferredencoding = lambda: "UTF-8"

# Document Question Answering
dqa = pipeline(
    "document-question-answering",
    model="naver-clova-ix/donut-base-finetuned-docvqa"
)

print(dqa(
    question="What is the balance due?",
    image="Sample-Invoice-printable.png"
))

# Sentiment Analysis
sentiment = pipeline(
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student",
    return_all_scores=True
)

print(sentiment("Apple stock is crazy awesome. Buy that stock for sure."))

# Text Generation
text_generation = pipeline(
    task="text-generation",
    model="gpt2"
)

print(text_generation("Siemens mobility builds rail ", max_length=50, do_sample=True))
print(text_generation("Summary of the Indian Constitution", max_length=50, do_sample=True))

