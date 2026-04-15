# Portfolio Project Setup Documentation

This repository began as a portfolio project assignment focused on setup, troubleshooting, and documentation. As the work developed, it expanded into a structured research repository on `AI-powered SEO content production`, with a specific focus on AI visibility, entity understanding, recommendation systems, and B2B SaaS search behavior.

This README reflects both parts of that process: the original technical setup work and the later research update built on top of it. The goal was not to collect a large volume of generic SEO material, but to assemble a smaller, higher-signal set of practitioner sources strong enough to support a real playbook later.

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

This setup process strengthened my confidence in troubleshooting technical problems independently. I used Google and YouTube strategically to find accurate solutions, adapted quickly to unfamiliar tools and workflows, and stayed persistent through each issue until the environment was fully configured.

The same problem-solving approach carried into the next phase of the project. Once the environment was working, the repository evolved from a setup exercise into a research project examining how SEO content production changes when discovery is shaped by LLMs, AI Overviews, recommendation systems, and entity-level understanding.

---

## Research Update: AI-Powered SEO Content Production

After the setup was complete, I used the repo to collect research for my chosen topic : `AI-powered SEO content production`.

The collection was designed around the assignment requirements: identify 10 strong experts, collect recent content through technical workflows, organize the material clearly in the repository, and document why the final set is worth using.

I did not want this repository to become a generic folder of SEO links. The goal was to build a source base that could support a future playbook, especially around:

- AI visibility instead of only traditional rankings
- entity understanding and recommendation logic
- commercial-intent content for B2B SaaS
- how AI search changes what content is worth producing

## What I Collected

Inside [`research/`](research/) I organized the material into:

- [`research/sources.md`](research/sources.md) as the final source index with 10 selected experts, links, dates, and reasons for choosing them
- [`research/linkedin-posts/`](research/linkedin-posts/) for recent LinkedIn post notes collected manually and organized by author
- [`research/youtube-transcripts/`](research/youtube-transcripts/) for long-form transcript-based research collected through API-based workflow
- [`research/other/`](research/other/) for workflow notes, troubleshooting context, and supporting documentation

The collection currently includes:

- 10 selected experts relevant to AI-powered SEO content production
- 8 YouTube transcript files for deeper long-form insights
- 3 LinkedIn post collections for fresher industry observations
- supporting notes on source selection, repo organization, and technical workflow

## Repository Structure

The repository was organized to make the research usable, not just stored:

- `research/sources.md` works as the main decision layer, showing who was selected, when the source was published, where it came from, and why it matters
- `research/linkedin-posts/` holds short-form signals, recent opinions, and tactical observations by author
- `research/youtube-transcripts/` holds longer-form material with enough depth to extract frameworks, workflows, and reasoning
- `research/other/` captures process documentation, troubleshooting, and supporting context so the repo shows how the research was built, not only the final output

## Why I Chose These Experts

The shortlist was not based on who is most famous or most visible in surface-level SEO conversations. I tried to choose people whose work could actually support a practical playbook later.

The strongest picks usually did at least one of these things:

- published original frameworks, tests, or operational thinking
- connected AI search to real buyer journeys instead of trend commentary
- offered a niche angle like entity SEO, AI visibility measurement, grounding, or recommendation logic
- brought enough depth to be useful beyond hot takes

Some of the strongest examples in the final set are:

- Dan Petrovic for mechanistic thinking about grounding, snippets, citation logic, and selection
- Steve Toth for buyer-journey compression, alternatives content, and deal-breaker content strategy
- Jason Barnard for entity understanding and how AI systems interpret brand credibility
- Helene Jelenc for B2B SaaS AI visibility research with direct commercial relevance
- Lily Ray and Marie Haynes for quality, trust, and anti-hype guardrails

This mix made the research set feel more useful and less generic. Instead of collecting broad SEO commentary, I focused on experts who help explain how AI systems choose, cite, recommend, and summarize content.

## Why This Repository Feels More Niche Than Generic

What makes this repository more specific is not just the topic. It is the combination of sources and the lens used to evaluate them.

The recurring themes across the materials are:

- AI visibility is different from traditional ranking
- recommendation systems reward trust, clarity, and strong entity signals
- comparison pages, alternative pages, and deal-breaker content matter more in AI-assisted buying journeys
- measurement is becoming harder, so source selection and citation logic matter more
- not all SEO advice survives the shift to AI-driven discovery

That is why the expert list in [`research/sources.md`](research/sources.md) is intentionally selective. I was looking for people whose ideas could later turn into a real workflow, not just a trend summary.

## Why The Material Is Strong Enough For A Real Playbook

This repository is built to support future strategic use, not just to complete the collection task.

The material is strong enough for a later playbook because it combines:

- recent short-form content for current observations and shifts in the field
- long-form transcripts for frameworks, reasoning, and process detail
- a balanced expert mix across AI visibility, entity SEO, measurement, content systems, and B2B SaaS search behavior
- annotations and synthesis that explain why each source matters instead of treating all sources as equally useful

The result is a smaller but more intentional source base. That matters for this topic, because 10 high-signal experts with distinct strengths are more useful than a much larger list of repetitive SEO commentary.

## Technical Workflow Behind The Research

This project also became more technical than a normal note-taking task.

I used:

- `Python`
- `youtube-transcript-api`
- `Cursor IDE`
- `Git` and `GitHub`
- `WSL`
- `Claude Code` and `Codex`

The transcript collection workflow is reflected in [`get_transcript.py`](get_transcript.py), which I used to fetch YouTube transcripts and save them into the repo. LinkedIn material was collected and organized manually by author. I also kept supporting notes in `research/other/` because the research process included setup friction, tool debugging, and workflow decisions, not just content collection.

This part of the project demonstrates more than topic research alone. It also shows the ability to work with APIs, troubleshoot tooling, manage files systematically, and turn raw source collection into a structured repository.

## Repo Workflow

I committed and pushed throughout the project instead of waiting until the end for one large upload. That mattered because the repository kept changing as I collected sources, pulled transcripts, refined the shortlist, reorganized folders, and improved the documentation.

## Quick Navigation

- [`research/sources.md`](research/sources.md)
- [`research/linkedin-posts/`](research/linkedin-posts/)
- [`research/youtube-transcripts/`](research/youtube-transcripts/)
- [`research/other/`](research/other/)
