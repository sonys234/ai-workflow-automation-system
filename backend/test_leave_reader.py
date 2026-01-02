from agents.leave_reader import read_leave_request

leave_text = """
Hi, this is Rahul.
I need leave from 12 Jan 2026 to 14 Jan 2026 because of a family function.
"""

result = read_leave_request(leave_text)
print(result)
