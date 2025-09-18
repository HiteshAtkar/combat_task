from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel,Field
from typing import List

load_dotenv()

class validate(BaseModel):
    capital:str=Field(description="Write name of indias capital here")
    points:List[str]=Field(description="Write 4 point about Capital of india")

parser=PydanticOutputParser(pydantic_object=validate)

model=ChatPerplexity(model='sonar',temperature=0.4)

prompt=PromptTemplate.from_template("give me details about Capital of India, {format_instruction}",
        partial_variables={'format_instruction':parser.get_format_instructions()})

chain= prompt | model | parser

result=chain.invoke({})
print("Ans:",result.capital,end="\n")
print("Points:",result.points)





