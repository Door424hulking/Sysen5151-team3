"""DormFix service-layer walking skeleton."""

from intake_model import structure_request
from ticket_store import create_ticket


def submit_maintenance_request(description: str) -> dict:
    """Run one stubbed maintenance request through the DormFix architecture."""
    structured_request = structure_request(description)
    ticket = create_ticket(structured_request)

    return {
        "message": "Maintenance request submitted.",
        "ticket": ticket,
    }
