import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_code(user_prompt):
    # Define the AI's personality and rules
    system_prompt = (
        "You are Kernel, an expert AI coding assistant. "
        "Provide the code first, then a brief explanation. "
        "Use C++ by default unless the user specifies another language."
    )

    # Send the request to Groq's servers
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        model="openai/gpt-oss-120b", 
    )

    # Extract and return the text
    return chat_completion.choices[0].message.content