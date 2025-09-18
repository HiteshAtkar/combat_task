from langchain_perplexity import ChatPerplexity
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv
import os

api_key=os.getenv("PERPLEXITY_API_KEY")

model=ChatPerplexity(model='sonar',temperature=0.4,max_tokens=100,api_key=api_key)

chat_history=[
    SystemMessage(content="You are an AI Assistant which will give 1 line responces")
             ]

while(True):
    user=input("You:")
    chat_history.append(HumanMessage(content=user))
    if user=='exit':
        break
    else:
        result=model.invoke(chat_history)
        chat_history.append(AIMessage(content=result.content))
        print("AI:",result.content)




