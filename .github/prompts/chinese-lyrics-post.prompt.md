---
name: "Chinese Lyrics Post"
description: "Use when: creating a new Mandarin or Cantonese lyrics post for this Jekyll site"
argument-hint: "Artist, title, language, image URL, Spotify embed, lyrics, and permission to publish"
agent: "agent"
---

Load [copilot-instructions.md](../../copilot-instructions.md) and use the most recent matching Chinese lyrics post as the template.

Create a new Jekyll post with:
- Artist: [artist Chinese + English]
- Song title: [song Chinese + English translation]
- Language: [Mandarin or Cantonese]
- I have permission to publish the lyrics: [yes/no]
- Image URL: [url]
- Spotify embed: [iframe or none]
- Lyrics: [paste lyrics]
- Romanization needed: [pinyin/jyutping]

Requirements:
- Follow [copilot-instructions.md](../../copilot-instructions.md) exactly.
- Use the correct categories and existing repo tag conventions.
- Add the full Song Summary.
- Format every lyric line correctly.
- Run `./tools/test.sh`.
- Make one complete implementation pass before asking follow-ups unless something essential is missing.
- After finishing, summarize only the result and any real issues.
