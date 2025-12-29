# Copilot Instructions for Generating New Lyric Posts

Purpose

- Provide clear, concise guidance for GitHub Copilot (or any assistant) to generate new Jekyll lyric posts consistent with the site's existing `_posts`.

Key goals

- Produce valid Jekyll Markdown posts compatible with the Chirpy theme.
- Ensure consistent YAML front matter, emoji usage, lyric formatting, and tagging.
- Preserve editorial style used in existing posts (example: `/_posts/2025-12-20-WangLeeHom-Mistake-at-the-Flower-Field.md`).

Required front matter (YAML)

- Use the exact structure below; replace placeholders accordingly.

---

title: "{Artist (Chinese)} {Artist (English)} - {Song Title (Chinese)} ({English Translation}) Lyrics"
date: YYYY-MM-DD HH:MM:SS -0800
categories:

- Lyrics
- {Mandarin|Cantonese}
  tags:
- chinese
- {mandarin|cantonese}
- {pinyin|jyutping}
- song lyrics
- {c-pop|cantopop}
- {artist-name}
- {YYYY}s
  image:
  path: "{image_url}"

---

YAML rules

- Must start/end with `---` and contain valid YAML only.
- Two-space indentation.
- No comments or Markdown inside YAML.
- `tags` must include the artist tag (lowercase, hyphen-separated) and the release-decade tag (e.g., `2010s`).
- `date` must be the post creation timestamp in `YYYY-MM-DD HH:MM:SS -0800` format; do not use the song release date here.

Timezone and current-time guidance

- Use Pacific Standard Time (PST, offset `-0800`) for the `date` field. The `date` must reflect the generation time in PST.
- Recommended: call a `get_current_time()` helper in PST and format as `YYYY-MM-DD HH:MM:SS -0800` when programmatically creating posts. Example pseudocode:

```py
from datetime import datetime, timezone, timedelta

def get_current_pst_timestamp():
  pst = timezone(timedelta(hours=-8))
  return datetime.now(pst).strftime('%Y-%m-%d %H:%M:%S -0800')

# Usage:
# date: get_current_pst_timestamp()
```

Embeds and helper styles (immediately after YAML)

- If a Spotify URL is provided, include the standard Spotify iframe embed (see examples in `_posts`).
- Always include the small style helper block:

<style>
r { color: Red }
o { color: Orange }
g { color: Green }
</style>

Summary section (Song Summary)

- Header: `## 🎵 Song Summary`
- Metadata lines; each line must end with a single emoji. Include pinyin (for Mandarin) or jyutping (for Cantonese) in parentheses. Example lines:
  - `**Title:** {Chinese} ({Romanization} / {English}) 🎵`
  - `**Artist:** {Chinese} ({Romanization} / {English}) 🎤`
  - `**Album:** {Album Name} 💿`
  - `**Release Year:** {YYYY} 📅`
  - `**Songwriters:** {names} ✍️`
  - `**Genre:** {genre} 🎶`
- Follow with subsections and emojis: `Overview ✨`, `Composition 🎼`, `Release & Album Context 📀`, `Popularity & Reception 🌟`, `Legacy 🕊️`.
- Metadata lines; each line must end with a single emoji. Example lines:
- `**Title:** {Chinese} ({English}) 🎵`
- `**Artist:** {Chinese} {English} 🎤`
- `**Album:** {Album Name} 💿`
- `**Release Year:** {YYYY} 📅`
- `**Songwriters:** {names} ✍️`
- `**Genre:** {genre} 🎶`
- Follow with subsections and emojis: `Overview ✨`, `Composition 🎼`, `Release & Album Context 📀`, `Popularity & Reception 🌟`, `Legacy 🕊️`.
- Layout spacing: insert a single blank line between each metadata line and between subsections and their paragraphs (i.e., separate each item with one empty line for readability). Ensure generated Summary includes these blank lines.
- Metadata lines; each line must end with a single emoji. Example lines:
- `**Title:** {Chinese} ({English}) 🎵`
- `**Artist:** {Chinese} {English} 🎤`
- `**Album:** {Album Name} 💿`
- `**Release Year:** {YYYY} 📅`
- `**Songwriters:** {names} ✍️`
- `**Genre:** {genre} 🎶`
- Follow with subsections and emojis: `Overview ✨`, `Composition 🎼`, `Release & Album Context 📀`, `Popularity & Reception 🌟`, `Legacy 🕊️`.
- Layout spacing: each metadata item must start on its own line; do not insert blank (empty) lines between metadata items. To ensure each item renders on its own line without inserting an empty paragraph, end each metadata line with two spaces (Markdown hard line break). Generated summaries should place each metadata line on a separate line and include two trailing spaces at the end of each metadata line.
- Keep the summary in English, neutral and encyclopedic in tone.

