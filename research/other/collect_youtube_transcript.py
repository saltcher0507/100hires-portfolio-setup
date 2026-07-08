from pathlib import Path
from urllib.parse import urlparse, parse_qs

from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url: str):
    """Extract YouTube video ID from different URL formats."""

    parsed = urlparse(url)

    if parsed.hostname in ("youtu.be", "www.youtu.be"):
        return parsed.path.lstrip("/")

    if parsed.hostname in (
        "youtube.com",
        "www.youtube.com",
        "m.youtube.com",
    ):
        if parsed.path == "/watch":
            return parse_qs(parsed.query).get("v", [None])[0]

        if parsed.path.startswith("/shorts/"):
            return parsed.path.split("/")[2]

        if parsed.path.startswith("/embed/"):
            return parsed.path.split("/")[2]

    return None


youtube_url = input("Enter YouTube URL: ").strip()
expert_name = input("Enter expert name: ").strip()
output_filename = input("Enter output filename (without .md): ").strip()

video_id = extract_video_id(youtube_url)

if not video_id:
    raise ValueError("Invalid YouTube URL.")

output_dir = Path("research/youtube-transcripts")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / f"{output_filename}.md"

api = YouTubeTranscriptApi()
transcript = api.fetch(video_id)

text = "\n".join(snippet.text for snippet in transcript)

title = output_filename.replace("-", " ").title()

markdown = f"""# {title}

**Expert:** {expert_name}

**Source:**
{youtube_url}

## Transcript

{text}
"""

output_file.write_text(markdown, encoding="utf-8")

print(f"\nTranscript saved to:\n{output_file}")