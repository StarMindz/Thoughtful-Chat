import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()

# Configure the API key for Google Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="You are a customer support AI for Thoughtful AI. Your primary task is to answer user queries using a predefined question-answer dataset given by the user. If you find an exact match, respond with the corresponding answer. If no exact match exists, locate the most similar question and provide the related answer. If no similar query is found, generate a meaningful, context-aware response using your general knowledge. Always provide a clear, concise, and accurate response that directly addresses the user's query without explaining your thought process.",
)

class Chat(BaseModel):
    message: str

async def chat(message):
    try:
        # Start a chat session with the Gemini model
        chat_session = model.start_chat()
        
        # Send the user's message to the Gemini model
        response = chat_session.send_message(message)
        if response and response.text:
            # Convert the response to a string
            if isinstance(response.text, (dict, list)):
                return json.dumps(response.text)  # Convert JSON objects or lists to a string
            else:
                return str(response.text)
        else:
            return "Sorry, I couldn't generate a response."

    except Exception as e:
        # Return the error message for debugging purposes
        return f"Error: {str(e)}"
