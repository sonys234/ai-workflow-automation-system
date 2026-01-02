from workflows.leave_workflow import process_leave_request

leave_request = """
Hello,
This is Rahul.
I would like to apply for leave from 12 Jan 2026 to 14 Jan 2026
due to a family function.
"""

result = process_leave_request(leave_request)
print(result)
