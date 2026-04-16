# Step 5: Named Entity Recognition (NER)
# Learn: Find people, places, organizations, dates, etc.

import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["TEXT_ANALYTICS_ENDPOINT"]
key = os.environ["TEXT_ANALYTICS_KEY"]
client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Text to analyze
documents = ["Microsoft was founded by Bill Gates and Paul Allen in 1975 in Redmond, Washington."]

# Recognize entities
result = client.recognize_entities(documents)

# Print results
for doc in result:
    print("Entities found:")
    for entity in doc.entities:
        print(f"  • {entity.text:20s} - {entity.category:15s} ({entity.confidence_score:.2%})")