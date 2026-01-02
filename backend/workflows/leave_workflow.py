from agents.leave_reader import read_leave_request
from agents.leave_decision import decide_leave

def process_leave_request(leave_text: str) -> dict:
    """
    Orchestrates the full leave request workflow.
    """

    workflow_result = {
        "status": "FAILED",
        "leave_data": None,
        "decision": None,
        "error": None
    }

    try:
        # Step 1: Read & extract leave data
        leave_data = read_leave_request(leave_text)
        workflow_result["leave_data"] = leave_data

        # Step 2: Make decision
        decision = decide_leave(leave_data)
        workflow_result["decision"] = decision

        workflow_result["status"] = "SUCCESS"

    except Exception as e:
        workflow_result["error"] = str(e)

    return workflow_result
