
import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_groq import ChatGroq   # ✅ Import Groq LLM wrapper

# ✅ Set your API keys
os.environ["GROQ_API_KEY"] = os.getenv(
    "GROQ_API_KEY", ""
)
os.environ["SERPER_API_KEY"] = os.getenv(
    "SERPER_API_KEY", ""
)

# ✅ Define the LLM
groq_llm = ChatGroq(
    temperature=0,
    model_name="llama-3.3-70b-versatile",  # could also be "llama3-70b-8192"
    groq_api_key=os.environ["GROQ_API_KEY"]
)

# Search Tool
search_tool = SerperDevTool(n_results=5)

# Researcher Agent
researcher = Agent(
    role="Senior Research Analyst",
    goal="Concisely uncover AI and data science developments",
    backstory="Tech think tank analyst skilled in identifying key emerging trends efficiently.",
    verbose=False,
    allow_delegation=False,
    max_tokens=1000,
    llm=groq_llm   # ✅ Pass the LLM object, not a string
)

# Writer Agent
writer = Agent(
    role="Tech Content Strategist",
    goal="Craft compelling content on tech advancements",
    backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
    You transform complex concepts into compelling narratives.""",
    verbose=True,
    llm=groq_llm,   # ✅ Same fix here
    allow_delegation=True
)

# Task 1: Research
task1 = Task(
    description="""Briefly analyze AI Agents in Manufacturing.
    - Limit to 3-5 key insights
    - Use bullet points
    - Max 300 words""",
    expected_output="Concise bullet-point summary",
    agent=researcher
)

# Task 2: Write Tweets
task2 = Task(
    description="""Write me Tweets on how AI Agents are used in my industry -- Manufacturing.""",
    expected_output="Set of engaging Tweets",
    agent=writer
)

# Crew Setup
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True,
    max_rpm=4,
    max_steps=5
)

# Run Crew
result = crew.kickoff()

print("######################")
print(result)
