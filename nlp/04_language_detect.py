# Step 4: Language Detection
# Learn: Auto-detect language from 120+ languages

import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["TEXT_ANALYTICS_ENDPOINT"]
key = os.environ["TEXT_ANALYTICS_KEY"]
client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Different language texts
documents = [
    "Hello, how are you?",
    "Bonjour, comment allez-vous?",
    "Hola, ¿cómo estás?",
    "こんにちは、お元気ですか？"
]

# Detect languages
result = client.detect_language(documents)

# Print results
for idx, doc in enumerate(result):
    print(f"Text: {documents[idx]}")
    print(f"Language: {doc.primary_language.name}")
    print(f"Confidence: {doc.primary_language.confidence_score:.2%}\n")