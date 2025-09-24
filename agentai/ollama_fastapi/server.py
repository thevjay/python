from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()
client = Client(
    host="http://localhost:11434",
)

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.post("/chat")
def Chat(
       message: str = Body(..., description="The Message") 
):
    response = client.chat(model="gemma:2b",messages=[
        {"role":" user", "content": message}
    ])

    return { "r esponse": response.message.content}
 