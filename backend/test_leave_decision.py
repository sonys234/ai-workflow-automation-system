from agents.leave_decision import decide_leave

sample_leave = {
    "employee_name": "Rahul",
    "start_date": "2026-01-12",
    "end_date": "2026-01-14",
    "reason": "family function"
}

decision = decide_leave(sample_leave)
print(decision)
