import streamlit as st
from summarization_inference import summarize_text

# Show title and description.
st.title("📝 Text Summarization Chatbot")
st.write(
    "This app uses an advanced text summarization pipeline powered by Cohere and LangChain."
    "You can input a long piece of text, and we'll generate a concise summary for you! ")
st.write(    
    "To use this app, you need to provide your Cohere API key. "
)

# Ask user for their Cohere API key via `st.text_input`.
cohere_api_key = st.text_input("Cohere API Key", type="password")
if not cohere_api_key:
    st.info("Please add your Cohere API key to continue.", icon="🗝️")
else:
    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message (text to summarize).
    if text_to_summarize := st.chat_input("Enter text to summarize..."):
        # Store and display the current input text.
        st.session_state.messages.append({"role": "user", "content": text_to_summarize})
        with st.chat_message("user"):
            st.markdown(text_to_summarize)

        # Generate a summary using the summarization inference function.
        try:
            with st.chat_message("assistant"):
                with st.spinner("Generating summary..."):
                    summary = summarize_text(text_to_summarize, cohere_api_key)
                st.markdown(summary)
            st.session_state.messages.append({"role": "assistant", "content": summary})
        except Exception as e:
            st.error(f"⚠️ An error occurred: {str(e)}")