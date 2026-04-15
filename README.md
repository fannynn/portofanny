# Portfolio Project Setup Documentation

## Hello! I'm Fanny ;)

This repository was created as part of a portfolio project assignment to demonstrate the ability to follow technical instructions, troubleshoot setup issues, and document the workflow clearly and professionally.

## Tools Installed

The following tools and platforms were successfully installed and configured:

- Cursor IDE
- Claude Code extension
- Codex extension
- Git
- GitHub repository

## Steps Completed

1. Installed Cursor IDE successfully.
2. Opened Cursor IDE.
3. Initially got confused while installing Claude Code because I mistakenly tried using the browser installation method with PowerShell.
4. Encountered an **"Access is denied"** error when running the `mshta` command in PowerShell.
5. Researched the correct method and realized the proper way was through Cursor Extensions.
6. Opened Extensions using **Ctrl + Shift + X**.
7. Searched for **Claude Code**.
8. Installed and logged into Claude Code successfully.
9. Installed the **Codex** extension.
10. Initially did not know how to log into Codex.
11. Searched for a login tutorial on YouTube and found a helpful guide:  
    [Codex Login Tutorial](https://www.youtube.com/watch?v=1wP97Rd62cg&t=346s)
12. Followed the tutorial by clicking the Codex extension and selecting **Open Codex Sidebar**.
13. This redirected me to the login page, and I successfully logged in.
14. Created a public GitHub repository.
15. Attempted to open or clone the repository in Cursor but encountered another issue because nothing appeared.
16. Investigated the issue through Google search.
17. Discovered that Git was not installed on my system.
18. Installed Git.
19. Reopened Cursor and used **Ctrl + Shift + P**.
20. The **Clone with GitHub** option appeared successfully.
21. Opened the repository in Cursor IDE successfully.
22. Created the README file.
23. Prepared for commit and push to GitHub.

## Issues Encountered and Solutions

### Issue 1: Claude Code Installation Confusion

I initially used the wrong installation approach by trying to run a browser-based method through PowerShell. This caused an **"Access is denied"** error when running the `mshta` command.

The issue was resolved by using the correct method: installing Claude Code through **Cursor Extensions** (`Ctrl + Shift + X`).

### Issue 2: Codex Login Confusion

At first, I was unsure how to log into Codex after installation.

I solved this by searching for a tutorial on YouTube and following the steps to open **Open Codex Sidebar**, which redirected me to the login page and allowed successful sign-in.

### Issue 3: Unable to Open GitHub Repository

When I tried to clone the repository in Cursor, nothing appeared, which blocked progress.

After researching online, I discovered that Git was not installed on my system. Once Git was installed, the **Clone with GitHub** option became available through **Ctrl + Shift + P**, and the issue was resolved.

## Reflection

This setup process strengthened my confidence in troubleshooting technical problems independently. I used Google and YouTube strategically to find accurate solutions, adapted quickly to unfamiliar tools and workflows, and stayed persistent through each issue until the environment was fully configured. The experience reflects both technical initiative and practical problem-solving skills that I can apply to future development tasks.

---

## Next Phase: AI-Powered SEO Content Production Research

After completing the setup process, I continued this repository as a research project focused on **AI-powered SEO content production**. My goal was not only to collect sources, but to build a research base strong enough to support a real playbook later.

## What I Collected

Inside `/research`, I organized the project into:

- `research/sources.md` for the ranked source list and research direction
- `research/linkedin-posts/` for recent LinkedIn post notes from selected experts
- `research/youtube-transcripts/` for video transcripts organized by video
- `research/other/` for extra supporting research notes split into separate topic files

So far, I collected:

- a ranked expert/source list in `research/sources.md`
- LinkedIn research notes for Lily Ray, Jason Barnard, and Helene Jelenc
- YouTube transcript files for Dan Petrovic, Steve Toth, Metehan Yeşilyurt, Kevin Indig, Marie Haynes, Szymon Słowik, Aleyda Solis, and Helene Jelenc
- personal notes attached to transcript files so I can connect the raw source material with my own research takeaways

## Why I Chose These Experts

I did not want to just use the first generic SEO names that appeared in search results. I wanted experts with stronger voices, more specific experience, and ideas that felt genuinely useful for **AI-powered SEO content production**.

To choose them, I used:

- the Wellows article on top AI SEO agencies: https://wellows.com/blog/top-ai-seo-agencies/
- LinkedIn recommendations
- my discussions with Claude to brainstorm and narrow down relevant experts
- additional research into the experts' companies, roles, LinkedIn content, and YouTube material

From there, I narrowed the list to experts whose work seemed:

- actually practiced, not just discussed theoretically
- relevant to AI visibility, AI search, entity SEO, content systems, or SaaS-focused SEO
- strong enough to help me later build a practical playbook instead of a surface-level summary

Some of the companies and contexts that helped me judge their relevance were:

- `DEJAN AI`, which made Dan Petrovic stand out for deeper AI and search experimentation
- `SEO Notebook / Notebook Agency`, which made Steve Toth stand out for systems and execution
- `takaoto.pro`, which made Szymon Słowik stand out for more technical and strategic SEO thinking
- `metehan.ai / AppSamurai`, which made Metehan Yeşilyurt stand out for AI-native experimentation
- `Growth Memo`, which made Kevin Indig stand out for strategic and research-driven analysis
- `Amsive`, which made Lily Ray stand out for quality, trust, and AI search analysis
- `MHC Digital`, which made Marie Haynes stand out for search quality and visibility diagnosis
- `Kalicube`, which made Jason Barnard stand out for brand/entity understanding
- `Orainti`, which made Aleyda Solis stand out for practical SEO workflows
- `Flow Agency`, which made Helene Jelenc stand out especially for B2B SaaS and AI visibility testing

## Technical Tools and API Workflow

This project also pushed me beyond basic documentation work and into using more technical tools directly.

I used:

- `Python` for transcript collection
- `youtube-transcript-api` to pull YouTube transcripts
- `Cursor IDE` as the main working environment
- `Git` and `GitHub` for version control
- `Node.js` and additional terminal setup to support the project workflow

I also worked with a more custom AI setup:

- I used my own `SumoPod` API key
- because that setup was more manual, I installed `WSL`
- I used the `WSL` terminal inside Cursor IDE
- I configured SumoPod-related environment variables manually there
- I installed Claude Code manually through the terminal
- I tested the model configuration manually as `claude-sonnet-4-6`

One useful troubleshooting case in this setup was that `Claude Code` would open from `WSL`, but `/init` still failed with a model-access error even after I selected `claude-sonnet-4-6` again through `/model`. That pushed me to think beyond basic installation and look at possible causes such as API compatibility, endpoint format, environment-variable support, and `Cursor` + `WSL` integration behavior.

This part of the project shows that I was not only collecting notes manually, but also learning how to work with APIs, terminal-based setup, and AI tooling in a more technical way, including cases where the problem was not fully solved yet and had to be documented honestly as an active debugging issue.

## Why This Material Can Support a Real Playbook Later

I specifically looked for sources that could support a future playbook, not just fill a folder.

The material is useful for that because it includes:

- expert perspectives from practitioners with strong reputations and specific niches
- LinkedIn posts for recent observations and framing
- YouTube transcripts for longer explanations, tests, and strategic detail
- my own notes on why each source matters and what ideas may be useful later

That combination gives me a stronger base for identifying patterns around:

- AI visibility vs. traditional rankings
- content diversification across formats
- brand/entity signals
- AI-native SEO workflows
- what kinds of content systems might still perform well in an AI-search environment

## Project Workflow

I also committed and pushed my work regularly throughout the process instead of leaving everything for one giant commit at the end. That helped me keep the repository organized while I was still learning, testing, troubleshooting, and refining the research structure as I went.
