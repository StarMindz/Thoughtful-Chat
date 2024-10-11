# Import necessary modules
import asyncio
import streamlit as st
from geminiChat import chat

# Predefined questions and answers
qa_pairs = [
    {
        "question": "What does the eligibility verification agent (EVA) do?",
        "answer": "EVA automates the process of verifying a patient's eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
    },
    {
        "question": "What does the claims processing agent (CAM) do?",
        "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
    },
    {
        "question": "How does the payment posting agent (PHIL) work?",
        "answer": "PHIL automates the posting of payments to patient accounts, ensuring accurate reconciliation of payments and reducing administrative burden."
    },
    {
        "question": "Tell me about Thoughtful AI's Agents.",
        "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
    },
    {
        "question": "What are the benefits of using Thoughtful AI's agents?",
        "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
    }
]

# Streamlit page configuration: Sets up the title and icon for the web page
st.set_page_config(page_title="Thoughtful AI Support", page_icon="🤖")

# Setup App's Title and description on Streamlit page
st.title("Thoughtful AI Customer Support Agent")
st.markdown("Ask me anything about Thoughtful AI!")

# Add custom CSS to style the UI components
st.markdown(
    """
    <style>
    .user-message {
        text-align: right;
        background-color: #E0F7FA;
        padding: 10px;
        border-radius: 10px;
        margin: 5px;
    }
    .bot-message {
        text-align: left;
        background-color: #F1F8E9;
        padding: 10px;
        border-radius: 10px;
        margin: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize chat history using session state to persist across app reruns
if "messages" not in st.session_state:
    st.session_state.messages = []  # Initialize an empty list to store messages

# Asynchronous Function to handle bot responses based on user input
async def get_response(user_input):
    # Check if an exact match exists in the predefined dataset
    for qa in qa_pairs:
        if user_input.lower() == qa["question"].lower():
            return qa["answer"]

    # If no exact match, generate a response using the chat function
    prompt = f"""
    User query: "{user_input}"
    
    Here's the predefined question-answer dataset below:
    {[qa for qa in qa_pairs]}
    """
    print("Prompt", prompt)
    # Call chat to generate the response if no predefined answer is found
    response = await chat(message=prompt)

    return response

# Synchronous wrapper for the async function
def run_send_message():
    asyncio.run(send_message())

# Function to handle sending the message and updating the chat history
async def send_message():
    """Handle user input, generate bot response, and update the chat history."""
    user_input = st.session_state.user_input  # Get user input from session state
    if user_input:  # If the user has entered something
        # Append user's message to the chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Get bot's response and append to the chat history
        bot_response = await get_response(user_input)
        st.session_state.messages.append({"role": "bot", "content": bot_response})
        
        # Clear the input field after sending the message
        st.session_state.user_input = ""

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-message'>You: {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-message'>Bot: {msg['content']}</div>", unsafe_allow_html=True)

# Input box for sending messages
st.text_input("You:", key="user_input", on_change=run_send_message)  # Tied to the synchronous wrapper
