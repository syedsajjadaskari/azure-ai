"""
Simple test script to verify Azure OpenAI credentials
Run this BEFORE the Streamlit app to check if your setup works
"""

import os
from openai import AzureOpenAI

# Load from environment variables
API_KEY = os.environ["AZURE_OPENAI_API_KEY"]
ENDPOINT = os.environ["AZURE_OPENAI_ENDPOINT"]
DEPLOYMENT_NAME = "gpt-4o"  # Your deployment name

print("🧪 Testing Azure OpenAI Connection...")
print(f"Endpoint: {ENDPOINT}")
print(f"Deployment: {DEPLOYMENT_NAME}")
print()

try:
    # Create client
    client = AzureOpenAI(
        api_key=API_KEY,
        api_version="2024-10-21",
        azure_endpoint=ENDPOINT
    )
    
    print("✅ Client created successfully!")
    print()
    
    # Test chat completion
    print("🤖 Sending test message...")
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "user", "content": "Say 'Hello, I am working!' in one short sentence."}
        ],
        max_tokens=50
    )
    
    print("✅ Response received!")
    print()
    print("AI Response:")
    print(response.choices[0].message.content)
    print()
    print("🎉 SUCCESS! Your credentials work!")
    print("You can now use them in the Streamlit app.")
    
except Exception as e:
    print("❌ ERROR:", str(e))
    print()
    print("Troubleshooting:")
    print("1. Make sure endpoint ends with /")
    print("2. Check API key has no extra spaces")
    print("3. Verify deployment name is correct")
    print("4. Update openai library: pip install --upgrade openai")