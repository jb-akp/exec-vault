---
name: meeting-notes
description: Turns raw call notes or a transcript into a meeting note, updates the client note and the decisions log. Use right after a call.
---

## Steps

1. Ask for (or read from `00 Inbox/`) the raw notes or transcript, the client, and the date.
2. Create `03 Meetings/YYYY-MM-DD Client - Topic.md` with frontmatter (`type: meeting`, `client`, `updated`) and four sections: **Who**, **Decided**, **Asks** (who owes what, by when), **Notes**.
3. In `02 Clients/<Client>.md`: update `updated`, the status line, and the open asks. Link the meeting note.
4. Append each decision to `04 Decisions/log.md`: date, decision, why, who decided, link to the meeting.
5. If an ask belongs in ClickUp, draft the task under `## ClickUp drafts` in the meeting note. Create it only on Dana's "send".
6. Run `python3 tools/vault_check.py`.
