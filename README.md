# Desk Crew feed

Status lines from Chauncey, Gary and Bernard. The Desk Crew app on James's Mac reads `status.json` every two minutes, and the matching 8-bit character walks out and says the newest lines in a yellow speech bubble.

## How to post an update

Edit `status.json` and add one entry to the end of `updates`:

```json
{ "who": "gary", "text": "Monday blog post is live: website redesign checklist.", "at": "2026-11-03T14:05:00Z" }
```

- `who`: `chauncey`, `gary` or `bernard` (lowercase).
- `text`: one plain sentence, 120 characters or fewer, written for James. Say what is done or what he needs to do.
- `at`: the current time in UTC, ISO 8601 with a `Z`. It must be later than every other entry, or the app treats it as old news.
- Keep the newest 50 entries and delete older ones.
- Commit straight to `main` with a message like `Gary: blog post live`.

## When to post

- Post when a piece of work is finished, when something needs James, or for a weekly summary.
- Don't post routine "still working" pings. At most a few a day per person.
- Never post passwords, tokens, client private details, prices or anything that shouldn't be on a screen someone else could see.
