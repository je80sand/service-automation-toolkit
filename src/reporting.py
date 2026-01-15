def format_summary(record: dict) -> str:
    """
    Formats a job record into a readable summary.
    """

    return (
        "\n========== JOB SUMMARY ==========\n"
        f"Time Completed : {record['timestamp']}\n"
        f"Customer : {record['customer_name']}\n"
        f"Address : {record['service_address']}\n"
        f"Issue : {record['issue_reported']}\n"
        f"Status : {record['status']}\n"
        "================================\n"
    )