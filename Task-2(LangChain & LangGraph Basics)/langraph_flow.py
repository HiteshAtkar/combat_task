from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
import os
from typing import TypedDict, Annotated, List
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages


load_dotenv()

class GraphState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]

def call_llm(state: GraphState):
    llm = ChatPerplexity(model="sonar", temperature=0.3)
    response = llm.invoke(state["messages"])
    return {"messages": [response]}  

graph = StateGraph(GraphState)
graph.add_node("llm", call_llm)
graph.set_entry_point("llm")
graph.add_edge("llm", END)

app = graph.compile()

system_message = SystemMessage(
    content="You are a helpful AI assistant Give 1-2 line responses If user says hi/hello greet them."
)

state = {"messages": [system_message]}

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    state["messages"].append(HumanMessage(content=query))

    state = app.invoke(state)

    print("AI:", state["messages"][-1].content)
