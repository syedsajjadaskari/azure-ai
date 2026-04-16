# Step 5: Streaming Responses
# Learn: Get responses word-by-word (like ChatGPT)
import os
from openai import AzureOpenAI

api_key = os.environ["AZURE_OPENAI_API_KEY"]
endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
deployment_name = "gpt-4.1"

client = AzureOpenAI(
    api_key=api_key,
    api_version="2024-10-21",
    azure_endpoint=endpoint
)

# Stream response
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "user", "content": "Write a short poem about AI"}
    ],
    stream=True  # Enable streaming!
)

print("AI Response (streaming):")
for chunk in response:
    # Check if chunk has choices and content
    if chunk.choices and len(chunk.choices) > 0:
        delta_content = chunk.choices[0].delta.content
        if delta_content:
            print(delta_content, end="", flush=True)

print("\n")