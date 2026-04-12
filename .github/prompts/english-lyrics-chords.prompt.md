---
name: "English Lyrics And Chords Post"
description: "Use when: creating an English lyrics post with chords, especially using the Desperado-style inline chord layout"
argument-hint: "Artist, song title, image URL, Spotify embed, lyrics, chords/key, and permission to publish"
agent: "agent"
---

Load [copilot-instructions.md](../../copilot-instructions.md) and use [Desperado](../../_posts/2026-04-12-eagles-desperado.md) plus the most recent matching post as references.

Create a new Jekyll post with:
- Artist: [artist]
- Song title: [song]
- Language: English
- Include chords: yes
- Chord layout: [reuse Desperado inline layout / compact / other]
- I have permission to publish the lyrics and chords: [yes/no]
- Image URL: [url]
- Spotify embed: [iframe or none]
- Lyrics: [paste lyrics]
- Chords/key: [paste chords or say "use standard original-key arrangement"]

Requirements:
- Follow [copilot-instructions.md](../../copilot-instructions.md) exactly.
- Use categories `[Lyrics, English]` and existing repo tag conventions.
- Add the full Song Summary.
- Use theme-aware chord styling that works in dark mode.
- Avoid orphaned chords or empty lyric spans.
- Run `./tools/test.sh`.
- Make one complete implementation pass before asking follow-ups unless something essential is missing.
- After finishing, summarize only the result and any real issues.
