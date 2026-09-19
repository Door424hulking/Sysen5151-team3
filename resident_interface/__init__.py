"""Resident-facing interface for the DormFix walking skeleton."""

from ticket_service import submit_maintenance_request


def submit_issue(description: str) -> dict:
    """Submit one resident maintenance description to DormFix."""
    return submit_maintenance_request(description)
