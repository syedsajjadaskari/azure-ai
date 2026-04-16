# Step 8: Multiple Features at Once
# Learn: Analyze sentiment, key phrases, and entities together

import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["TEXT_ANALYTICS_ENDPOINT"]
key = os.environ["TEXT_ANALYTICS_KEY"]
client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Text to analyze
text = "Microsoft Azure AI is amazing! It helps developers build intelligent apps."
documents = [text]

# Analyze multiple features
print(f"Text: {text}\n")

# Sentiment
sentiment_result = client.analyze_sentiment(documents)[0]
print(f"😊 Sentiment: {sentiment_result.sentiment} ({sentiment_result.confidence_scores.positive:.0%})")

# Key Phrases
key_phrases = client.extract_key_phrases(documents)[0]
print(f"🔑 Key Phrases: {', '.join(key_phrases.key_phrases)}")

# Entities
entities = client.recognize_entities(documents)[0]
print(f"🏷️  Entities:")
for entity in entities.entities:
    print(f"   • {entity.text} ({entity.category})")