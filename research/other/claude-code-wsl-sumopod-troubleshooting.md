# Claude Code + WSL + SumoPod Troubleshooting Example

Another technical issue I worked through came up while trying to run `Claude Code` inside `Cursor IDE` through `WSL`, using my own `SumoPod` API key instead of the standard Claude sidebar login flow.

## Environment Setup Completed First

- upgraded `WSL` to version `2`
- installed `Node.js` and `Claude Code` inside `WSL`
- confirmed that the `claude` CLI launches from the `WSL` terminal
- exported custom environment variables inside the `WSL` shell:
  - `ANTHROPIC_BASE_URL=https://ai.sumopod.com`
  - `ANTHROPIC_API_KEY=MY_SUMOPOD_API_KEY`
  - `ANTHROPIC_MODEL=claude-sonnet-4-6`
- checked the `SumoPod` dashboard to confirm that `claude-sonnet-4-6` was listed as available

The CLI itself opened successfully, so the main problem was clearly not basic installation or command availability.

## Exact Failure Point

The failure only showed up when I tried to start the Claude Code workflow with:

```bash
/init
```

The error returned was:

```text
There's an issue with the selected model (claude-sonnet-4-6).
It may not exist or you may not have access to it.
Run /model to pick a different model.
```

I then tested the obvious fallback path by running:

```bash
/model
```

and selecting the same model again, but `/init` still failed with the same message.

At that point, the issue looked more technical than a typo or a missed install step, because:

- the `claude` command itself was already available
- the environment variables were already exported in `WSL`
- the model name matched what was shown in the `SumoPod` dashboard
- the failure happened at runtime when Claude Code tried to initialize a session

## Technical Hypotheses I Investigated

The debugging path then became much more specific:

- `Claude Code` might not fully support provider overrides through `ANTHROPIC_BASE_URL`, even if a normal SDK client does
- `SumoPod` might expose only an OpenAI-compatible surface instead of the Anthropic-style behavior Claude Code expects
- the endpoint might require a more specific path than `https://ai.sumopod.com`
- the backend might not support the exact `/v1/messages` request and response format used during `/init`
- the model name might appear in the dashboard but still be unavailable for that route, account scope, or session type
- the environment variables might be available in the `WSL` shell but not inherited the same way by the `Cursor` + `WSL` Claude Code process

## Why This Was A Real Debugging Issue

This feels worth documenting because it shows a more technical category of troubleshooting than a basic install error.

Getting the CLI to launch was not the hard part. The harder part was diagnosing a compatibility problem across:

- `Cursor IDE`
- `WSL`
- `Claude Code`
- custom `ANTHROPIC_*` environment variables
- a third-party provider endpoint instead of the default Claude login flow

In other words, the setup looked correct at the shell level, but the real workflow still broke at model initialization. That made it a useful example of API-provider debugging, environment verification, and tool-integration troubleshooting rather than a simple one-step setup issue.
