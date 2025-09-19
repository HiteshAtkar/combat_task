from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, END
import operator


load_dotenv()
class ChatState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]

def route_logic(state: ChatState) -> str:
    last_message = state["messages"][-1].content.lower()

    if any(symbol in last_message for symbol in ["+", "-", "*", "/", "%"]):
        return "calculator"
    else:
        return "llm"

def router_node(state: ChatState):
    return {}

def calculator_node(state: ChatState):
    expr = state["messages"][-1].content
    result = eval(expr)
    return {"messages": [AIMessage(content=f"{result} (answer from calculator node)")]}

def llm_node(state: ChatState):
    llm = ChatPerplexity(model="sonar", temperature=0.4, max_tokens=200)
    response = llm.invoke(state["messages"])
    return {"messages": [AIMessage(content=response.content)]}

graph = StateGraph(ChatState)

graph.add_node("router", router_node)
graph.add_node("calculator", calculator_node)
graph.add_node("llm", llm_node)

graph.set_entry_point("router")

graph.add_conditional_edges("router", route_logic, {
    "calculator": "calculator",
    "llm": "llm",
})

graph.add_edge("calculator", END)
graph.add_edge("llm", END)

app = graph.compile()

while True:
    query = input("Ask:")
    if query== "exit":
        break
    else:
        result = app.invoke({"messages": [HumanMessage(content=query)]})
        print("AI:", result["messages"][-1].content)