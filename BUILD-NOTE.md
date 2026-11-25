# BUILD-NOTE — The Funniest Sick-Day Excuse

- Competition: `u-zeroxfive-the-funniest-sick-day-excuse-37423a36`
- Prize: $2 (1st $1.00, 2nd $0.50, 3rd $0.50)
- Opens: 2026-11-24 17:12:13 UTC (00:12 WIB 25 Nov 2026) — already open at build time (built 2026-11-25 ~02:45 UTC)
- Deadline: 2026-11-27 17:10 UTC (00:10 WIB 28 Nov 2026)
- Gate: /output/entry.txt must be UTF-8 text of one line, not only whitespace.
- Entrypoint: `main.py` at repo root (Python 3.13, harness program/v1).

## Entry

> I can't come in - my bed has me hostage, and the ransom is eight more hours of sleep.

- Characters: 85 (gate: one line; see gate note below)
- Bytes (UTF-8): 85
- Lines: 1, no trailing newline
- Whitespace-only: no

## Why this line

A sick-day excuse where the bed is the captor and sleep is the ransom: it
is transparently not an illness, which is the point — the excuse is so
cheerfully dishonest that it almost works. It lands without borrowing any
example text from the brief.

Original work — no anchor, rung, or house text from the kit was copied.

## Gate note

The requirements JSON for this competition states no per-competition
character limit (it carries only the generic platform checks). Sibling
one-line builds in this workspace passed kit gates of 1–160 and 1–200
characters, so this entry is kept at 85 characters — safely inside both.

## Verification (local, run 2026-11-25)

1. Cleaned `/output`, ran `python3 main.py` → `/output/entry.txt` written.
2. Cleaned `/output` again, ran `python3 main.py` a second time.
3. Both runs byte-identical (SHA-256 `2bcb584ee55ceb69e58239e05f9051104ab4ae313ff21abde9160e3d2d904a3e` on both runs), gate check passed: UTF-8 decodes, 85 characters, single line, not whitespace-only.

Run the check yourself:

```sh
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
python3 -c "t=open('/output/entry.txt',encoding='utf-8').read(); print(len(t), repr(t))"
```

## Repo note for the submitter

- Repo must be created after the competition opened (2026-11-24T17:12:13Z) and carry `.makefun/owner.json` naming the linked wallet (included).
- README badges above use `kiw33/u-zeroxfive-the-funniest-sick-day-excuse-37423a36` as the repo name; adjust the rank/reward badge URLs if the repo is created under a different name.
- GitHub About must have a website on make.fun and the topic `makefun` before submitting (kit check `repo_about`).
