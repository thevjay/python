# Persona Based Prompting
from dotenv import load_dotenv
from openai import OpenAI

import json

load_dotenv()

client = OpenAI(
    api_key="AIzaSyBjA34ENgeGNplvIqCP-qcH2fuMkqxd7o",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Zero Shot Prompting: Directly giving the insert to the model  
SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Vijay.
    You are acting on behalf of Vijay who is 25 years old Tech enthusiatic and
    principle engineer. Your main tech stack is JS and Python and You are leaning GenAI these days.

    Examples:
    Q: Hey
    A: Hey, Whats up!
"""
message_history = [
    { "role":"system","content": SYSTEM_PROMPT}
]

user_query = input(" ")
message_history.append({ "role":"user","content": user_query })

response=client.chat.completions.create(
    model="gpt-4o",
    response_format={"type":"json_object"},
    messages=[
        {"role":"system","content": SYSTEM_PROMPT },
        {"role":"user","content":"Hey, Can you tell me a joke"}
    ]
)
