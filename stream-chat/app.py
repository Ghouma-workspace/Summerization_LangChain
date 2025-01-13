import streamlit as st
from summarization_inference import summarize_text

# Streamlit app
st.title("Text Summarization App")
st.write("Enter the text you'd like to summarize below:")

# Input API key
api_key = st.text_input("Enter your Cohere API Key", type="password")

# Text input area
text_to_summarize = st.text_area("Input Text", placeholder="Paste your text here...")

if st.button("Summarize Text"):
    if not text_to_summarize.strip():
        st.error("Please enter some text to summarize!")
    elif not api_key.strip():
        st.error("Please enter your Cohere API key!")
    else:
        # Summarize the text using the inference function
        try:
            with st.spinner("Generating summary..."):
                summary = summarize_text(text_to_summarize, api_key)
                st.success("Summary Generated!")
                st.write(summary)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

st.markdown("### About")
st.write(
    """
    This app uses a custom text summarization pipeline powered by Cohere. 
    Enter your text in the box above and click 'Summarize Text' to get a concise summary.
    """
)