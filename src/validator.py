def validate_ticket(raw_input: str):
    """
    Validates and parses a service ticket string.

    Expected format:
        name, address, issue
    """

    fields = [part.strip() for part in raw_input.split(",")]

    if len(fields) != 3:
        return False, "Input must be: name, address, issue"

    name, address, issue = fields

    if not name or not address or not issue:
        return False, "All fields are required"

    return True, {
        "name": name,
        "address": address,
        "issue": issue
    }