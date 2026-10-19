# CLAUDE.md — Executive Vault

You maintain this Obsidian vault for Dana Whitlock, managing partner at Northgate Advisory (fictional sample firm).
Read this file first, every session. Keep it under 60 lines: rules and pointers only. Content lives in the folders.

## Where things live
- `01 Today/today.md` — the live state of the day. Read it SECOND, right after this file. Trust it over memory.
- `02 Clients/` — one note per client: status, contacts, open asks, last touch. Filename = client name.
- `03 Meetings/` — one note per meeting, `YYYY-MM-DD Client - Topic.md`, made by the `meeting-notes` skill.
- `04 Decisions/log.md` — append-only. What was decided, why, by whom, date.
- `05 People/` — one note per person: role, company, how Dana knows them, last contact.
- `00 Inbox/` — anything unfiled. Sort it into the folders above at the end of each brief.
- `90 Archive/` — closed clients and old days. Never delete; move here.
- `connections.md` — every outside tool this vault can reach, and what it may read or write.

## Rules
- Every note starts with frontmatter: `type`, `updated` (YYYY-MM-DD), and `client` or `person` when it applies.
- Link people and clients with `[[wikilinks]]` by filename. A link to a note that doesn't exist yet is fine; it marks a note to create.
- When two notes disagree, the newer `updated` date wins, and fix the older one in the same session.
- `today.md` holds today and yesterday only. Older days move to `90 Archive/days/`.
- Never send anything outside the vault (Telegram, email, GoHighLevel, ClickUp comments) without Dana's explicit "send".
- Write like Dana reads: short lines, decisions first, no filler.
- When Dana corrects a fact, fix the note it lives in during the same session, not later.

## Routines (skills in `.claude/skills/`)
- `daily-brief` — 7:00am: calendar + ClickUp due today + client notes touched in 7 days → `01 Today/today.md`, then a 5-line summary to Telegram (drafted, sent only on approval).
- `meeting-notes` — after a call: raw notes in, a meeting note out, client note and decisions log updated.

## Checks
- Run `python3 tools/vault_check.py` after any reorganization. Zero broken links, zero notes without frontmatter, this file under 60 lines.
