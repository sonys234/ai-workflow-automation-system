from agents.leave_reader import read_leave_request
from agents.leave_decision import decide_leave
from db.database import insert_leave_request

def process_leave_request(leave_text: str) -> dict:
    workflow_result = {
        "status": "FAILED",
        "leave_data": None,
        "decision": None,
        "error": None
    }

    try:
        leave_data = read_leave_request(leave_text)
        workflow_result["leave_data"] = leave_data

        decision = decide_leave(leave_data)
        workflow_result["decision"] = decision

        status = "COMPLETED"

        insert_leave_request(
            leave_data=leave_data,
            decision_data=decision,
            status=status
        )

        workflow_result["status"] = "SUCCESS"

    except Exception as e:
        workflow_result["error"] = str(e)

    return workflow_result