Song Content subsection (within Song Summary)

- Insert a `### Song Content 📝` subsection after Overview and before Composition.
- Analyze the song's themes, narrative arc, and emotional journey directly from the lyrics.
- For songs with significant lyrical density (40+ unique lines), include a **Format & Delivery** paragraph that:
  - Identifies the likely genre/delivery style (rap/hip-hop, ballad, upbeat pop) based on lyrical structure and density
  - Comments on rapid-fire lines, conversational language, internal monologues, or other stylistic markers
  - Explains how the chosen format suits the thematic content
- Follow with a **Narrative Structure** paragraph that:
  - Outlines the song's main themes and how they evolve through verses, chorus, and bridge
  - Traces the protagonist's emotional or philosophical journey
  - Notes key turning points or shifts in perspective
- Conclude with observations on resolution, message, or philosophical takeaway.
- Maintain analytical, encyclopedic tone; do not use first-person voice or casual commentary.

Lyrics section

- Header: `## 📖 Lyrics`
- Section headers must include a single emoji, e.g., `Verse 🎵`, `Pre-Chorus 🔔`, `Chorus ⭐`, `Bridge 🌉`, `Outro 🌙`.
- For Chinese lyrics, format each stanza as:

Chinese line (two trailing spaces)
**pinyin/jyutping** (two trailing spaces)
English translation (two trailing spaces)

**Important:** Each line in the lyrics section must end with exactly two spaces before the newline. This is Markdown syntax for a hard line break and ensures proper rendering. Apply this to all Chinese lines, romanization lines, and English translations.

- Use tone-mark pinyin for Mandarin and numeric jyutping for Cantonese.
- Bold romanization lines.
- Preserve original punctuation.
- For English-only lines inside lyrics, render the English line bold by itself.
- Instrumental sections: include only the section header and no body lines.

Auto-translation option

- If the user requests auto-generated English translations, produce a clear, line-by-line English translation directly under each romanization line. Preserve the original line breaks and punctuation; do not add commentary. When translating, prioritize literal meaning while keeping natural English phrasing.

Styling & emoji rules

- Use only standard Unicode emojis.
- One emoji per metadata line or header.
- Emojis allowed only in metadata labels and headers (not in paragraphs).
- Keep emoji usage consistent with examples in `_posts`.

Filenames & post metadata

- Filename format: `YYYY-MM-DD-Artist-Title.md` (use hyphens, ASCII where possible).
- Put the post into `_posts/`.
- `categories` should include `Lyrics` and the language (`Mandarin` or `Cantonese`).
- `tags` must be lowercase and hyphen-separated.

Filename example

- Follow the filename pattern exactly. Example for Hacken Lee's "紅日": `2025-12-27-hacken-lee-hong-jan.md` (use the generation date for the leading `YYYY-MM-DD`).

Examples & references

- Refer to existing posts in `_posts` for tone and formatting. Example: `/workspaces/Testing/_posts/2025-12-20-WangLeeHom-Mistake-at-the-Flower-Field.md` and `/workspaces/Testing/_posts/2025-12-24-JayChou-WontCry.md`.

Preview & verification

- To preview the site locally (dev server with live reload):

```bash
./tools/run.sh
```

- To build for production/test:

```bash
./tools/test.sh
```

Commit guidance

- Create a focused commit with the new Markdown file only.
- Use a descriptive commit message: `Add lyrics post: {Artist} - {Song Title}`.

Checklist before committing a generated post

- [ ] YAML front matter valid and complete
- [ ] `tags` include artist and release decade, lowercase
- [ ] Spotify iframe present if a Spotify link is given
- [ ] `style` helper block present
- [ ] Summary metadata lines include emojis and are English
- [ ] All lyric sections use the two-space rule and bold romanization lines
- [ ] Filename follows `YYYY-MM-DD-Artist-Title.md` and is in `_posts/`

Notes for Copilot usage

- Prefer conservative edits: do not paraphrase lyrics; use provided lyrics verbatim.
- When romanizing, preserve tone marks for pinyin and numeric tones for jyutping.
- If any required field is missing from user input, prompt for it before generating the file.

Contact

- If unsure about a stylistic choice, open an issue or ask the repository owner before committing.
