# Step 2: Sentiment Analysis
# Learn: Detect if text is positive, negative, or neutral

import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


endpoint = os.environ["TEXT_ANALYTICS_ENDPOINT"]
key = os.environ["TEXT_ANALYTICS_KEY"]

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Text to analyze
documents = ["I love Azure AI! It's amazing!"]

# Analyze sentiment
result = client.analyze_sentiment(documents)

# Print results
for doc in result:
    print(f"Text: {documents[0]}")
    print(f"Sentiment: {doc.sentiment}")
    print(f"Positive: {doc.confidence_scores.positive:.2%}")
    print(f"Negative: {doc.confidence_scores.negative:.2%}")
    print(f"Neutral: {doc.confidence_scores.neutral:.2%}")