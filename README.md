# AI-Powered SEO Content Production Research

This repository contains my research project about AI-powered SEO content production because it sits at the intersection of SEO, LLM visibility, content systems, and B2B SaaS buyer behavior.

The goal was not to dump links into folders. I wanted to build a source base strong enough to support a real playbook later, especially around AI visibility, entity understanding, commercial-intent content, and the shift from classic rankings to citation and recommendation systems.

## What I Collected

Inside [`research/`](research/) I organized the project into:

- `research/sources.md` for the final list of 10 chosen experts, dates, links, and why each source matters
- `research/linkedin-posts/` for recent LinkedIn post notes organized by author
- `research/youtube-transcripts/` for transcript-first research files organized by video
- `research/other/` for workflow notes, troubleshooting notes, and supporting research context

The collection includes:

- 10 selected experts relevant to AI-powered SEO content production
- 8 YouTube transcript files pulled for longer-form source material
- 3 LinkedIn author files with recent posts and takeaways
- additional notes on source selection, technical workflow, repo organization, and troubleshooting

## Why These Experts

I did not want this to be built from the first recognizable SEO names in search results. The shortlist was narrowed toward people whose work feels genuinely useful for a future playbook, not just for surface-level commentary.

The people I prioritized usually had one or more of these traits:

- they actively test or ship ideas instead of only reposting industry opinions
- they connect AI search to real workflows, not only trend language
- they publish unusual or high-signal thinking on citations, entities, AI visibility, or B2B SaaS search behavior
- they seem capable of supporting a practical playbook later, not just a list of hot takes

Some of the strongest examples in the final set are:

- Dan Petrovic for mechanistic thinking about grounding, snippets, and selection
- Steve Toth for buyer-journey compression, deal-breaker content, and comparison strategy
- Jason Barnard for entity understanding and AI recommendation logic
- Helene Jelenc for B2B SaaS AI visibility research with direct commercial relevance
- Lily Ray and Marie Haynes for quality, trust, and anti-hype guardrails

## Technical Workflow

This project also pushed me into more technical collection work than a normal note-taking task.

I used:

- `Python`
- `youtube-transcript-api`
- `Cursor IDE`
- `Git` and `GitHub`
- `WSL`
- `Claude Code` and `Codex`

The transcript workflow is documented in code through [`get_transcript.py`](get_transcript.py), which I used to fetch YouTube transcripts and save them into the repo structure. The supporting notes in `research/other/` also document the setup and troubleshooting work behind the collection process.

One part of that workflow became a real debugging problem: `Claude Code` would launch from `WSL`, but `/init` failed when I tried to use my own `SumoPod` model configuration. I kept that note in the repo because it shows that part of the assignment was not just collecting sources, but also dealing honestly with provider compatibility, environment variables, and tool-integration issues.

## Why The Material Is Playbook-Worthy

This research set feels usable for a real playbook later because it covers more than one layer of the topic:

- recent LinkedIn posts for fresh observations and framing
- long-form YouTube transcripts for deeper reasoning and process detail
- practitioner notes on citations, entity SEO, AI search measurement, and B2B SaaS buyer behavior
- my own synthesis inside the files so the repo is not just raw source storage

The strongest recurring themes so far are:

- AI visibility is not the same thing as traditional ranking
- recommendation systems reward trust, clarity, and entity understanding
- comparison content, deal-breaker content, and multi-format presence matter more in AI-assisted buying journeys
- raw traffic thinking is weaker than source selection, citation, and recommendation thinking

## Quick Navigation

- [`research/sources.md`](research/sources.md)
- [`research/linkedin-posts/`](research/linkedin-posts/)
- [`research/youtube-transcripts/`](research/youtube-transcripts/)
- [`research/other/`](research/other/)

## Repo Workflow

I committed and pushed throughout the project instead of waiting for one final dump. That mattered because I was still collecting, troubleshooting, reorganizing, and refining the research structure while learning the tools.
