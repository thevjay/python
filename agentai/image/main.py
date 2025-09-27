from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role":"user",
            "content":[
                {"type":"text", "text":"Generate a caption for this image in about 50 words"},
                {"type": "image_url", "image_url":{"url":""}}
            ]
        }
    ]
)

print("Response:", response.choices[0].message.content)