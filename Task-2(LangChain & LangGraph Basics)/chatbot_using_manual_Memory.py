from langchain_perplexity import ChatPerplexity
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

model=ChatPerplexity(model='sonar',temperature=0.4,max_tokens=100)

chat_history=[
    SystemMessage(content="You are an AI Assistant which will give 1 line responces to my question")
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









