from datetime import datetime


def build_job_record(ticket: dict) -> dict:
    """
    Creates a completed job record from validated ticket data.
    """

    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "customer_name": ticket["name"],
        "service_address": ticket["address"],
        "issue_reported": ticket["issue"],
        "status": "Completed"
    }