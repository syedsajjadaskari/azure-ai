"""
AI Chat Assistant - Powered by Azure OpenAI
Chat with GPT-4o using different AI personalities!
"""
import streamlit as st
from openai import AzureOpenAI

# Page config
st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 AI Chat Assistant")
st.markdown("Powered by Azure OpenAI GPT-4o")

# Sidebar - Credentials
st.sidebar.header("⚙️ Azure OpenAI Settings")

auth_method = st.sidebar.radio(
    "Authentication Method",
    ["API Key", "Azure AD Token"],
    help="Choose 'API Key' for key-based auth or 'Azure AD Token' for Entra ID auth"
)

if auth_method == "API Key":
    api_key = st.sidebar.text_input("API Key", value="", type="password", 
                                     help="Find this in Azure Portal > Your OpenAI Resource > Keys and Endpoint")
else:
    api_key = st.sidebar.text_input("Azure AD Token", value="", type="password",
                                     help="Get this from 'az account get-access-token --resource https://cognitiveservices.azure.com'")

endpoint = st.sidebar.text_input(
    "Endpoint", 
    value="", 
    placeholder="https://your-resource.openai.azure.com",
    help="Example: https://my-resource.openai.azure.com (no trailing slash)"
)

deployment_name = st.sidebar.text_input(
    "Deployment Name", 
    value="gpt-4o",
    help="The name of your deployed model in Azure OpenAI Studio"
)

api_version = st.sidebar.selectbox(
    "API Version",
    ["2024-10-21", "2024-08-01-preview", "2024-06-01", "2024-02-15-preview"],
    help="Try different versions if you encounter issues"
)

# Sidebar - AI Personality
st.sidebar.markdown("---")
st.sidebar.header("🎭 AI Personality")
personalities = {
    "Helpful Assistant": "You are a helpful, friendly assistant. Be concise and clear.",
    "Python Expert": "You are an expert Python programmer. Provide code examples and best practices.",
    "Creative Writer": "You are a creative writer. Be imaginative and engaging.",
    "Pirate": "You are a friendly pirate assistant. Always respond like a pirate! Use 'Ahoy' and 'matey'.",
    "Philosopher": "You are a thoughtful philosopher. Provide deep, meaningful insights.",
    "Chef": "You are an expert chef. Share cooking tips and recipes with enthusiasm."
}

selected_personality = st.sidebar.selectbox(
    "Choose personality:",
    list(personalities.keys())
)
system_message = personalities[selected_personality]

# Sidebar - Parameters
st.sidebar.markdown("---")
st.sidebar.header("🎛️ Parameters")
temperature = st.sidebar.slider("Temperature (Creativity)", 0.0, 2.0, 0.7, 0.1)
max_tokens = st.sidebar.slider("Max Tokens", 100, 2000, 500, 100)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Main chat interface
col1, col2 = st.columns([2, 1])

with col1:
    st.header("💬 Chat")
    
    # Display chat history
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.chat_message("user").write(message["content"])
        else:
            st.chat_message("assistant").write(message["content"])

with col2:
    st.header("ℹ️ Info")
    
    # Current settings
    st.subheader("Current Settings")
    st.write(f"**Personality:** {selected_personality}")
    st.write(f"**Temperature:** {temperature}")
    st.write(f"**Max Tokens:** {max_tokens}")
    st.write(f"**Auth Method:** {auth_method}")
    st.markdown("---")
    
    # Message count
    st.subheader("📊 Stats")
    user_messages = len([m for m in st.session_state.messages if m["role"] == "user"])
    ai_messages = len([m for m in st.session_state.messages if m["role"] == "assistant"])
    st.metric("Your Messages", user_messages)
    st.metric("AI Responses", ai_messages)
    st.markdown("---")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    
    # Tips
    st.subheader("💡 Tips")
    st.markdown("""
    - Try different personalities
    - Adjust temperature for creativity
    - Check your endpoint format
    - Ensure API key is valid
    """)
    
    # Troubleshooting
    with st.expander("🔧 Troubleshooting"):
        st.markdown("""
        **401 Error Solutions:**
        1. **Check API Key**: Copy fresh key from Azure Portal
        2. **Verify Endpoint**: Should be `https://YOUR-RESOURCE.openai.azure.com`
        3. **Check Deployment Name**: Must match exactly in Azure
        4. **Try Different API Version**: Select from dropdown above
        5. **Check Access**: Ensure your account has access to the resource
        
        **Where to find credentials:**
        - Azure Portal → Your OpenAI Resource → Keys and Endpoint
        """)

# Chat input
if prompt := st.chat_input("Type your message..."):
    if not api_key or not endpoint:
        st.error("⚠️ Please enter your Azure OpenAI credentials in the sidebar")
    else:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message immediately
        with col1:
            st.chat_message("user").write(prompt)
        
        # Create Azure OpenAI client
        try:
            # Clean endpoint - remove trailing slash and whitespace
            endpoint_clean = endpoint.strip().rstrip('/')
            
            # Validate endpoint format
            if not endpoint_clean.startswith('https://'):
                st.error("❌ Endpoint must start with https://")
                st.session_state.messages.pop()  # Remove user message
                st.stop()
            
            # Create client based on auth method
            if auth_method == "API Key":
                client = AzureOpenAI(
                    api_key=api_key.strip(),
                    api_version=api_version,
                    azure_endpoint=endpoint_clean
                )
            else:
                # For Azure AD token, use default_headers
                from openai import DefaultHttpxClient
                import httpx
                
                client = AzureOpenAI(
                    api_key="dummy",  # Required but not used
                    api_version=api_version,
                    azure_endpoint=endpoint_clean,
                    default_headers={"Authorization": f"Bearer {api_key.strip()}"}
                )
            
            # Prepare messages with system message
            api_messages = [
                {"role": "system", "content": system_message}
            ] + st.session_state.messages
            
            # Get response with streaming
            with col1:
                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    full_response = ""
                    
                    response = client.chat.completions.create(
                        model=deployment_name.strip(),
                        messages=api_messages,
                        temperature=temperature,
                        max_tokens=max_tokens,
                        stream=True
                    )
                    
                    # Stream response
                    for chunk in response:
                        if chunk.choices and chunk.choices[0].delta.content:
                            full_response += chunk.choices[0].delta.content
                            message_placeholder.write(full_response + "▌")
                    
                    message_placeholder.write(full_response)
            
            # Add assistant response to history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            error_msg = str(e)
            st.error(f"❌ Error: {error_msg}")
            
            # Provide specific guidance based on error
            if "401" in error_msg or "Unauthorized" in error_msg:
                st.warning("**Authentication Failed:**")
                st.info("""
                1. Double-check your API Key in Azure Portal
                2. Verify the endpoint URL is correct
                3. Try switching between 'API Key' and 'Azure AD Token' methods
                4. Ensure your Azure subscription is active
                """)
            elif "404" in error_msg:
                st.warning("**Deployment Not Found:**")
                st.info(f"The deployment '{deployment_name}' doesn't exist. Check the name in Azure OpenAI Studio.")
            elif "429" in error_msg:
                st.warning("**Rate Limit Exceeded:**")
                st.info("You've hit the rate limit. Wait a moment and try again.")
            
            # Remove the user message if there was an error
            if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
                st.session_state.messages.pop()

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Built with Streamlit & Azure OpenAI")
st.sidebar.caption("AI-102 Exam Preparation Project")