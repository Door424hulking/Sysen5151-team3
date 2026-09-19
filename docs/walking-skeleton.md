# DormFix Walking Skeleton

## Scope and model references

This canned scenario refines UC.1, Resident Requests Maintenance. It carries one routine, non-emergency request through description, missing-information exchange, draft review, and explicit submission. It demonstrates interface and call ordering; it does not implement production behavior.

- [UC.1 business Sequence](https://cloud.innoslate.com/cornell/p/748/diagrams/sequence/184356): the existing Student Resident–DormFix system-boundary view.
- [UC.1.WS Walking Skeleton Internal Calls](https://cloud.innoslate.com/cornell/p/748/diagrams/sequence/199600): the internal interaction view for the numbered calls below.
- [C.0 DormFix](https://cloud.innoslate.com/cornell/p/748/database/entity/184313) contains the four implementation Assets. They are internal components, not new external stakeholders.

| Model participant | Entity | Code boundary |
|---|---:|---|
| X.C.1 Student Resident | [184315](https://cloud.innoslate.com/cornell/p/748/database/entity/184315) | Canned scenario driver in `app.py` |
| C.1 resident_interface | [199592](https://cloud.innoslate.com/cornell/p/748/database/entity/199592) | `resident_interface/__init__.py` |
| C.2 ticket_service | [199594](https://cloud.innoslate.com/cornell/p/748/database/entity/199594) | `ticket_service/__init__.py` |
| C.3 intake_model | [199595](https://cloud.innoslate.com/cornell/p/748/database/entity/199595) | `intake_model/__init__.py` |
| C.4 ticket_store | [199596](https://cloud.innoslate.com/cornell/p/748/database/entity/199596) | `ticket_store/__init__.py` |

## Numbered interaction sequence

Synchronous return values retrace their callers. The table names those return paths explicitly without treating them as new direct calls between unrelated components. The response labels `missing_information_prompt`, `structured_ticket_draft`, and `ticket_confirmation` identify returned information, not additional Python functions.

| # | Sender → receiver | Call or response | UC.1 trace |
|---:|---|---|---|
| 1 | Student Resident → resident_interface | `describe_issue(description)` | UC.1.1 Describe Maintenance Issue |
| 2 | resident_interface → ticket_service | `begin_request(description)` | UC.1.2 Capture Maintenance Description |
| 3 | ticket_service → intake_model | `structure_request(description)`; fixed incomplete draft returns to ticket_service, then resident_interface | UC.1.3 Extract Request Details; UC.1.4 Identify Missing Information |
| 4 | resident_interface → Student Resident | `missing_information_prompt`: the returned `prompt` text, displayed by app.py | UC.1.5 Request Missing Information |
| 5 | Student Resident → resident_interface | `provide_information(draft, supplemental_information)` | UC.1.6 Provide Missing Information |
| 6 | resident_interface → ticket_service | `complete_request(draft, supplemental_information)`; fixed complete draft returns to resident_interface | UC.1.6 internal refinement |
| 7 | resident_interface → Student Resident | `structured_ticket_draft`: the complete_request return value, displayed before submission | UC.1.7 Present Structured Request; UC.1.8 Review Structured Request |
| 8 | Student Resident → resident_interface | `submit_issue(confirmed_draft)` | UC.1.9 Submit Maintenance Request |
| 9 | resident_interface → ticket_service | `submit_maintenance_request(confirmed_draft)` | UC.1.9 internal refinement |
| 10 | ticket_service → ticket_store | `create_ticket(confirmed_draft)`; fixed ticket returns to ticket_service, then resident_interface | UC.1.10 Create Maintenance Ticket |
| 11 | resident_interface → Student Resident | `ticket_confirmation`: the returned ticket confirmation fields, displayed by app.py | UC.1.10 result and end-to-end return |

Business Sequence messages UC.1.1, UC.1.5, UC.1.6, UC.1.7, and UC.1.9 map to refinement interactions 1, 4, 5, 7, and 8 respectively. Resident review is represented by displaying the complete draft before the separate submission call. There is no production confirmation validation or interactive user interface in this increment.

## Run the canned scenario

From the repository root:

```sh
python app.py
```

The scenario uses only the Python standard library. The description is `The sink is leaking.` The initial intake stub returns category `plumbing` and missing fields `location` and `availability`.

The second stage accepts the modeled draft and supplemental-information arguments but deliberately returns a fixed example, without processing or validating those inputs:

- Location: `Example residence, Room 101`
- Availability: `Example access window`
- Missing fields: `[]`

These are demonstration fixtures, not real resident or housing information. The complete draft is displayed before app.py makes a separate submission call. Only the submission stage calls ticket_store. The final fixed result is ticket `DORMFIX-001`, status `submitted`, category `plumbing`, and no missing fields in this canned request.

## Verification boundary

The local scenario run exits successfully. A separate execution check confirmed that ticket creation is not called during description or supplementation, is called exactly once after explicit submission, and receives the same complete draft that was presented for review. This verifies only the canned path and interface ordering. It does not establish that other inputs, real users, or deployed services are supported.

The saved refinement must also be checked against this call list. A successful Python run alone does not prove model alignment.

## Out of scope

- Real database access or persistence
- A real language-model call or classification logic
- Input validation, authentication, or interactive UI
- Error handling, retries, or logging
- Automated technician assignment, billing, parts purchasing, or emergency response
