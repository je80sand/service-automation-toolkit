from validator import validate_ticket
from job_log import build_job_record
from reporting import format_summary


def run():
    """
    Main entry point for the service automation tool.
    """

    user_input = input(
        "Enter service ticket (name, address, issue): "
    ).strip()

    is_valid, result = validate_ticket(user_input)

    if not is_valid:
        print(f"\nERROR: {result}\n")
        return

    job_record = build_job_record(result)
    summary = format_summary(job_record)

    print(summary)


if __name__ == "__main__":
    run()