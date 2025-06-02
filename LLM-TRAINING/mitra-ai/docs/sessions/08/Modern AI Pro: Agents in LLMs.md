

- Low level goals to high level goals
- One shot to an iterative process
- Planning to break down tasks
- Using tools to execute the tasks
- Get external feedback along the way
- Keep a memory of everything
- Access to real time and external data
- Sync to Async


pip install -U -q crewai crewai-tools

```

from google.colab import userdata
import os
os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")

```
```

from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
os.environ["SERPER_API_KEY"] = userdata.get("SERPER_API_KEY")

search_tool = SerperDevTool(n_results=5)

search_tool

```

```

# Create the researcher agent
researcher = Agent(
    role='Senior Research Analyst',
    goal='Concisely uncover AI and data science developments',  # Make goal more concise
    backstory="""Tech think tank analyst skilled in identifying key emerging trends efficiently.""",  # Reduce backstory length
    verbose=False,  # Reduce verbose output
    allow_delegation=False,
    max_tokens=1000,  # If supported
    llm='groq/mixtral-8x7b-32768'
)

```

```

# Create the writer agent
writer = Agent(
    role='Tech Content Strategist',
    goal='Craft compelling content on tech advancements',
    backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
  You transform complex concepts into compelling narratives.""",
    verbose=True,
    llm='groq/mixtral-8x7b-32768',
    allow_delegation=True
)


```

```

# Create tasks for the agents
task1 = Task(
    description="""Briefly analyze AI Agents in Manufacturing.
    - Limit to 3-5 key insights
    - Use bullet points
    - Max 300 words""",
    expected_output="Concise bullet-point summary",
    agent=researcher
)

# Create tasks for the agents
task2 = Task(
    description="""Write me Tweets on how AI Agents are used in my industry -- Manufacturing.""",
    expected_output="Detailed report",
    agent=writer
)

```

```

# Instantiate your crew with a sequential process and add a step limit
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True,
    max_rpm=4,
    max_steps=5  # Add a max_steps parameter to avoid infinite loops
)


```

```
# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)

```











