---
type: reference
updated: 2026-10-19
---
# Connections

Every outside system this vault can reach. If it isn't listed here, Claude assumes it can't reach it and asks.

| Tool | How Claude reaches it | Reads | Writes | If it breaks |
|---|---|---|---|---|
| Google Calendar | Google Workspace CLI (`gws calendar events list`) | Today's and tomorrow's events | Nothing (read-only by rule) | Brief says "calendar unavailable" at the top; never guesses meetings |
| ClickUp | ClickUp API via MCP server, token in `.env` | Tasks due today, overdue, assigned to Dana | Task comments, only on "send" | Brief lists "ClickUp unavailable"; last known tasks are NOT reused |
| GoHighLevel | GHL API v2 (location token in `.env`) | Contacts, pipeline stage, last activity | Notes on a contact, only on "send" | Client notes keep their last `updated` date so staleness shows |
| Telegram | Bot API, one private chat with Dana | Nothing | The daily summary, only on "send" | Summary stays in `today.md` |

## Rules
- Tokens live in `.env`, which is gitignored. Never print one, never write one into a note.
- Read before write: every write is preceded by a read of the same record in the same session.
- A connection that fails is reported at the top of the next brief, not silently skipped.
