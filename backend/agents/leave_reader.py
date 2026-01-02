from ollama import chat
import json

def read_leave_request(text: str) -> dict:
    prompt = f"""
You are an AI assistant working in an HR automation system.

Your task:
Extract structured information from the employee leave request below.

Rules:
- Return ONLY valid JSON
- Do NOT add explanations
- Do NOT include markdown
- Use ISO date format: YYYY-MM-DD

Fields required:
- employee_name
- start_date
- end_date
- reason

Leave request:
{text}
"""

    response = chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    content = response["message"]["content"]

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise ValueError("LLM did not return valid JSON")
