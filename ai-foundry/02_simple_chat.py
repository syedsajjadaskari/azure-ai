# Step 2: Basic Chat Completion
# Learn: Ask GPT a question and get answer

import os
from openai import AzureOpenAI

# Setup
api_key = os.environ["AZURE_OPENAI_API_KEY"]
endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
deployment_name = "gpt-4.1"

client = AzureOpenAI(
    api_key=api_key,
    api_version="2024-10-21",
    azure_endpoint=endpoint
)

# Simple chat
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "user", "content": "Explain Azure OpenAI in one sentence"}
    ]
)

# Print response
print("AI Response:")
print(response.choices[0].message.content)