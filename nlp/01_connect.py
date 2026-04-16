# Step 1: Connect to Azure Language
# Type this yourself - only 8 lines!

import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["TEXT_ANALYTICS_ENDPOINT"]
key = os.environ["TEXT_ANALYTICS_KEY"]

client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

print("✅ Connected to Azure Language!")
print(f"Endpoint: {endpoint}")