import streamlit as st
from openai import OpenAI
import os

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
import os

os.environ='OPEN_API_KEY'

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
prompt = st.text_input("What is up?")
if prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        
    # Generate response from OpenAI
    with st.chat_message("assistant"):
        response = client.Completion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            max_tokens=150,
            stream=True,
        )
        full_response = ""
        for chunk in response:
            full_response += chunk.choices[0].text
            st.markdown(chunk.choices[0].text)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
