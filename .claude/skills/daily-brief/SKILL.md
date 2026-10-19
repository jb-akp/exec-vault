---
name: daily-brief
description: Morning brief for Dana. Pulls calendar, ClickUp and recent client notes into 01 Today/today.md and drafts a 5-line Telegram summary. Use at the start of the day or when Dana says "brief".
---

## Steps

1. **Read state.** `CLAUDE.md`, then `01 Today/today.md`. Yesterday's "Tomorrow" section is the starting draft.
2. **Pull live signal** (see `connections.md`; a failure goes on the first line of the brief, never skipped silently):
   - Calendar: today's events with attendees. For each attendee or company, find the matching `[[note]]` in `05 People/` or `02 Clients/`.
   - ClickUp: tasks due today or overdue, assigned to Dana.
   - Client notes in `02 Clients/` with `updated` in the last 7 days.
3. **Write today.** In `01 Today/today.md`, replace the draft with:
   - **Top 3** (deadline-real first)
   - **Meetings**: time, who, one line of context from their note, the open ask
   - **Due**: ClickUp items, overdue marked
   - **Watch**: things waiting on someone else
4. **Prune.** Move the day before yesterday to `90 Archive/days/YYYY-MM-DD.md`. Sort `00 Inbox/` into its folders.
5. **Draft the Telegram summary** (5 lines max) at the bottom of `today.md` under `## Telegram draft`. Send only on Dana's "send".
6. **Check.** Run `python3 tools/vault_check.py`. Fix anything it reports before finishing.

## Rules
- Never invent a meeting, task or contact. If a source is down, say so.
- A meeting with a person who has no note gets a new note in `05 People/` with what the calendar says, marked `type: person, stub: true`.
