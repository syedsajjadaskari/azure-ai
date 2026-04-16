from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import ListSortOrder

project_endpoint = "https://agents-demo-resource.services.ai.azure.com/api/projects/agents-demo"
project = AIProjectClient(endpoint=project_endpoint, credential=DefaultAzureCredential())

# Create an agent with specific instructions
agent = project.agents.create_agent(
    model="gpt-4o",
    name="product-expert",
    instructions="You are a product expert specializing in tech gadgets. "
                 "Always provide detailed specifications and compare products when asked."
)

print(f"Created agent: {agent.name} (ID: {agent.id})")

# Create a conversation thread
thread = project.agents.threads.create()

# Add a message to the thread
message = project.agents.messages.create(
    thread_id=thread.id,
    role="user",
    content="What are the key differences between iPhone 15 Pro and Samsung S24 Ultra?"
)

# Run the agent
run = project.agents.runs.create_and_process(
    thread_id=thread.id,
    agent_id=agent.id
)

# Check if run succeeded
if run.status == "failed":
    print(f"Run failed: {run.last_error}")
else:
    # Get messages from the thread
    messages = project.agents.messages.list(
        thread_id=thread.id,
        order=ListSortOrder.ASCENDING
    )
    
    # Print the conversation
    for msg in messages:
        if msg.text_messages:
            print(f"{msg.role}: {msg.text_messages[-1].text.value}\n")

# Clean up
project.agents.delete_agent(agent.id)