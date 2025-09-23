from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AIzaSyBjA34ENgeGNplvIqCP-qcH2fuMkqxd7o",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":"You are an expert in Maths and only and only ans maths reality"},
        {"role":"user","content":"Hey, I am vIjay "}
    ]
)

print(response.choices[0].message.content)