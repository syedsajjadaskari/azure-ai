# Step 4: System Messages
# Learn: Control AI personality and behavior

import os
from openai import AzureOpenAI

api_key = os.environ["AZURE_OPENAI_API_KEY"]
endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
deployment_name = "gpt-4.1"

client = AzureOpenAI(api_key=api_key, api_version="2024-10-21", azure_endpoint=endpoint)

# Set AI personality with system message
messages = [
    {"role": "system", "content": "You are a helpful pirate assistant. Always respond like a pirate."},
    {"role": "user", "content": "How do I learn programming?"}
]

response = client.chat.completions.create(
    model=deployment_name,
    messages=messages,
    temperature=0.7
)

print("AI (as pirate):")
print(response.choices[0].message.content)