# Prompt Log

## 2026-09-19 — Team 3 

Built from:
- DormFix system context model
- DormFix operational concept
- UC.1 Resident Requests Maintenance

Prompt purpose:
Assist with establishing the Chapter 1 repository scaffold and documentation structure based on the team's existing DormFix model and product concept.

Reviewed by:
Team 3 Zhengxu An

Assistant assumptions:
No additional product features were promoted beyond the team's modeled scope. Repository artifacts were reviewed against the SYSEN 5151 Lab Manual before being added.
## 2026-09-19 — Team 3 

Built from:
- UC.1 Resident Requests Maintenance
- DormFix planned behavioral sequence
- docs/walking-skeleton.md

Prompt purpose:
Generate the Chapter 2 DormFix walking skeleton using stub participants that match the UC.1 architectural call sequence.

Components:
- resident_interface
- ticket_service
- intake_model
- ticket_store

Constraints:
- hard-coded stub values only
- no real SQLite access
- no real language-model call
- no error handling
- no retries
- no logging
- no functionality outside UC.1

Reviewed by:
Team 3

Assistant assumptions:
The provisional UC.1 call order uses resident_interface, ticket_service, intake_model, and ticket_store. This call sequence must be reconciled with the final Innoslate Sequence Diagram when the diagram is completed.
