

- [memory-types](https://colab.research.google.com/drive/1AcyWGauS0KooIGpk5KBR6yKE62pgJUA1#scrollTo=RyNVRd6-6_U2)


  pip install -U -q langchain-anthropic langchain gradio langchain-community


```

from google.colab import userdata
from os import environ
from langchain_anthropic import ChatAnthropic

environ["ANTHROPIC_API_KEY"] = userdata.get('ANTHROPIC_API_KEY')
llm = ChatAnthropic(temperature=0.7, model_name="claude-3-sonnet-20240229")


```

Basic: Conversation Buffer Memory
-----------------------------------

```
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain.chains import ConversationChain

from langchain_core.prompts.prompt import PromptTemplate
template = """
Your name is Mitra. You are an assistant for question-answering tasks for Mitra Robot customer support.
Use three sentences maximum and keep the answer concise.
Have a conversation related to robots and note their key details. Ask them about their
key information to get started.

Current conversation:
{history}
Human: {input}
Mitra:"""
prompt = PromptTemplate(input_variables=["chat_history", "input"], template=template)


```

```
memory=ConversationBufferMemory()

memory.save_context({"input": "My name is Balaji and I live in Bengaluru"}, {"output": "Thank you!"})
memory.load_memory_variables({})

conversation = ConversationChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    verbose=True,
)

conversation.predict(input="Hi, what is the name the customer gave?")



Entering new ConversationChain chain...
Prompt after formatting:

Your name is Mitra. You are an assistant for question-answering tasks for Mitra Robot customer support.
Use three sentences maximum and keep the answer concise.
Have a conversation related to robots and note their key details. Ask them about
their key information to get started.

Current conversation:
Human: My name is Balaji and I live in Bengaluru
AI: Thank you!
Human: Hi, what is the name the customer gave?
Mitra:

Mitra: The customer's name is Balaji and he lives in Bengaluru.
To assist you better, could you please share some key details about the robot or
the issue you need help with?

```

```
import gradio as gr
def chat(message, history):
    return conversation.predict(input=message)

# Create a Gradio interface
demo = gr.ChatInterface(
    fn=chat,
    title="Mitra Robot Buffer Memory Chat",
)

# Launch the Gradio interface
demo.launch(share=True)

```

Colab notebook detected. To show errors in colab notebook, set debug=True in launch()
Running on public URL: https://7ea571ee6fc344917c.gradio.live

This share link expires in 72 hours. For free permanent hosting and GPU upgrades, 
run `gradio deploy` from Terminal to deploy to Spaces (https://huggingface.co/spaces)


```

memory.load_memory_variables({})

conversation_with_summary = ConversationChain(
    llm=llm,
    memory=ConversationSummaryMemory(llm=llm),
    verbose=True,
    prompt=prompt
)
conversation_with_summary.predict(input="Hi, what's up?")


```

```

Hello! I'm Mitra, an AI assistant for Mitra Robot customer support. 
Let's start with some key details about your robot - what model do you have and what questions 
can I help you with? I'll provide concise and helpful responses.

```

```


def summary_chat(message, history):
    return conversation_with_summary.predict(input=message)

# Create a Gradio interface
summary_demo = gr.ChatInterface(
    fn=chat,
    title="Mitra Robot Summary Memory Chat",
)

# Launch the Gradio interface
summary_demo.launch(share=True)

```


```

Colab notebook detected. To show errors in colab notebook, set debug=True in launch()
Running on public URL: https://55536c3417c3518d12.gradio.live

This share link expires in 72 hours. For free permanent hosting and GPU upgrades,
run `gradio deploy` from Terminal to deploy to Spaces (https://huggingface.co/spaces)


```

```

conversation_with_summary.memory.load_memory_variables({})

{'history': 'The human greeted the AI assistant, who introduced itself as Mitra, an AI assistant for Mitra Robot customer support. Mitra asked the human for their robot model and what questions they need help with,
stating that it will provide concise and helpful responses.'}

```



















