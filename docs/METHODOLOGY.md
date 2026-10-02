# Methodology

## Problem model
Marketing content often moves through multiple review states while context is split across messages, documents, and tools. This demonstration compresses the minimum useful approval context into one inspectable queue.

## Workflow
Each record follows:
`content item -> current state -> owner -> due timing -> rationale/history -> next action`

The interface does not decide approval. It exposes enough state for a human to see what requires attention.

## Product behavior
The static client-side application:
- renders a synthetic queue;
- filters by approval state;
- filters by owner;
- searches visible record content;
- opens row detail with rationale and history;
- updates visible result counts;
- supports keyboard activation of queue rows.

There is no server-side logic, persistence, remote API, or external dependency.

## State semantics
- **Needs review** — a human decision/check is outstanding.
- **Waiting** — progress depends on an external input or response.
- **Approved** — the synthetic example has a recorded positive decision.
- **Rejected** — the synthetic example has a recorded negative decision and next action.

These labels are demonstration state, not real-world approvals.

## Design choice
The build is intentionally small. The experiment is whether a bounded operational workflow can be built, documented, tested, independently reviewed, published, and honestly constrained end to end.
