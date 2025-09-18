from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os
from langgraph.graph import StateGraph, END
import operator
from typing import TypedDict, Annotated, List


load_dotenv()

AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

class ChatState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add] 

llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=AZURE_OPENAI_API_VERSION
)

def user_input_node(state: ChatState) -> ChatState:
    user_msg = state["messages"][-1] 
    return {"messages": [user_msg]}

def llm_node(state: ChatState) -> ChatState:
    response = llm.invoke(state["messages"])
    return {"messages": [response]} 

def output_node(state: ChatState) -> ChatState:
    ai_msg = state["messages"][-1]
    print(f"AI: {ai_msg.content}")
    return {"messages": [ai_msg]}

workflow = StateGraph(ChatState)

workflow.add_node("user_input", user_input_node)
workflow.add_node("llm", llm_node)
workflow.add_node("output", output_node)

workflow.set_entry_point("user_input")
workflow.add_edge("user_input", "llm")
workflow.add_edge("llm", "output")
workflow.add_edge("output", END)

app = workflow.compile()

if __name__ == "__main__":
    chat_history: List[BaseMessage] = []
    print("Hello how can i help you with ?")
    while True:
        query = input("You:")
        if query=="exit":
            break
        chat_history.append(HumanMessage(content=query))

        result = app.invoke({"messages": chat_history})
        chat_history.extend(result["messages"])  