
- [getting-started-labs](https://colab.research.google.com/drive/1patliw_XCH-3eKJVrfVcjF8nLyPy1Mb7)


Modern AI Pro: Getting started with LLMs 
-------------------------------------------------

Let's build a combination of relational database and vector DB to create a modern AI application.


We will use a simple utility to make the text wrap properly when printing
--------------------------------------------------------------------------


Snippet Illustration
---------------------

- **Defines a function `set_css()`** that injects custom CSS to modify how `<pre>` blocks behave in Jupyter notebooks (enabling line wrapping).
- **Registers this function** to run automatically **before every code cell** using `get_ipython().events.register('pre_run_cell', set_css)`.
- **Improves readability** of long outputs by ensuring that text in `<pre>` tags doesn't overflow and wraps within the cell.

```

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







## Step 1: Get your dataset from Kaggle

Go to your account: https://www.kaggle.com/settings and create the new token button to download the kaggle.json. Extract the key and username and add it to Google Colab secrets. If you need help on this, go to our earliern notebook.


```

from google.colab import userdata
from os import environ

environ["KAGGLE_KEY"]      = userdata.get('KAGGLE_KEY')
environ["KAGGLE_USERNAME"] = userdata.get('KAGGLE_USERNAME')

! pip -q install kaggle

```

! kaggle datasets list


! kaggle datasets download -d 'saketk511/world-important-events-ancient-to-modern'
! unzip /content/world-important-events-ancient-to-modern.zip




Snippet Illustration
---------------------

- **Loads event data** from a CSV file and identifies the top 100 most frequent event types using `value_counts()`.
- **Generates a word cloud** from these frequencies using the `WordCloud` library to visualize their prominence.
- **Displays the word cloud** using `matplotlib` with axes hidden for a clean visual presentation.



```
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv("World Important Dates.csv")
top_100_events = df['Type of Event'].value_counts().head(100)

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(top_100_events)

# Display the generated word cloud:
plt.figure(figsize=(15, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide the axis
plt.show()

```










```
import sqlite3 as sql
db_path = '/content/worldevents.db'

# Connect to the SQLite database (this will create the database if it does not exist)
conn = sql.connect(db_path)

# Check if the table exists
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='world_events';")
table_exists = cursor.fetchone()

# If the table doesn't exist, create it from the DataFrame
if not table_exists:
    df.to_sql('world_events', conn, index=False)
    print("Table 'world_events' created and data inserted.")
else:
    print("Database and table 'world_events' already exist.")


```


```
%%sql
sqlite:///worldevents.db
select * from world_events LIMIT 5;

```



Step 3: Vectorize the Scalar DB
----------------------------------


We are going to use a bunch of libraries:


*   Langchain
*   Chroma DB
*   sentence-transformers

A glossary will be provided which explains these libraries


Installation
----------------

pip -q install langchain langchain-community sentence-transformers chromadb

```
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': False}
)

```
Query and create documents
----------------------------

```

# 
from langchain.docstore.document import Document
doc = []
cur = conn.cursor()
cur.execute("SELECT [Name of Incident],[Type of Event], Impact, [Place Name]  FROM world_events")
rows = cur.fetchall()


for row in rows:
    page = Document(page_content=row[0]+ ". Impact of the event:"+ row[2], metadata={' "Type of Event"': row[1], ' "Place Name"': row[3]})
    doc.append(page)

print(doc)


```



```
from langchain_community.vectorstores import Chroma
try:
  vector_db = Chroma.from_documents(doc, embedding_model)
except Exception as error:
    print("An exception occurred:", type(error).__name__)

```

```
query = "conflicts involving UK"
docs = vector_db.similarity_search(query, k=6)
docs

```


```

for doc in docs:
    # Extracting page_content and metadata for readability
    page_content = doc.page_content
    place_name = doc.metadata[' "Place Name"']
    type_of_event = doc.metadata[' "Type of Event"']

    # Formatting the output
    print(f"Event: {page_content}")
    print(f"Place: {place_name}")
    print(f"Type of Event: {type_of_event}\n")


```


pip install -q langchain-groq


```

import os
from langchain_groq import ChatGroq
os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")
llm_groq = ChatGroq(model_name="llama3-70b-8192")

```


```

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("Answer this question in detail: {question} from these documents {context} pulled from our database. \
Correct the names if needed. If possible, tell us how these events are connected. At the end print parse the  original context as citations. \
Remove duplicates from citations.")
chain = (
    {"context": vector_db.as_retriever(), "question": RunnablePassthrough()}
    | prompt
    | llm_groq
    | StrOutputParser()
)

```
print(chain.invoke("conflicts involving UK"))

```
from langchain_community.utilities import SQLDatabase
db = SQLDatabase.from_uri("sqlite:///worldevents.db")
def get_schema(_):
    return db.get_table_info()

def run_query(query):
    return db.run(query)

```

Optional 4: Setup Mistral 7B
------------------------------

```
!pip install -q -U bitsandbytes torch accelerate # related to loading custom models
!pip install -q -U langchain_core langchainhub

```


Ready the quantization for better memory performance
-------------------------------------------------------

```

from transformers import BitsAndBytesConfig, AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

```

```

model_id = "mistralai/Mistral-7B-Instruct-v0.1"
model_4bit = AutoModelForCausalLM.from_pretrained( model_id, device_map="auto",quantization_config=quantization_config)
tokenizer = AutoTokenizer.from_pretrained(model_id

```

```

from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
hf = pipeline(
    task="text-generation",
    model=model_4bit, #Quantized
    tokenizer=tokenizer,
    eos_token_id=tokenizer.eos_token_id,
    pad_token_id=tokenizer.eos_token_id,
    use_cache=True,
    max_length=500,
        device_map="auto",
        do_sample=True,
        top_k=5,
        num_return_sequences=1,
)
llm_mistral = HuggingFacePipeline(pipeline=hf)

```
```

print(chain.invoke("List all the key Conflicts involving UK. "))

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("Answer this question in detail: {question} from these documents {context} pulled from our database. \
Correct the names if needed. If possible, tell us how these events are connected.")
chain = (
    {"context": db.as_retriever(), "question": RunnablePassthrough()}
    | prompt
    | llm_mistral
    | StrOutputParser()

)
sql_response = (
    RunnablePassthrough.assign(schema=get_schema)
    | prompt
        | llm.bind(stop=["\nSQLResult:"])
    | StrOutputParser()
)
print(sql_response.invoke({"question": "How many events are there?"}))

```


Note: Only one of the below methods is required to be executed - Azure or MitraLLM
-----------------------------------------------------------------------------------





Step 5: Writing SQL queries with Groq
----------------------------------------


```

template = """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

Question: {question}
Give ONLY the query without the prepending ```sql and no explanation around the code.
This has to be passed to a code interpreter.
"""
prompt = ChatPromptTemplate.from_template(template)


```



```

from langchain_community.utilities import SQLDatabase
db = SQLDatabase.from_uri("sqlite:///worldevents.db")
def get_schema(_):
    return db.get_table_info()
def run_query(query):
    return db.run(query)


```


get_schema(_)

```

sql_response = (
    RunnablePassthrough.assign(schema=get_schema)
    | prompt
        | llm_groq.bind(stop=["\nSQLResult:"])
    | StrOutputParser()
)
print(sql_response.invoke({"question": "How many wars are involving India and China?"}))


```



```
SELECT COUNT(*) 
FROM world_events 
WHERE "Country" IN ('India', 'China') AND "Type of Event" = 'Battle';

```


```

sql_chain = (
    RunnablePassthrough.assign(query=sql_response).assign(
        schema=get_schema,
        response=lambda x: db.run(x["query"]),
    )
)
sql_chain.invoke({"question": "Give me the political party creation in India"})

```

```

response = sql_chain.invoke({"question": "Give me the political party creation in India"})
print(response['query'])
print(response['response'])


```

```

SELECT "Name of Incident" FROM world_events WHERE "Type of Event" = 'Political' AND "Country" = 'India';
[('Establishment of the Delhi Sultanate',), ('Indian Independence',), ('First General Elections',), ('Emergency Declared by Indira Gandhi',), ('Article 370 Revocation for Jammu & Kashmir',)]

```


```

response = sql_chain.invoke({
    "question": (
        "Give me the name and year of battles (use synonyms such as military and "
        "military battle) that happened in India between 1500 and 1800."
    )
})

response

```


```

response = sql_chain.invoke({
    "question": (
        "Give me the name and year of battles (use synonyms such as military and "
        "military battle) that happened in India between 1500 and 1800."
    )
})

response

```

print(response['query'])


response['response']





































