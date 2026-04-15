from youtube_transcript_api import YouTubeTranscriptApi
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import os


def extract_video_id(value):
    if "youtube.com" in value or "youtu.be" in value:
        parsed = urlparse(value)
        if parsed.netloc == "youtu.be":
            return parsed.path.lstrip("/")
        return parse_qs(parsed.query).get("v", [""])[0]
    return value


def clear_broken_proxy_settings():
    # Some local terminals inject a dead proxy like 127.0.0.1:9, which breaks requests.
    for key in [
        "HTTP_PROXY",
        "HTTPS_PROXY",
        "ALL_PROXY",
        "http_proxy",
        "https_proxy",
        "all_proxy",
    ]:
        os.environ.pop(key, None)


def main():
    if len(sys.argv) != 3:
        print("Usage: python get_transcript.py <youtube_url_or_video_id> <output_file>")
        sys.exit(1)

    video_input = sys.argv[1]
    output_file = Path(sys.argv[2])
    video_id = extract_video_id(video_input)

    if not video_id:
        print("Could not find a valid YouTube video ID.")
        sys.exit(1)

    clear_broken_proxy_settings()
    if output_file.parent.exists() and not output_file.parent.is_dir():
        print(
            f"Cannot save transcript because '{output_file.parent}' is a file, not a folder."
        )
        print(
            "Delete or rename that file in Cursor, then create a folder with the same name."
        )
        sys.exit(1)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    print(f"Fetching transcript for video: {video_id}")

    try:
        ytt_api = YouTubeTranscriptApi()
        fetched = ytt_api.fetch(video_id)
    except Exception as exc:
        print(f"Transcript fetch failed: {exc}")
        sys.exit(1)

    full_text = " ".join(entry.text for entry in fetched)

    with output_file.open("w", encoding="utf-8") as f:
        f.write("# Transcript\n\n")
        f.write(full_text)

    print(f"Done! Saved to {output_file}")


if __name__ == "__main__":
    main()
