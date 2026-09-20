# Prompt Log

## 2026-09-19 — Team 3 

Built from:
- DormFix system context model
- DormFix operational concept
- UC.1 Resident Requests Maintenance

Prompt purpose:
Assist with establishing the Chapter 1 repository scaffold and documentation structure based on the team's existing DormFix model and product concept.

Reviewed by:
Team 3

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

## Provenance gaps identified on 2026-09-19

The two historical entries above are preserved unchanged. The individual member,
assistant/model, complete original prompt, human reviewer, review outcome, and
assumption disposition remain unverified. "Reviewed by: Team 3" does not identify
an individual or establish that a human review occurred. Confirm facts from
retained records; leave missing evidence as a gap rather than reconstructing it.

## 2026-09-19 — Documentation repair

Requested by: Gengrui Jiang (`gj248-arch`).
Generated and checked by: Codex. Assistant model identifier: not recorded.

Purpose and files: added the startup command in `README.md`, synchronized
`docs/environment.md` with ADR-0001 (LM Studio / Llama 3.1 8B Instruct), and
recorded known assistant usage and provenance gaps in `docs/prompt-log.md`.

Validation: Codex ran the existing stub successfully with Python 3.12.14 and
checked that both historical entries were preserved. Missing member/model
details remain unknown. Human reviewer and review outcome: pending.

## 2026-09-19 — UC.1 model and walking-skeleton alignment

Requested by: Gengrui Jiang (`gj248-arch`).
Generated and checked by: Codex. Assistant model identifier: not recorded.

Purpose and files: changed `app.py`, `resident_interface/__init__.py`, and
`ticket_service/__init__.py` to separate description, supplementation/draft
review, and submission. Only submission creates the canned ticket. Updated
`docs/walking-skeleton.md` with the eleven numbered UC.1.WS interactions and
participant mapping, and repaired its `README.md` link.

Model source: saved UC.1.WS Sequence 199600 and its four internal Assets.
The original UC.1 business Sequence 184356 remains the system-boundary view.
This dated refinement reconciles the earlier provisional call order; it does
not establish who generated or reviewed the historical work.

Validation by Codex: checked the saved model's eleven ordered interactions and
five lifelines. Ran the actual `app.main` with Python 3.12.14; a local trace
observed all eleven interactions, prompt/draft/ticket display order, no ticket
before submission, and exactly one creation receiving the displayed draft.
A separate Codex review checked the code and mapping; this was AI review.

Assumptions: all inputs, missing-field responses, draft fields, and ticket ID
are fixed fixtures. The second stage returns a canned complete draft. Display
followed by a separate submit call represents review/confirmation. There is no
real model call, persistence, authentication, confirmation validation, error
handling, retry, or logging.

Human reviewer and outcome: pending. Before merge, record the reviewer's name,
date, and actual acceptance, changes, or rejections after comparing the saved
UC.1.WS model, call mapping, and three changed Python files.

## Prompt-record handling

Per the user's request, original repair prompt records are retained locally and
excluded from the current repository tree. This log is a factual AI-usage
summary, not the original prompts; the course prompt-provenance gap remains.
The earlier documentation prompt was removed by a normal commit; that removal
does not erase Git history. The alignment prompt was never committed.
