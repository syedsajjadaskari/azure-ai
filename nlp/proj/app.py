"""
Azure Text Analytics Dashboard
Analyze text with AI - sentiment, entities, key phrases, and more!
"""

import streamlit as st
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Page config
st.set_page_config(
    page_title="Text Analytics AI",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Azure Text Analytics Dashboard")
st.markdown("Analyze any text with AI - sentiment, entities, languages, and more!")

# Sidebar for credentials
st.sidebar.header("⚙️ Azure Settings")
endpoint = st.sidebar.text_input("Endpoint", value="", type="default")
api_key = st.sidebar.text_input("API Key", value="", type="password")

# Sidebar - Sample texts
st.sidebar.markdown("---")
st.sidebar.markdown("### 📝 Try Sample Texts")
sample_choice = st.sidebar.selectbox(
    "Select a sample:",
    ["Custom", "Product Review", "Customer Feedback", "News Article", "Social Media"]
)

samples = {
    "Product Review": "I absolutely love this product! The quality is amazing and the customer service was excellent. Highly recommended!",
    "Customer Feedback": "The service was okay but the wait time was too long. The staff tried their best though.",
    "News Article": "Microsoft announced a new AI breakthrough in natural language processing today in Redmond, Washington.",
    "Social Media": "Just had the worst experience ever at the restaurant. Never going back! 😡"
}

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📝 Input Text")
    
    # Text input
    if sample_choice != "Custom":
        default_text = samples[sample_choice]
    else:
        default_text = ""
    
    user_text = st.text_area(
        "Enter text to analyze:",
        value=default_text,
        height=200,
        placeholder="Type or paste your text here..."
    )
    
    # Character count
    if user_text:
        st.caption(f"📏 {len(user_text)} characters")

with col2:
    st.header("🎯 AI Analysis")
    
    if user_text and endpoint and api_key:
        # Analyze button
        if st.button("🚀 Analyze Text", type="primary", use_container_width=True):
            
            with st.spinner("Analyzing..."):
                try:
                    # Create client
                    client = TextAnalyticsClient(
                        endpoint=endpoint,
                        credential=AzureKeyCredential(api_key)
                    )
                    
                    documents = [user_text]
                    
                    # 1. Sentiment Analysis
                    st.subheader("😊 Sentiment Analysis")
                    sentiment_result = client.analyze_sentiment(documents)[0]
                    
                    sentiment = sentiment_result.sentiment
                    scores = sentiment_result.confidence_scores
                    
                    # Display sentiment with emoji
                    sentiment_emoji = {
                        "positive": "😊",
                        "negative": "😞",
                        "neutral": "😐",
                        "mixed": "🤔"
                    }
                    
                    st.markdown(f"### {sentiment_emoji.get(sentiment, '😐')} {sentiment.upper()}")
                    
                    # Confidence scores
                    col_pos, col_neg, col_neu = st.columns(3)
                    with col_pos:
                        st.metric("Positive", f"{scores.positive:.0%}")
                    with col_neg:
                        st.metric("Negative", f"{scores.negative:.0%}")
                    with col_neu:
                        st.metric("Neutral", f"{scores.neutral:.0%}")
                    
                    st.markdown("---")
                    
                    # 2. Key Phrases
                    st.subheader("🔑 Key Phrases")
                    key_phrases_result = client.extract_key_phrases(documents)[0]
                    
                    if key_phrases_result.key_phrases:
                        # Display as tags
                        phrases_html = " ".join([
                            f'<span style="background-color: #E3F2FD; padding: 5px 10px; margin: 3px; border-radius: 15px; display: inline-block;">{phrase}</span>'
                            for phrase in key_phrases_result.key_phrases[:10]
                        ])
                        st.markdown(phrases_html, unsafe_allow_html=True)
                    else:
                        st.info("No key phrases detected")
                    
                    st.markdown("---")
                    
                    # 3. Language Detection
                    st.subheader("🌍 Language")
                    language_result = client.detect_language(documents)[0]
                    
                    lang = language_result.primary_language
                    col_lang, col_conf = st.columns(2)
                    with col_lang:
                        st.info(f"**{lang.name}** ({lang.iso6391_name})")
                    with col_conf:
                        st.info(f"Confidence: **{lang.confidence_score:.0%}**")
                    
                    st.markdown("---")
                    
                    # 4. Named Entities
                    st.subheader("🏷️ Named Entities")
                    entities_result = client.recognize_entities(documents)[0]
                    
                    if entities_result.entities:
                        entity_data = []
                        for entity in entities_result.entities[:10]:
                            entity_data.append({
                                "Entity": entity.text,
                                "Category": entity.category,
                                "Confidence": f"{entity.confidence_score:.0%}"
                            })
                        
                        # Display as table
                        st.dataframe(entity_data, use_container_width=True, hide_index=True)
                    else:
                        st.info("No entities detected")
                    
                    st.markdown("---")
                    
                    # 5. PII Detection
                    st.subheader("🔒 Personal Information (PII)")
                    try:
                        pii_result = client.recognize_pii_entities(documents)[0]
                        
                        if pii_result.entities:
                            st.warning(f"⚠️ {len(pii_result.entities)} PII entities detected")
                            
                            pii_data = []
                            for entity in pii_result.entities:
                                pii_data.append({
                                    "Type": entity.category,
                                    "Text": entity.text
                                })
                            st.dataframe(pii_data, use_container_width=True, hide_index=True)
                            
                            # Show redacted version
                            with st.expander("👁️ View Redacted Text"):
                                st.code(pii_result.redacted_text)
                        else:
                            st.success("✅ No personal information detected")
                    except:
                        st.info("PII detection not available for this language")
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    st.info("💡 Make sure your credentials are correct")
    
    elif user_text:
        st.warning("⚠️ Please enter Azure credentials in the sidebar")
    else:
        st.info("👈 Enter text to analyze")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 Features")
st.sidebar.markdown("""
- 😊 Sentiment Analysis
- 🔑 Key Phrase Extraction
- 🌍 Language Detection
- 🏷️ Named Entity Recognition
- 🔒 PII Detection
""")

st.sidebar.markdown("---")
st.sidebar.caption("Built with Streamlit & Azure AI")