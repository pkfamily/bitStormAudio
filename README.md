# Bit Storm Audio

A Jekyll-powered blog dedicated to annotated song lyrics, translations, and music writing in Mandarin, Cantonese, and English.

## Overview

Bit Storm Audio features:

- Chinese and English lyric posts with romanization and translation
- Genre-focused music writing and cultural context
- Chord charts for select English-language songs
- A dark-mode blog layout built with the Chirpy theme

## Tech stack

- Jekyll
- Ruby / Bundler
- Chirpy theme
- GitHub Pages-ready static site generation

## Local development

```bash
./tools/run.sh            # Start the Jekyll dev server with live reload
./tools/run.sh -p         # Production preview mode
./tools/test.sh           # Full site build and validation check
bundle install            # Install Ruby dependencies
```

The local site is typically available at:

- http://127.0.0.1:4000

## Project structure

```text
.
├── _posts/                 # Published lyric/music posts
├── _tabs/                 # Top-level pages (About, Archives, Tags, etc.)
├── _data/                 # Site metadata and social/contact config
├── _plugins/              # Custom Jekyll hooks
├── assets/                # Images, avatars, and theme assets
├── tools/                 # Local build and generation scripts
├── _config.yml            # Site configuration
├── Gemfile                # Ruby dependencies
├── index.html             # Homepage entry point
├── README.md              # Project overview
├── LICENSE                # Project license
└── _site/                 # Generated static site output
```

## Writing posts

Most content work in this repository is creating a new file in `_posts/` using the project conventions described in the repo guidance files.

Useful references:

- `CLAUDE.md` — repository-specific authoring and build notes
- `copilot-instructions.md` — detailed post-formatting rules
- `tools/generate_post.py` — scaffolds new lyric posts

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
