# Step 3: Multi-Turn Conversation
# Learn: Have a back-and-forth conversation with AI

import os
from openai import AzureOpenAI

api_key = os.environ["AZURE_OPENAI_API_KEY"]
endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
deployment_name = "gpt-4.1"
client = AzureOpenAI(api_key=api_key, api_version="2024-10-21", azure_endpoint=endpoint)

# Conversation with history
messages = [
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a programming language..."},
    {"role": "user", "content": "What can I build with it?"}
]

response = client.chat.completions.create(
    model=deployment_name,
    messages=messages
)

print("User: What can I build with Python?")
print(f"AI: {response.choices[0].message.content}")