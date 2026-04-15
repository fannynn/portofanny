# Claude Code + WSL + SumoPod Troubleshooting Example

Another useful technical issue I worked through involved trying to use `Claude Code` inside `Cursor IDE` through `WSL`, while preferring my own `SumoPod` API key instead of the direct Claude sidebar login flow.

## What I Completed First

- upgraded `WSL` to version `2`
- installed `Node.js` and `Claude Code` inside `WSL`
- confirmed that the `claude` CLI launches from the `WSL` terminal
- exported custom environment variables:
  - `ANTHROPIC_BASE_URL=https://ai.sumopod.com`
  - `ANTHROPIC_API_KEY=...`
  - `ANTHROPIC_MODEL=claude-sonnet-4-6`
- checked the `SumoPod` dashboard to confirm that `claude-sonnet-4-6` was listed as available

## Remaining Issue

The remaining issue was that `/init` in Claude Code still failed with a model-access error, even after selecting the same model again through `/model`.

That gave me a more realistic debugging problem to investigate, including questions such as:

- whether the endpoint was truly compatible with the API format `Claude Code` expects
- whether `Claude Code` supports this exact environment-variable setup
- whether the `SumoPod` endpoint supports the expected Anthropic-style `/v1/messages` flow
- whether there was a model naming, access, or protocol mismatch even though the model appeared in the dashboard
- whether running through `Cursor` + `WSL` introduced an extra integration issue

I think this is worth documenting because it shows that my work was not limited to straightforward installation. It also involved diagnosing compatibility problems between developer tools, terminal environments, and third-party API providers, even when the setup looked correct on the surface.
