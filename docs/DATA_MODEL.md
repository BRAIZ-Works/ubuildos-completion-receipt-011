# Data Model

Each synthetic queue item contains:

| Field | Meaning |
|---|---|
| `id` | Local record identifier |
| `title` | Content item name |
| `channel` | Example distribution channel |
| `priority` | Example urgency label |
| `status` | Needs review / Waiting / Approved / Rejected |
| `owner` | Synthetic responsible person |
| `due` | Human-readable timing |
| `next` | Explicit next action |
| `rationale` | Why the item is in its current state |
| `history` | Small decision/event history |

## Data boundary

All shipped records are synthetic examples. The product contains no intended customer, employee, prospect, or campaign production data.

## Persistence boundary

Records live in static JavaScript in the release. Refreshing the page restores the shipped sample state. There is no database or write-back path.
