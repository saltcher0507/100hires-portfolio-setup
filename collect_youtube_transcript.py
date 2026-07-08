from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi


VIDEO_ID = "YYZUVbMbln8"
VIDEO_TITLE = "Signal-Based Outbound"
VIDEO_URL = f"https://www.youtube.com/watch?v={VIDEO_ID}"
OUTPUT_FILE = Path("research/youtube-transcripts/florin-tatulea-signal-based-outbound.md")


api = YouTubeTranscriptApi()
transcript = api.fetch(VIDEO_ID)
text = "\n".join(snippet.text for snippet in transcript)

OUTPUT_FILE.write_text(
    f"# {VIDEO_TITLE}\n\n"
    f"- Expert: Florin Tatulea\n"
    f"- Channel: 30 Minutes to President's Club\n"
    f"- Source: {VIDEO_URL}\n"
    f"- Transcript type: YouTube captions\n\n"
    f"## Why This Video Was Selected\n\n"
    f"This video is relevant to Cold Outreach Pipeline for B2B SaaS because it focuses on signal-based outbound, "
    f"which helps identify better prospecting triggers and create more relevant outreach messages.\n\n"
    f"## Transcript\n\n"
    f"{text}\n",
    encoding="utf-8",
)

print(f"Saved transcript to {OUTPUT_FILE}")
