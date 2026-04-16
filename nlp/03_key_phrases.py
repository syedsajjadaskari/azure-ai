# Step 3: Key Phrase Extraction
# Learn: Extract important words and phrases

import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["TEXT_ANALYTICS_ENDPOINT"]
key = os.environ["TEXT_ANALYTICS_KEY"]
client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Text to analyze
documents = ["Azure AI provides machine learning and natural language processing capabilities for developers."]

# Extract key phrases
result = client.extract_key_phrases(documents)

# Print results
for doc in result:
    print("Key Phrases:")
    for phrase in doc.key_phrases:
        print(f"  • {phrase}")