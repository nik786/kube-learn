
```

# We will use a simple utility to make the text wrap properly when printing.
from IPython.display import HTML, display

def set_css():
  display(HTML('''
  <style>
    pre {
        white-space: pre-wrap;
    }
  </style>
  '''))
get_ipython().events.register('pre_run_cell', set_css)

```
pip install -U duckduckgo_search

```

from duckduckgo_search import DDGS
results = DDGS().text("India World Cup win", max_results=5)
print(results)

```

```

keywords = 'Zelensky Trump fun meeting'
r = DDGS().news(keywords, region='in-en')

# Parse and print relevant information from each dictionary
for article in r:
    date = article.get('date')
    title = article.get('title')
    body = article.get('body')
    url = article.get('url')
    image = article.get('image')
    source = article.get('source')

    print(f"Date: {date}")
    print(f"Title: {title}")
    print(f"Body: {body}")
    print(f"URL: {url}")
    print(f"Image: {image}")
    print(f"Source: {source}")
    print("\n" + "="*80 + "\n")
print(r)

```
```

text = ""
for article in r:
  text +=  article.get('title')+ "\n"+ article.get('body')+"\n\n"

text

```

!pip install -q langchain-groq


```
import os
from google.colab import userdata
from langchain_groq import ChatGroq
os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")
llm_groq = ChatGroq(model_name="llama3-70b-8192")

```

```
from langchain_core.prompts import ChatPromptTemplate
def news_analyzer(pov, query):
  text = ""
  r = DDGS().news(query, region='us-en')
  for article in r:
    text +=  article.get('title')+ "\n"+ article.get('body')+"\n\n"

  prompt = "Give a detailed news analysis like an anchor with this pov and with this cultural context." + pov +  "You will be given news items to analyze and a tone of a particular celebrity to use. Here is the user question" + query + \
            "\n\n. The news items are : " + text
  return llm_groq.invoke(prompt).content

```

```
response = news_analyzer("Eastern European viewpoint", "Can Zelensky still get his Mineral deal without a guarantee")
print(response)
```













