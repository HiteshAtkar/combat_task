from typing import TypedDict, Annotated, List
import operator
from langgraph.graph import StateGraph, END
from langchain_perplexity import ChatPerplexity
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from dotenv import load_dotenv

load_dotenv()

# ---- State ----
class ChatState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]

# ---- Router ----
def router(state: ChatState):
    text = state["messages"][-1].content
    if any(op in text for op in ["+", "-", "*", "/"]):
        return "calculator"
    return "llm"

# ---- Calculator ----
def calculator(state: ChatState):
    text = state["messages"][-1].content
    try:
        result = eval(text, {"__builtins__": {}})
        return {"messages": [AIMessage(content=f"Answer: {result}")]}
    except Exception as e:
        return {"messages": [AIMessage(content=f"Error: {str(e)}")]}

# ---- LLM ----
llm = ChatPerplexity(model="sonar", temperature=0.3)

def ask_llm(state: ChatState):
    reply = llm.invoke(state["messages"])
    return {"messages": [reply]}

# ---- Build Graph ----
graph = StateGraph(ChatState)

graph.add_node("router", router)       # ✅ Added router node
graph.add_node("calculator", calculator)
graph.add_node("llm", ask_llm)

graph.set_entry_point("router")        # router = entrypoint
graph.add_conditional_edges("router", router, {
    "calculator": "calculator",
    "llm": "llm"
})
graph.add_edge("calculator", END)
graph.add_edge("llm", END)

app = graph.compile()

# ---- Chat Loop ----
print("Chatbot ready! (type 'exit' to quit)\n")
while True:
    query = input("You: ")
    if query.lower() == "exit":
        print("Bot: Goodbye 👋")
        break
    result = app.invoke({"messages": [HumanMessage(content=query)]})
    print("Bot:", result["messages"][-1].content)