from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi


VIDEO_ID = "JX1UNIJwcCY"
VIDEO_TITLE = "Cold Email Masterclass: Everything You Need To Book Meetings in 2026"
VIDEO_URL = f"https://www.youtube.com/watch?v={VIDEO_ID}"
OUTPUT_FILE = Path("research/youtube-transcripts/cold-email-masterclass-book-meetings-2026.md")


api = YouTubeTranscriptApi()
transcript = api.fetch(VIDEO_ID)
text = "\n".join(snippet.text for snippet in transcript)

OUTPUT_FILE.write_text(
    f"# {VIDEO_TITLE}\n\n"
    f"- Expert: Armand Farrokh\n"
    f"- Channel: 30 Minutes to President's Club\n"
    f"- Source: {VIDEO_URL}\n"
    f"- Transcript type: YouTube captions\n\n"
    f"## Why This Video Is Relevant\n\n"
    f"This video is directly related to cold outreach pipeline for B2B SaaS because it focuses on cold email, "
    f"booking meetings, and outbound prospecting messages.\n\n"
    f"## Transcript\n\n"
    f"{text}\n",
    encoding="utf-8",
)

print(f"Saved transcript to {OUTPUT_FILE}")
