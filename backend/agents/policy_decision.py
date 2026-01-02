import json
import re
from ollama import chat
from utils.policy_retriever import load_policy_retriever

retriever = load_policy_retriever()

def policy_based_decision(leave_data: dict) -> dict:
    query = f"""
Employee leave request details:
Start date: {leave_data['start_date']}
End date: {leave_data['end_date']}
Reason: {leave_data['reason']}
"""

    # Use .invoke instead of .get_relevant_documents
    policy_docs = retriever.invoke(query)
    policy_text = "\n".join([doc.page_content for doc in policy_docs])

    prompt = f"""
You are an HR decision assistant.

Company policy:
{policy_text}

Leave request:
{query}

Task:
Decide whether the leave should be APPROVED, REJECTED, or ESCALATED.
Justify the decision based strictly on company policy.

Return ONLY valid JSON with:
- decision
- justification
"""

    response = chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    raw_output = response["message"]["content"]

    # Safely parse JSON instead of using eval
    try:
        result = json.loads(raw_output)
    except json.JSONDecodeError:
        # If the model adds extra text, extract JSON block with regex
        match = re.search(r"\{.*\}", raw_output, re.DOTALL)
        if match:
            result = json.loads(match.group(0))
        else:
            raise ValueError("No valid JSON found in model response")

    return result