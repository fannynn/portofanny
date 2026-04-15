# YouTube Transcript API Troubleshooting Example

One of the clearest examples of my technical troubleshooting in this project was the YouTube transcript workflow.

At first, I tried to install `youtube-transcript-api` inside `Git Bash`, but `pip` was not recognized there. To solve that, I switched terminals inside Cursor IDE and used `Command Prompt` / `PowerShell` instead. From there, I checked Python, installed the package properly, and verified that it was available.

I then created `get_transcript.py` in the repo and tested it from:

- `C:\Users\fanny\portofanny-2\portofanny`

When I first ran the script, it failed because the version of `youtube-transcript-api` I installed no longer supported the older `get_transcript` method I had been trying to use.

To fix that, I updated the script logic to use:

- `YouTubeTranscriptApi()`
- `.fetch(video_id)`
- `entry.text`

instead of the older pattern.

This showed me how to:

- switch between terminals depending on the tool
- work with Python packages from the terminal
- troubleshoot version differences in an API library
- test the script again after updating the code
- use the script to save transcript output directly into my research folder

That part of the workflow was especially useful because it moved the project from simple note-taking into actual API and terminal-based problem solving.
