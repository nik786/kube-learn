
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from duckduckgo_search import DDGS

# ✅ Set your Groq API key here (or export it in your shell before running)
os.environ["GROQ_API_KEY"] = os.getenv(
    "GROQ_API_KEY", ""
)


llm_groq = ChatGroq(model_name="llama-3.3-70b-versatile")




def news_analyzer(pov, query):
  text = ""
  r = DDGS().news(query, region='us-en')
  for article in r:
    text +=  article.get('title')+ "\n"+ article.get('body')+"\n\n"

  prompt = "Give a detailed news analysis like an anchor with this pov and with this cultural context." + pov +  "You will be given news items to analyze and a tone of a particular celebrity to use. Here is the user question" + query + \
            "\n\n. The news items are : " + text
  return llm_groq.invoke(prompt).content


response = news_analyzer("Eastern European viewpoint", "Can Zelensky still get his Mineral deal without a guarantee")
print(response)

