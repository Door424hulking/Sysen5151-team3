# ADR-0001: Initial Toolchain

Status: Accepted

## Context

DormFix requires a lightweight prototype architecture that supports a web-based user interface, a REST API, persistent maintenance-ticket storage, and configurable language-model assistance.

## Decision

The initial DormFix prototype will use:

- Python 3.12
- Streamlit for the user interface
- FastAPI for the REST API
- SQLite for ticket storage
- A configurable language model for assisted maintenance-report intake
- GitHub for source control and team collaboration
- Innoslate for systems modeling

## Rationale

The selected technologies support rapid prototype development and provide a straightforward architecture for demonstrating the complete maintenance workflow from issue reporting through repair confirmation. The technology stack also allows the language-model component to remain configurable while the rest of the application architecture remains stable.

## Model Hosting Decision

The specific language-model runner and whether the model will be locally hosted or accessed through a hosted service have not yet been finalized.

## What Would Change This Decision

The team may revisit this toolchain if later testing identifies unacceptable performance, deployment limitations, integration difficulties, data-security concerns, or language-model capability limitations.
