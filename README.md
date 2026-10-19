# Exec Vault: an Obsidian vault Claude Code can actually run

A sample executive knowledge vault (fictional firm, fictional clients) built the way I run my own: plain Markdown in Obsidian, one short `CLAUDE.md` rules file that Claude Code reads first, skills for the daily routines, and a check script that catches the drift before it matters.

```
exec-vault/
├── CLAUDE.md                  rules + pointers only, 30 lines, read first every session
├── connections.md             Calendar · ClickUp · GoHighLevel · Telegram: what each may read/write, what happens when one fails
├── Home.md                    Obsidian map of content
├── 00 Inbox/                  unfiled; sorted at the end of every brief
├── 01 Today/today.md          live state of the day (today + yesterday only)
├── 02 Clients/                one note per client: status, contacts, open asks, last touch
├── 03 Meetings/               YYYY-MM-DD Client - Topic.md
├── 04 Decisions/log.md        append-only: what, why, who, when
├── 05 People/                 one note per person
├── 90 Archive/                never delete, move here
├── .claude/skills/
│   ├── daily-brief/           7am: calendar + ClickUp + recent clients → today.md + Telegram draft
│   └── meeting-notes/         raw notes → meeting note, client note and decisions log updated
├── tools/vault_check.py       broken links, missing frontmatter, CLAUDE.md length
└── examples/before/           the same vault, the way most of them start
```

## Before and after

`examples/before/` is the same information the way vaults usually grow: client details pasted into `CLAUDE.md`, notes with no frontmatter, links to names that don't match any file, and rules that contradict each other ("if unsure, ask Dana. Actually don't ask Dana, just guess." / "if the calendar fails, use last week's calendar").

```
$ python3 tools/vault_check.py examples/before
5 notes checked in before/
  FAIL broken link [[People/Priya]] in CLAUDE.md
  FAIL no frontmatter: Clients/bayou.md
  FAIL broken link [[scope v3 FINAL]] in Clients/bayou.md
  ...
  FAIL CLAUDE.md is 80 lines (max 60): move content into the folders it points to
11 problems

$ python3 tools/vault_check.py
10 notes checked in exec-vault/
OK: 0 problems
```

## The rules that make it work

1. **`CLAUDE.md` holds rules and pointers, never content.** Every line is read on every session, so client details live in `02 Clients/` and the rules file just says where.
2. **One live state file, kept small.** `today.md` holds today and yesterday; older days are archived. Claude reads it second and trusts it over its own memory.
3. **Filenames are the links.** A client note is named after the client, so `[[Bayou Freight]]` always resolves and Obsidian's graph stays honest.
4. **Frontmatter on every note** (`type`, `updated`): the newer `updated` wins when two notes disagree, and staleness is visible.
5. **Connections declare their failure mode.** A tool that's down shows at the top of the brief; nothing is guessed from old data.
6. **Nothing leaves the vault without "send".** Telegram, ClickUp comments and GoHighLevel notes are drafted in the vault first.

## Try it

Open the folder in Obsidian, or in Claude Code run `claude` in the folder and say "brief". Run `python3 tools/vault_check.py` after any reorganization.

Built by James Bradford (Akapulu Labs). The firm, people and clients here are fictional.
