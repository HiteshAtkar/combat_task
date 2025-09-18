from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import ConversationChain

load_dotenv()

llm = ChatPerplexity(model="sonar", temperature=0.3)

memory = ConversationBufferMemory(return_messages=True)

prompt = ChatPromptTemplate.from_messages([
    ("system", "you are a helpful AI assistant. and give 1-2 line responce to users questions,if he/she say hi greet them"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=False 
)

while True:
    query = input("You: ")
    if query=='exit':
        break

    result = conversation.invoke({"input": query})

    print(f"AI: {result['response']}")
