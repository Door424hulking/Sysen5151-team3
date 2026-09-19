"""DormFix Chapter 2 walking skeleton entry point."""

from resident_interface import submit_issue


def main():
    description = "The sink is leaking."

    result = submit_issue(description)

    print("DormFix Walking Skeleton")
    print("------------------------")
    print(f"Resident report: {description}")
    print(f"Ticket ID: {result['ticket']['ticket_id']}")
    print(f"Status: {result['ticket']['status']}")
    print(f"Category: {result['ticket']['request']['category']}")
    print(
        "Missing information:",
        ", ".join(result["ticket"]["request"]["missing_fields"]),
    )


if __name__ == "__main__":
    main()
