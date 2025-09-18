from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatPerplexity(model='sonar',temperature=0.4)

prompt=PromptTemplate.from_template("give me name of capital of india and explain in 4 bullet points")

parser=StrOutputParser()

chain= prompt | model | parser

result=chain.invoke({})
print("Ans:",result)






