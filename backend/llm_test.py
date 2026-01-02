from ollama import chat

response = chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": "Explain what an employee leave request is in one sentence."
        }
    ]
)

print(response["message"]["content"])
