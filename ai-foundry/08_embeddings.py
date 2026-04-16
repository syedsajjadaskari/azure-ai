# Step 8: Image Generation (DALL-E)
# Learn: Generate images from text descriptions

from openai import AzureOpenAI

api_key = "YOUR_API_KEY"
endpoint = "YOUR_ENDPOINT"
dalle_deployment = "dall-e-3"  # Your DALL-E deployment

client = AzureOpenAI(api_key=api_key, api_version="2024-10-21", azure_endpoint=endpoint)

# Generate image
prompt = "A cat wearing sunglasses, digital art"

response = client.images.generate(
    model=dalle_deployment,
    prompt=prompt,
    size="1024x1024",
    n=1
)

image_url = response.data[0].url

print("Image generated!")
print(f"Prompt: {prompt}")
print(f"URL: {image_url}")
print("\nOpen this URL in your browser to see the image!")