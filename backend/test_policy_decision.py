from agents.policy_decision import policy_based_decision

leave_data = {
    "employee_name": "Rahul",
    "start_date": "2026-01-12",
    "end_date": "2026-01-14",
    "reason": "family function"
}

result = policy_based_decision(leave_data)
print(result)
