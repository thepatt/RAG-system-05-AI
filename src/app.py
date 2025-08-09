import streamlit as st
from chatbot.backend import ChatBot
from utils.ui_settings import UISettings

# Configure Streamlit page
st.set_page_config(
    page_title="AgentGraph Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Main app
st.title("🤖 AgentGraph Chatbot")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        # Add feedback buttons for assistant messages
        if message["role"] == "assistant":
            col1, col2, col3 = st.columns([1, 1, 10])
            with col1:
                if st.button("👍", key=f"like_{len(st.session_state.messages)}_{message['content'][:10]}"):
                    UISettings.feedback(message["content"], liked=True)
            with col2:
                if st.button("👎", key=f"dislike_{len(st.session_state.messages)}_{message['content'][:10]}"):
                    UISettings.feedback(message["content"], liked=False)

# Chat input
if prompt := st.chat_input("Enter your message..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ChatBot.respond(st.session_state.messages.copy(), prompt)
            st.markdown(response)

# Sidebar with controls
with st.sidebar:
    st.header("Controls")
    
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    
    st.header("Chat Statistics")
    st.metric("Total Messages", len(st.session_state.messages))
    user_messages = len([m for m in st.session_state.messages if m["role"] == "user"])
    st.metric("User Messages", user_messages)
    st.metric("Assistant Messages", len(st.session_state.messages) - user_messages)
