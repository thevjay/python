from transformers import pipeline

pipe = pipeline("image-text-to-text",model="google/gemma-3-4b-it")

messages = [
    {
        "role":"user",
        "content":[
            {"type":"image","url":"https://huggingface.co/datasets/huggingface"},
            {"type":"text","text":"What animal is on the candy"}
        ]
    }
]

pipe(text=messages)