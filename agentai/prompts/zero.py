from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AIzaSyBjA34ENgeGNplvIqCP-qcH2fuMkqxd7o",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Zero Shot Prompting: Directly giving the insert to the model  
SYSTEM_PROMPT = "you should only and only ans the coding related questions. Do not ans anything else. Your name is Alexa. If user asks something other than coding, just say sorry."
response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content": SYSTEM_PROMPT },
        {"role":"user","content":"Hey, Can you tell me a joke"}
    ]
)

print(response.choices[0].message.content)
# 1. Zero-shot Prompting: The model is given a direct question or task without prior examples.
