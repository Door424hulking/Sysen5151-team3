# DormFix Walking Skeleton

## UC.1 — Resident Requests Maintenance

The walking skeleton represents the primary DormFix use case in which a Student Resident submits a routine, non-emergency maintenance request.

The purpose of this increment is to verify that one resident action can travel through the major architectural participants and return a response of the correct shape. All participant behavior is stubbed. No real database access or language-model call is performed.

## Call Sequence

1. Student Resident -> resident_interface:
   submits maintenance description

2. resident_interface -> ticket_service:
   submit_maintenance_request(description)

3. ticket_service -> intake_model:
   structure_request(description)

4. intake_model -> ticket_service:
   returns structured maintenance information

5. ticket_service -> ticket_store:
   create_ticket(structured_request)

6. ticket_store -> ticket_service:
   returns stub ticket record

7. ticket_service -> resident_interface:
   returns ticket confirmation

8. resident_interface -> Student Resident:
   displays ticket confirmation

## Stub Input

Example resident description:

"The sink is leaking."

## Expected Stub Result

The walking skeleton returns a ticket confirmation containing a hard-coded structured request and ticket identifier.

Example:

- Ticket ID: DORMFIX-001
- Category: plumbing
- Status: submitted
- Missing information:
  - location
  - availability

## Out of Scope

This walking skeleton does not include:

- real SQLite database access
- a real language-model call
- real classification logic
- authentication
- error handling
- retries
- logging
- automated technician assignment
- billing
- parts purchasing
- emergency response
