# Environment

Language / version: Python 3.12

Runtime: Local Python virtual environment

User interface: Streamlit

API framework: FastAPI

Database: SQLite

Model runner: LM Studio (local hosting)

Language model: Llama 3.1 8B Instruct (initial selection)

Editor: Visual Studio Code

Source control: GitHub

System modeling environment: Innoslate

## Development assistants

- Gengrui Jiang (`gj248-arch`): Codex, used for the documentation update recorded
  in [the prompt log](prompt-log.md). The assistant model identifier has not been
  recorded and needs confirmation from the session settings.
- The original team environment record listed ChatGPT without naming the
  individual users or model identifiers. That historical declaration is retained
  here without assigning it to any member.
- Other team members: individual assistant usage remains to be confirmed by each
  member; record the member's name and actual assistant, or explicitly state
  that no assistant was used.

The product model and runner selections above come from
[ADR-0001](adr/0001-initial-toolchain.md#model-hosting-decision).
They describe the planned runtime integration. The Chapter 2 walking skeleton
currently returns stub values and does not invoke the model.
