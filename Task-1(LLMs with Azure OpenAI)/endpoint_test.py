from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=AZURE_OPENAI_API_VERSION
)

messages = [
    {"role": "system", "content": "You are a helpful and friendly assistant."}
]

response = client.chat.completions.create(
    model=AZURE_OPENAI_DEPLOYMENT_NAME,
    messages=messages
    )

result = response.choices[0].message.content
print(result)

while True:
    user_input = input("You: ")
    if user_input== 'exit':
        break
    else:
         messages.append({"role": "user", "content": user_input})
         response = client.chat.completions.create(
         model=AZURE_OPENAI_DEPLOYMENT_NAME,
         messages=messages)

         result = response.choices[0].message.content
         print("AI:",result)

         messages.append({"role": "assistant", "content": result})




    