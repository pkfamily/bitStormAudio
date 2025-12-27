Post generator script

This repository includes `tools/generate_post.py`, a small helper to create Jekyll lyric posts with the correct PST timestamp and required front matter.

Quick examples

Interactive / typical usage (arguments required):

```bash
python3 tools/generate_post.py \
  --artist-ch "李克勤" --artist-en "Hacken Lee" \
  --title-ch "紅日" --title-en "Red Sun" \
  --language cantonese --release-year 1992 \
  --lyrics-file path/to/lyrics.md \
  --spotify "https://open.spotify.com/track/..." \
  --image "https://example.com/image.jpg"
```

What it does
- Writes a new file to `_posts/YYYY-MM-DD-artist-title.md` where the leading date and `date:` front-matter timestamp are the current time in the America/Los_Angeles timezone (PST/PDT). The timestamp format is `YYYY-MM-DD HH:MM:SS -0800`.
- Generates YAML front matter following the project's conventions.
- Includes the Spotify iframe (if provided) and the style helper block.
- Appends the lyrics file contents to the `## 📖 Lyrics` section if `--lyrics-file` is provided; otherwise a minimal placeholder is inserted.

Notes
- The script does not auto-translate lyrics. If you need line-by-line translations, provide them in a pre-formatted lyrics file to `--lyrics-file`.
- The script requires Python 3.9+ for `zoneinfo`.
