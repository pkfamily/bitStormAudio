#!/usr/bin/env python3
"""
Generate a Jekyll lyric post with PST timestamp and required front matter.

Usage examples:
  python tools/generate_post.py --artist-ch "李克勤" --artist-en "Hacken Lee" \
    --title-ch "紅日" --title-en "Red Sun" --language cantonese --release-year 1992 \
    --lyrics-file path/to/lyrics.md --spotify "https://open.spotify.com/..." --image "https://..."

If `--lyrics-file` is provided the file contents are appended to the Lyrics section as-is.
"""

import argparse
import re
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path


def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def get_current_pst_timestamp():
    dt = datetime.now(ZoneInfo("America/Los_Angeles"))
    return dt.strftime("%Y-%m-%d %H:%M:%S %z")


def get_date_prefix():
    dt = datetime.now(ZoneInfo("America/Los_Angeles"))
    return dt.strftime("%Y-%m-%d")


def build_front_matter(args, date_ts):
    language_cap = "Cantonese" if args.language.lower().startswith("c") else "Mandarin"
    tag_lang = "cantonese" if language_cap == "Cantonese" else "mandarin"
    tag_roman = "jyutping" if language_cap == "Cantonese" else "pinyin"
    tag_pop = "cantopop" if language_cap == "Cantonese" else "c-pop"
    artist_tag = slugify(args.artist_en or args.artist_ch)
    decade = f"{int(int(args.release_year) // 10) * 10}s"

    fm = ["---"]
    title = f"{args.artist_ch} {args.artist_en} - {args.title_ch} ({args.title_en}) Lyrics"
    fm.append(f'title: {title!r}')
    fm.append(f'date: {date_ts}')
    fm.append("categories:")
    fm.append("  - Lyrics")
    fm.append(f"  - {language_cap}")
    fm.append("tags:")
    fm.append("  - chinese")
    fm.append(f"  - {tag_lang}")
    fm.append(f"  - {tag_roman}")
    fm.append("  - song lyrics")
    fm.append(f"  - {tag_pop}")
    fm.append(f"  - {artist_tag}")
    fm.append(f"  - {decade}")
    fm.append("image:")
    fm.append(f'  path: "{args.image or ""}"')
    fm.append("---\n")
    return "\n".join(fm)


def build_spotify_iframe(spotify_url: str) -> str:
    if not spotify_url:
        return ""
    # convert to embed if possible (assumes provided spotify track url or embed url)
    src = spotify_url
    if "open.spotify.com" in spotify_url and "embed" not in spotify_url:
        src = spotify_url.replace("/track/", "/embed/track/")
    iframe = (
        f'<iframe data-testid="embed-iframe" style="border-radius:12px" '
        f'src="{src}" width="100%" height="152" frameBorder="0" '
        'allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>\n\n'
    )
    return iframe


def build_summary(args) -> str:
    # Minimal summary block following site style
    # Metadata lines should end with two spaces to force a Markdown hard line break
    metadata = []
    metadata.append(f"**Title:** {args.title_ch} ({args.title_en}) 🎵")
    metadata.append(f"**Artist:** {args.artist_ch} {args.artist_en} 🎤")
    metadata.append(f"**Album:** {args.album or 'Single / Album (original release)'} 💿")
    metadata.append(f"**Release Year:** {args.release_year} 📅")
    metadata.append(f"**Songwriters:** {args.songwriters or '(credited songwriters)'} ✍️")
    metadata.append(f"**Genre:** {args.genre or ('Cantopop' if args.language.lower().startswith('c') else 'C-pop')} 🎶")

    # append two trailing spaces to metadata lines to create hard line breaks when rendered
    metadata = [m + "  " for m in metadata]

    # subsections and their paragraphs (each subsection starts on its own line)
    subsections = []
    subsections.append("### Overview ✨")
    subsections.append(args.overview or "Put an English overview of the song here.")
    subsections.append("### Composition 🎼")
    subsections.append(args.composition or "Put a short composition note here.")
    subsections.append("### Release & Album Context 📀")
    subsections.append(args.release_context or "Release context notes here.")
    subsections.append("### Popularity & Reception 🌟")
    subsections.append(args.reception or "Reception notes here.")
    subsections.append("### Legacy 🕊️")
    subsections.append(args.legacy or "Legacy notes here.")

    # Join metadata with single newlines (they contain trailing two spaces), then put a blank line before subsections
    return "\n".join(["## 🎵 Song Summary"] + metadata) + "\n\n" + "\n".join(subsections) + "\n\n"


def build_style_block():
    return "<style>\n r { color: Red }\n o { color: Orange }\n g { color: Green }\n</style>\n\n"


def build_lyrics_section(lyrics_text: str) -> str:
    out = "## 📖 Lyrics\n\n"
    if lyrics_text:
        out += lyrics_text.strip() + "\n"
    else:
        out += "### Verse 1 🎵\n\nChinese line  \n**jyutping**  \nEnglish translation\n"
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--artist-ch", required=True)
    p.add_argument("--artist-en", required=True)
    p.add_argument("--title-ch", required=True)
    p.add_argument("--title-en", required=True)
    p.add_argument("--language", choices=["cantonese", "mandarin"], default="cantonese")
    p.add_argument("--release-year", required=True)
    p.add_argument("--spotify")
    p.add_argument("--image")
    p.add_argument("--lyrics-file")
    p.add_argument("--album")
    p.add_argument("--songwriters")
    p.add_argument("--genre")
    p.add_argument("--overview")
    p.add_argument("--composition")
    p.add_argument("--release-context")
    p.add_argument("--reception")
    p.add_argument("--legacy")

    args = p.parse_args()

    date_ts = get_current_pst_timestamp()
    date_prefix = get_date_prefix()

    slug = slugify(f"{args.artist_en} {args.title_en}")
    filename = f"{date_prefix}-{slug}.md"
    out_path = Path("_posts") / filename

    fm = build_front_matter(args, date_ts)
    iframe = build_spotify_iframe(args.spotify)
    style = build_style_block()
    summary = build_summary(args)

    lyrics_text = ""
    if args.lyrics_file:
        try:
            lyrics_text = Path(args.lyrics_file).read_text(encoding="utf-8")
        except Exception as e:
            print(f"Warning: could not read lyrics file: {e}")

    lyrics_section = build_lyrics_section(lyrics_text)

    content = fm + iframe + style + summary + "---\n" + lyrics_section

    out_path.write_text(content, encoding="utf-8")
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
