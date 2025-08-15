import os
import warnings
from transformers import pipeline, MBartForConditionalGeneration, MBart50TokenizerFast

# Suppress logs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
warnings.filterwarnings("ignore")

# Summarization pipeline (CPU)
summarizer = pipeline(
    task="summarization",
    model="Falconsai/text_summarization",
    device=-1
)

shell_news = """
Who we are
Shell is a global group of energy and petrochemical companies, employing around 103,000 people [A] and with operations in more than 70 countries.

We seek to provide the world with the energy it needs today, while helping it build a sustainable energy future.

Our competitive advantages are built upon our large and diverse portfolio, people who have outstanding talent, strong technological capability and deep customer reach, which we are leveraging to help enable a balanced energy transition.

Shell's stakeholders include our customers, investors, employees and contractors, pensioners, our strategic partners and suppliers, the communities where we work, civil society, academia and think tanks, governments and regulators.

We expect our employees and contractors to maintain our focus on safety and abide by our core values of honesty, integrity and respect for people.

[A] At December 31, 2023.

Our operating businesses
Integrated Gas and Upstream
Integrated Gas and Upstream (IGU) explores for and extracts crude oil, natural gas and natural gas liquids. It delivers hydrocarbon products from conventional oil and gas operations, deep-water exploration and production, liquefied natural gas (LNG) activities, and converts natural gas into gas-to-liquids (GTL) fuels and other products. The marketing, trading and optimisation of LNG are included in IGU. IGU provides the secure energy customers need and we aim to do this with lower emissions.

Reporting segments
Integrated Gas | Upstream

Downstream, Renewables and Energy Solutions
Downstream, Renewables and Energy Solutions (R&ES) provides products and services to more than 1 million business customers. It includes Chemicals and Products, and Marketing, which includes Mobility – a business that serves around 33 million retail customers a day at more than 47,000 service stations. Marketing also includes Lubricants, and Sectors and Decarbonisation activities. Downstream and R&ES, underpinned by Trading and Supply, aims to meet the evolving energy needs of our customers.

Reporting segments
Marketing | Chemicals and Products | Renewables and Energy Solutions

Innovation
Technological innovation is integral to our pursuit of more and cleaner energy solutions as we work towards becoming a net-zero emissions energy business by 2050. Projects & Technology (P&T) manages major projects, driving innovation, while delivering technical services to our businesses. P&T provides essential functional leadership across Shell, addressing safety and environment, contracting and procurement, and greenhouse gas emissions management. Our research and development activities also encompass safety, performance products, and automation and artificial intelligence.
"""
print(summarizer(shell_news))

# Feature extraction pipeline (CPU)
feature_extractor = pipeline(
    "feature-extraction",
    model="sentence-transformers/all-mpnet-base-v2",
    framework="pt",
    device=-1
)
features = feature_extractor(
    "The students are having an awesome time!",
    return_tensors="pt"
)[0].numpy().mean(axis=0)
print(features)

# Question answering pipeline (CPU)
qa_model = pipeline(
    task="question-answering",
    model="deepset/roberta-base-squad2",
    device=-1
)
print(qa_model(
    question="Who is the state leader mentioned?",
    context="Today Eknath Shinde presided over the inauguration of the assembly. He is the CM of Maharashtra."
))

# Translation (CPU)
model_name = "facebook/mbart-large-50-many-to-many-mmt"
model = MBartForConditionalGeneration.from_pretrained(model_name)
tokenizer = MBart50TokenizerFast.from_pretrained(model_name, src_lang="en_XX")

translation_pipeline = pipeline(
    task="translation",
    model=model,
    tokenizer=tokenizer,
    device=-1
)

print(translation_pipeline(
    "Combat Loneliness Mitra gets to know you better every day, improving the quality of conversation providing constant support and companionship.",
    src_lang="en_XX",
    tgt_lang="hi_IN"
))

