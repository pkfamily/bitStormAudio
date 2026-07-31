# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A Jekyll static site (Chirpy theme, `chirpy-starter` layout) called "Bit Storm Audio" — a music blog of annotated song lyrics (Mandarin, Cantonese, English), with romanization (pinyin/jyutping), English translations, and occasionally chord charts. Almost all content work in this repo is: **add a new post to `_posts/`**.

Since Jekyll/RubyGems only exposes `_data`, `_layouts`, `_includes`, `_sass`, and `assets` from the theme gem, this repo vendors the rest of the required scaffolding (`_config.yml`, `_plugins`, `_tabs`, `index.html`) per the chirpy-starter convention — don't be surprised these exist with minimal content; they're copied from the theme, not authored here.

## Commands

```bash
./tools/run.sh            # bundle exec jekyll s -l  (dev server, live reload, http://127.0.0.1:4000)
./tools/run.sh -p         # same, but JEKYLL_ENV=production
./tools/test.sh           # clean rebuild to _site/ (JEKYLL_ENV=production) + htmlproofer link/HTML check
bundle install            # install Ruby deps (first-time / after Gemfile changes)
```

`tools/test.sh` is the closest thing to a CI check available locally — always run it before considering a post change done, since it validates against html-proofer (internal links, HTML validity), and future-dated posts are silently skipped in preview but will surface as build issues.

There is no JS/npm build in this repo (`.devcontainer/post-create.sh` only runs `npm i`/`npm run build` conditionally, guarded by `if [ -f package.json ]`, which does not exist here).

### Generating a post

`tools/generate_post.py` scaffolds a new Chinese-language lyrics post with correct PST-timestamped front matter:

```bash
python3 tools/generate_post.py \
  --artist-ch "李克勤" --artist-en "Hacken Lee" \
  --title-ch "紅日" --title-en "Red Sun" \
  --language cantonese --release-year 1992 \
  --lyrics-file path/to/lyrics.md \
  --spotify "https://open.spotify.com/track/..." \
  --image "https://example.com/image.jpg"
```

It writes `_posts/YYYY-MM-DD-{artist}-{title}.md` (date = current America/Los_Angeles time, requires Python 3.9+ for `zoneinfo`). It does not translate/romanize lyrics — pass a pre-formatted `--lyrics-file`, or write the post by hand following the conventions below. The script's own `build_summary()` section list (Overview/Composition/Release & Album Context/Popularity & Reception/Legacy) is a minimal subset — the full required section set for hand-authored posts is longer; see below.

## Post authoring conventions

The canonical, detailed spec lives in `copilot-instructions.md` (also duplicated as reusable prompt files at `.github/prompts/chinese-lyrics-post.prompt.md` and `.github/prompts/english-lyrics-chords.prompt.md`) — **read that file before generating a post**; the summary below hits only the load-bearing rules that are easy to get wrong.

- **Filename**: `_posts/YYYY-MM-DD-Artist-Title.md`, ASCII/hyphens. Leading date should match generation date; front-matter `date` must not be future-dated relative to local build time or the post is skipped.
- **Front matter**: `date: YYYY-MM-DD HH:MM:SS -0800` (PST, generation time — not the song's release date). `categories: [Lyrics, {Mandarin|Cantonese|English}]`. Tags are lowercase; must include the artist tag and a `{YYYY}s` decade tag. Use `song lyrics` (with a space) — not `song-lyrics` — since both normalize to the same archive slug and would collide. Check existing tags in `_posts/` before inventing a new one, to avoid duplicate tags that differ only in spacing/punctuation.
- **Style block**: every post includes the `<style> r{} o{} g{} </style>` color-helper block right after front matter (and any Spotify iframe).
- **Song Summary** (`## 🎵 Song Summary`): metadata lines (Title/Artist/Album/Release Year/Songwriters/Genre), each ending in exactly one emoji and a hard line break (two trailing spaces), then exactly these seven subsections in order: Overview, Composition, Song Content, Artistic Approach, Release & Context, Popularity & Reception, Legacy. English, encyclopedic tone, no first person.
- **Lyrics** (`## 📖 Lyrics`): section headers get one emoji, e.g. `### [主歌] / Verse 1 🎵`. For Chinese lyrics every line needs all three of: Chinese text, **bold** romanization (tone-mark pinyin for Mandarin, numeric jyutping for Cantonese), English translation — each line hard-broken with two trailing spaces. Stanzas separated by `---`. Instrumental sections get only the header, no body.
- **Chords (English posts)**: use phrase-level inline chord annotations, not raw monospaced blocks, when aesthetics matter. See `_posts/2026-04-12-eagles-desperado.md` for the current preferred pattern — a `.chord-sheet` CSS component keyed entirely to Chirpy theme variables (`var(--card-bg)`, `var(--main-border-color)`, `var(--text-color)`, `var(--text-muted-color)`, `var(--link-color)`), with `html[data-mode='dark']` overrides where needed. Never leave a hard-coded light background — this site defaults to dark mode (`theme_mode: dark` in `_config.yml`). Don't add empty lyric spans just to preserve chord timing; every displayed chord must stay attached to visible lyric text, including at line-wrap points.
- **Copyright**: if lyrics/chords appear to be copyrighted and the user hasn't said they have permission to publish, ask before generating the post.
- Do not paraphrase lyrics — use provided lyrics verbatim.

## Structure

- `_posts/` — all published content, one Markdown file per song.
- `_tabs/` — top-level pages (About, Archives, Categories, Tags) copied from the theme per chirpy-starter convention.
- `_data/contact.yml`, `_data/share.yml` — site data copied/customized from the theme.
- `_plugins/posts-lastmod-hook.rb` — sets `last_modified_at` from git history (`git log` on the post file) when a post has more than one commit.
- `assets/Avatar/`, `assets/Post-Main/` — avatar GIFs and post header images used by front matter `image.path`.
- `_config.yml` — site config (Chirpy theme import, `theme_mode: dark`, permalinks, `jekyll-archives` for tag/category pages). The `defaults` block sets `layout: post`, `comments: true`, `toc: true` for everything under `_posts`.
- `_site/` — build output, not source; ignore when reading/editing.
- `tools/` — repo-local scripts (`generate_post.py`, `run.sh`, `test.sh`), excluded from the Jekyll build via `_config.yml`'s `exclude:` list.
