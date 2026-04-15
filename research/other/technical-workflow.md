# Technical Workflow I Used

This project was not only manual note-taking. It also included transcript collection, repo organization, troubleshooting, and some setup work to make the tools usable in practice.

## Main Tools

- `Cursor IDE` as the working environment
- `Git` and `GitHub` for version control
- `Python` for transcript collection
- `youtube-transcript-api` for pulling YouTube transcript data
- `WSL` for terminal-based setup and custom model configuration
- `Claude Code` and `Codex` for collection support, troubleshooting, and repo work

## Transcript Collection

For YouTube source collection, I used a small Python script:

- `get_transcript.py`

The script takes a YouTube URL or video ID, extracts the transcript through `youtube-transcript-api`, clears broken proxy variables if needed, and saves the output into the repo.

That part matters because one of the assignment requirements was using APIs or technical tools to collect source material rather than only summarizing videos manually from memory.

## Environment And Troubleshooting Work

Part of the workflow was more technical than I originally expected:

- I used my own `SumoPod` API key
- I installed and used `WSL`
- I configured `ANTHROPIC_*` environment variables manually
- I tested model configuration with `claude-sonnet-4-6`
- I documented a failure case where `Claude Code` launched correctly but `/init` still failed

That issue was useful to keep in the repo because it showed a real debugging path involving provider compatibility, endpoint behavior, environment inheritance, and `Cursor` + `WSL` integration rather than a simple install mistake.

## Why I Kept These Notes

I wanted the repository to show not only what I collected, but also how I collected it and what technical problems came up along the way.

For a research assignment like this, I think that matters because the final folders look simple, but getting to a clean structure still involved tool setup, transcript extraction, file organization, and honest documentation when something worked imperfectly.
