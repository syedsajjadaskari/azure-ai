# Step 7: Embeddings
# Learn: Convert text to numbers for semantic search

from openai import AzureOpenAI

api_key = "YOUR_API_KEY"
endpoint = "YOUR_ENDPOINT"
embedding_deployment = "text-embedding-ada-002"  # Your embedding deployment

client = AzureOpenAI(api_key=api_key, api_version="2024-10-21", azure_endpoint=endpoint)

# Text to convert
texts = [
    "Azure OpenAI is amazing",
    "I love machine learning",
    "The weather is nice today"
]

# Get embeddings
for text in texts:
    response = client.embeddings.create(
        model=embedding_deployment,
        input=text
    )
    
    embedding = response.data[0].embedding
    print(f"Text: {text}")
    print(f"Embedding length: {len(embedding)}")
    print(f"First 5 values: {embedding[:5]}")
    print()