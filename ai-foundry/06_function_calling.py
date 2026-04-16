# Step 6: Function Calling
# Learn: Let AI call your functions

from openai import AzureOpenAI
import json

api_key = "YOUR_API_KEY"
endpoint = "YOUR_ENDPOINT"
deployment_name = "gpt-4o"

client = AzureOpenAI(api_key=api_key, api_version="2024-10-21", azure_endpoint=endpoint)

# Define a function
def get_weather(location):
    return f"The weather in {location} is sunny and 22°C"

# Tell AI about the function
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City name"}
            },
            "required": ["location"]
        }
    }
}]

# Ask AI
response = client.chat.completions.create(
    model=deployment_name,
    messages=[{"role": "user", "content": "What's the weather in Seattle?"}],
    tools=tools
)

# Check if AI wants to call function
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    
    print(f"AI wants to call: {tool_call.function.name}")
    print(f"With argument: {args['location']}")
    
    # Call the actual function
    result = get_weather(args['location'])
    print(f"Result: {result}")