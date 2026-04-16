# Step 1: Setup Azure OpenAI Client
# Type this yourself - only 10 lines!

import os
from openai import AzureOpenAI

# Your Azure OpenAI credentials
api_key = os.environ["AZURE_OPENAI_API_KEY"]
endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
deployment_name = "gpt-4o"  # Your deployment name

# Create client
client = AzureOpenAI(
    api_key=api_key,
    api_version="2024-10-21",
    azure_endpoint=endpoint
)

print("✅ Connected to Azure OpenAI!")
print(f"Endpoint: {endpoint}")
print(f"Deployment: {deployment_name}")