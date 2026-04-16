# Step 6: PII (Personally Identifiable Information) Detection
# Learn: Find emails, phone numbers, SSNs, credit cards

import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["TEXT_ANALYTICS_ENDPOINT"]
key = os.environ["TEXT_ANALYTICS_KEY"]
client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Text with PII
documents = ["My email is john.doe@example.com and my phone is 555-123-4567."]

# Detect PII
result = client.recognize_pii_entities(documents)

# Print results
for doc in result:
    print("PII Entities found:")
    for entity in doc.entities:
        print(f"  • {entity.text:25s} - {entity.category:15s}")
    
    print(f"\nRedacted text:")
    print(f"  {doc.redacted_text}")