from datetime import datetime

def decide_leave(leave_data: dict) -> dict:
    """
    Applies business rules to decide leave approval.
    """

    try:
        start_date = datetime.fromisoformat(leave_data["start_date"])
        end_date = datetime.fromisoformat(leave_data["end_date"])
        reason = leave_data.get("reason", "").lower()
    except Exception:
        return {
            "decision": "ESCALATE",
            "comment": "Invalid or missing date format"
        }

    leave_days = (end_date - start_date).days + 1

    # Rule 1: Missing reason
    if not reason:
        return {
            "decision": "REJECTED",
            "comment": "Leave reason not provided"
        }

    # Rule 2: Long leave
    if leave_days > 5:
        return {
            "decision": "ESCALATE",
            "comment": "Leave duration exceeds automatic approval limit"
        }

    # Rule 3: Acceptable reasons
    if any(keyword in reason for keyword in ["family", "personal", "medical"]):
        return {
            "decision": "APPROVED",
            "comment": "Leave approved under standard policy"
        }

    # Fallback
    return {
        "decision": "ESCALATE",
        "comment": "Reason requires manual review"
    }
