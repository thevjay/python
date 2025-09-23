# Few Shot Prompting
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AIzaSyBjA34ENgeGNplvIqCP-qcH2fuMkqxd7o",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Few Shot Prompting: Directly giving the insert to the model and few examples to the model
SYSTEM_PROMPT = """
you should only and only ans the coding related questions. Do not ans anything else. Your name is 
Alexa. If user asks something other than coding, just say sorry.

Rule:
- Strinctly follow the output in JSON format

Output Format:
{{
    "code":"string" or null,
    "isCodingQuestion":boolean
}}

Examples:
Q: Can you explain the a + b whole sq uare?
# A: Sorry, I can only help with Coding related questions. 
A : {{ "code":null, "isCodingQuestion":false }}

Q: Hey, Write a code in python for adding two numbers.
# A: def add(a,b):
#     return a + b
A : {{"code":"def add(a,b):
    return a + b","isCodingQuestion": false
}}  
"""
response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content": SYSTEM_PROMPT },
        {"role":"user","content":"Hey, Can you tell me a joke"}
    ]
)

print(response.choices[0].message.content)
# 2. Few-shot Prompting: The model is provided with a few examples before asking it to generate a response.

