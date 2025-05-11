

- [hugging-face](https://colab.research.google.com/drive/1bRZYvajrSV_k1AgH_Je1O4TWfpNvRU0P#scrollTo=PK5_GUoLVrO6)

text classification with a smaller model

```

roberta = pipeline("zero-shot-classification",model="facebook/bart-large-mnli", device="cuda")

```

```
sequence_to_classify = "My son is sick and need to be hospitalized"
candidate_labels = ['health insurance','auto insurance','property damage', 'accident claim', 'others']
output = roberta(sequence_to_classify, candidate_labels)
output

```

```
sequence_to_classify = "How do I make biriyani well?"
candidate_labels = ['billing','account creation','product issues', 'other']
output = roberta(sequence_to_classify, candidate_labels)
output

```

```

sequence_to_classify = "Virat Kohli is an awesome player."
candidate_labels = ['cricket', 'football', 'tennis', 'medicine']
output = roberta(sequence_to_classify, candidate_labels)
output
```

# Find the index of the highest score

max_score_index = output['scores'].index(max(output['scores']))

# Retrieve the corresponding label

label_with_highest_score = output['labels'][max_score_index]

# Print the label

print("Label with the highest score:", label_with_highest_score)


Text Summarization
-------------------

summarizer = pipeline(task="summarization",model="Falconsai/text_summarization")



news = """ Even as the decision to omit Shreyas Iyer and Ishan Kishan from the central contracts list for not turning up for domestic tournaments continues to receive mixed reactions, there was plenty of discussion about Hardik Pandya’s inclusion as well. The Indian Express understands that the selectors and the BCCI only handed Hardik a contract after the all-rounder gave an undertaking that if there are no white-ball commitments with the national team, he would feature for Baroda in the Syed Mushtaq Ali T20s and Vijay Hazare Trophy.

During the recent meeting, apart from Shreyas and Ishan, there was discussion regarding Pandya’s place in Grade A of the annual contract list as well. Since injuring his ankle during the World Cup in October, Pandya had remained out of action till last week when he returned to competitive cricket in the DY Patil tournament, where he is turning out for Reliance. Like Ishan, Pandya has been training individually in Vadodara, but what worked in his favour is that he has been reporting at the National Cricket Academy (NCA) on a time-to-time basis to have his fitness assessed.

According to a top BCCI official, Pandya has also given assurance that he would feature in domestic tournaments if they don’t overlap with international commitments. “We have had discussions with Pandya, who has been told to play domestic white-ball tournaments when he is available. At this stage, according to the assessment of the BCCI’s medical team, he is not in a position to bowl in red-ball tournaments. So playing Ranji Trophy is out of the equation for Pandya. But he has to play other white-ball tournaments if there are no India commitments. If not, he will miss out on a contract,” the official told The Indian Express.

According to the Future Tours Programme, India are scheduled to play only three T20Is at home against Bangladesh as the team has a busy Test calendar. In the October-December period, when India don’t have any white-ball commitments, the Syed Mushtaq Ali T20s and Vijay Hazare Trophy would be conducted. And unless Pandya has any fitness issues, he has been directed to feature in both these tournaments.

Different yardsticks
While former cricketers have welcomed the BCCI’s decision to drop Shreyas and Ishan from the contracts list, Irfan Pathan raised the question regarding Pandya on X (previously Twitter). “They are talented cricketers, both Shreyas and Ishan. Hoping they bounce back and come back stronger. If players like Hardik don’t want to play red-ball cricket, should he and others like him participate in white-ball cricket when they aren’t on national duty? If this doesn’t apply to all, then Indian cricket won’t achieve the desired results!” Pathan tweeted on Thursday morning.

Festive offer
Also Read | How missing Ranji Trophy games resulted in Shreyas Iyer and Ishan Kishan being dropped from BCCI’s central contract list
It is understood that the BCCI will also instruct contracted players to report to their respective state units when they are not part of the national team set-up. There have been instances when in the middle of the domestic season, players from several states attended short camps with their respective IPL franchises, a move which didn’t go down well with the state units. Shreyas, for instance, attended a Kolkata Knight Riders camp after missing a Ranji fixture with Mumbai.



On Wednesday, based on the recommendations of the selectors, BCCI secretary Jay Shah announced that Shreyas and Ishan were not considered for the 2023-24 annual contracts. Though the two were part of the national set-up across all three formats for the majority of 2023, that the duo didn’t turn up for Ranji Trophy had drawn sharp criticism from several quarters. And despite Shah writing to contracted players, urging them to participate in the tournament, Shreyas and Ishan missed the next round of Ranji fixtures.
"""
summarizer(news)



shell_news = """
Who we are
Shell is a global group of energy and petrochemical companies, employing around 103,000 people [A] and with operations in more than 70 countries.

We seek to provide the world with the energy it needs today, while helping it build a sustainable energy future.

Our competitive advantages are built upon our large and diverse portfolio, people who have outstanding talent, strong technological capability and deep customer reach, which we are leveraging to help enable a balanced energy transition.

Shell's stakeholders include our customers, investors, employees and contractors, pensioners, our strategic partners and suppliers, the communities where we work, civil society, academia and think tanks, governments and regulators.

We expect our employees and contractors to maintain our focus on safety and abide by our core values of honesty, integrity and respect for people.

[A] At December 31, 2023.

Our operating businesses
Sunset view of the Vito platform surrounded by several boats (photo)
Integrated Gas and Upstream
Integrated Gas and Upstream (IGU) explores for and extracts crude oil, natural gas and natural gas liquids. It delivers hydrocarbon products from conventional oil and gas operations, deep-water exploration and production, liquefied natural gas (LNG) activities, and converts natural gas into gas-to-liquids (GTL) fuels and other products. The marketing, trading and optimisation of LNG are included in IGU. IGU provides the secure energy customers need and we aim to do this with lower emissions.

Reporting segments
Integrated Gas | Upstream

Looking-up perspective of a wind turbine against blue sky (photo)
Downstream, Renewables and Energy Solutions
Downstream, Renewables and Energy Solutions (R&ES) provides products and services to more than 1 million business customers. It includes Chemicals and Products, and Marketing, which includes Mobility – a business that serves around 33 million retail customers a day at more than 47,000 service stations. Marketing also includes Lubricants, and Sectors and Decarbonisation activities. Downstream and R&ES, underpinned by Trading and Supply, aims to meet the evolving energy needs of our customers.

Reporting segments
Marketing | Chemicals and Products | Renewables and Energy Solutions

Innovation
Technological innovation is integral to our pursuit of more and cleaner energy solutions as we work towards becoming a net-zero emissions energy business by 2050. Projects & Technology (P&T) manages major projects, driving innovation, while delivering technical services to our businesses. P&T provides essential functional leadership across Shell, addressing safety and environment, contracting and procurement, and greenhouse gas emissions management. Our research and development activities also encompass safety, performance products, and automation and artificial intelligence.
"""
summarizer(shell_news)



Generate Text embeddings
-------------------------

feature_extractor = pipeline("feature-extraction",framework="pt",model="sentence-transformers/all-mpnet-base-v2")


feature_extractor("The students are having an awesome time!",return_tensors = "pt")[0].numpy().mean(axis=0)




qa_model = pipeline(task="question-answering", model="deepset/roberta-base-squad2")

qa_model(question="Who is the state leader mentioned?",context="Today Eknath Shinde presided over the innaguration of the assembly. he is the cm of maharashtra.")


```

from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
model_name = "facebook/mbart-large-50-many-to-many-mmt"


model = MBartForConditionalGeneration.from_pretrained(model_name)
tokenizer = MBart50TokenizerFast.from_pretrained(model_name, src_lang="en_XX")
translation = pipeline(task="translation",model=model,tokenizer=tokenizer)

```

```

translation("Combat Loneliness Mitra gets to know you better every day, improving the quality of conversation providing constant support and companionship.", src_lang="en_XX", tgt_lang="hi_IN")


```


Multimodal Models for Visual Question Answering
------------------------------------------------


```
import locale
locale.getpreferredencoding = lambda: "UTF-8"

!apt install -y tesseract-ocr
!pip install -q -U pytesseract

```
```

from transformers import pipeline

vqa = pipeline(model="impira/layoutlm-document-qa")
image = "https://templates.invoicehome.com/invoice-template-us-neat-750px.png"
vqa(image=image,question="What is the invoice date?")


vqa(image=image,question="What is the balance due?")

vqa(image=image,question="what is teh address")

```



Answering questions based on tabular data
-------------------------------------------

tqa = pipeline(task="table-question-answering", model="google/tapas-large-finetuned-wtq")


data = {"Actors": ["Brad Pitt", "Leonardo Di Caprio", "George Clooney"], "Number of movies": ["87", "53", "69"]}
import pandas as pd
tqa(table=pd.DataFrame.from_dict(data), query="how many movies does Leonardo Di Caprio have?")


Answering questions on Documents
----------------------------------


from PIL import Image
dqa = pipeline("document-question-answering", model="naver-clova-ix/donut-base-finetuned-docvqa")

dqa(question="What is the balance due?", image="https://www.invoicesimple.com/wp-content/uploads/2018/06/Sample-Invoice-printable.png")



Text Sentiment Analysis
-------------------------

sentiment = pipeline(model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", return_all_scores=True)

sentiment("Apple stock is crazy awesome. Buy that stock for sure.")


Let's do Text Generation
-------------------------

text_generation = pipeline(task="text-generation",model="gpt2")

text_generation("Siemens mobility builds rail ")

text_generation("Summary of the Indian Constituition")


This hallucinates like hell. Good that we went beyond GPT2!
We will be using Mistral 7B that is a very good model (as of Jan 2024). But, 
it won't fit in the free Colab directly. We need to start with Quantization to fit the model in memory.

10b: Text generation with Mistral
----------------------------------

!pip install -q -U bitsandbytes torch accelerate


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
tokenizer = AutoTokenizer.from_pretrained(model_id)

```

Step 2: Setting up the pipeline to use with Langchain
------------------------------------------------------
```

!pip install --upgrade --quiet langchain langchain-community
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline

```

```

hf = pipeline(
    task="text-generation",
    model=model_4bit, #Quantized
    tokenizer=tokenizer,
    eos_token_id=tokenizer.eos_token_id,
    pad_token_id=tokenizer.eos_token_id,
    use_cache=True,
    max_length=500,
)
llm_mistral = HuggingFacePipeline(pipeline=hf)

```

```

from langchain import PromptTemplate, LLMChain
template = """Question: {question}

Summary: Summarize the following for a layman."""
summary_prompt = PromptTemplate.from_template(template)
summary_chain_m = summary_prompt | llm_mistral


```

summary_chain_m.invoke({"question": "Summary of the Indian Constituition"})


```

template = """Give a critical commentary and explain the background for this political context for a non-US resident:
{context}
"""
prompt = PromptTemplate(template=template, input_variables=["question","context"])
chain = prompt | llm_mistral

```

```
context = """
The Biden administration told the Supreme Court that “Texas has effectively prevented Border Patrol from monitoring the border” at Shelby Park. The state has defended the seizure, with Attorney General Ken Paxton saying he “will continue to defend Texas’s efforts to protect its southern border” against the federal government's attempts to undermine it.

At a ranch outside Eagle Pass where Abbott sympathizers gathered ahead of Saturday's rally, vendors sold Donald Trump-inspired MAGA hats and Trump flags. A homemade sign read, "The federal government has lost its way. Their job is to protect the states.”

Julio Vasquez, pastor of Iglesia Luterana San Lucas in Eagle Pass, said Abbott's campaign is a waste of money because migrants “come with empty hands asking for help.”

Alicia Garcia, a lifelong Eagle Pass resident who avoids Shelby Park but attended Friday's annual rodeo-themed festival at the nearby international bridge, questioned the value of Abbott's efforts because many asylum-seekers are released by U.S. authorities to argue their cases in immigration court.

“What’s with the show?” said Garcia, 38. "Better to just break everything down if they are still crossing.”
"""

chain.invoke({"context":context})


```

Step 4: Bringing capabilities of Code execution
-------------------------------------------------

```
import locale
locale.getpreferredencoding = lambda: "UTF-8"
!pip install -U -q langchain-experimental
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_experimental.utilities import PythonREPL
```

```

def _sanitize_output(text: str):
    _, after = text.split("```python")
    return after.split("```")[0]

template = """Write python code to solve the user's problem: {problem}.

Return only python code in Markdown format, e.g.:

```python
....
```"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | llm_mistral | StrOutputParser() | _sanitize_output | PythonREPL().run

```

chain.invoke({"problem": "What is 2 plus 2"})

We can try for non-textual data
--------------------------------

Image Classification
---------------------

```
vision_classifier = pipeline(task="image-classification",model="google/vit-base-patch16-224")

preds = vision_classifier(images="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/2019_Toyota_Corolla_Icon_Tech_VVT-i_Hybrid_1.8.jpg/1200px-2019_Toyota_Corolla_Icon_Tech_VVT-i_Hybrid_1.8.jpg")
preds = [{"score": round(pred["score"], 4), "label": pred["label"]} for pred in preds]
preds

```

Speech Recognition
---------------------


transcriber("https://www.signalogic.com/melp/EngSamples/male600.wav")


Video classification
----------------------

pip install -q -U decord


from transformers import pipeline

videoclassifer = pipeline(task = "video-classification", model="nateraw/videomae-base-finetuned-ucf101-subset")

videoclassifer("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/basketball.avi?download=true")














































































































