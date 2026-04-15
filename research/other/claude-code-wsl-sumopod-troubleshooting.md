# Claude Code + WSL + SumoPod Troubleshooting Example

Another useful technical issue I worked through involved trying to use `Claude Code` inside `Cursor IDE` through `WSL`, while preferring my own `SumoPod` API key instead of the direct Claude sidebar login flow.

## Environment Setup Completed First

- upgraded `WSL` to version `2`
- installed `Node.js` and `Claude Code` inside `WSL`
- confirmed that the `claude` CLI launches from the `WSL` terminal
- exported custom environment variables inside the `WSL` shell:
  - `ANTHROPIC_BASE_URL=https://ai.sumopod.com`
  - `ANTHROPIC_API_KEY=MY_SUMOPOD_API_KEY`
  - `ANTHROPIC_MODEL=claude-sonnet-4-6`
- checked the `SumoPod` dashboard to confirm that `claude-sonnet-4-6` was listed as available

The CLI itself would open successfully, which meant the installation and base command path were not the main problem.

## Exact Failure Point

The actual failure appeared only when I tried to start the Claude Code workflow with:

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

That made the issue more technical than a simple typo or missing installation step, because:

- the `claude` command itself was already available
- the environment variables were already exported in `WSL`
- the model name matched what was shown in the `SumoPod` dashboard
- the failure happened at runtime when Claude Code tried to initialize a session

## Technical Hypotheses I Had To Investigate

At that point, the debugging questions became more specific:

- whether `Claude Code` actually supports overriding its provider through `ANTHROPIC_BASE_URL`, or whether it expects Anthropic's own endpoint behavior more strictly than a normal SDK client would
- whether `SumoPod` exposes an Anthropic-native API surface or only an OpenAI-compatible format, because Claude Code may expect Anthropic-specific request and response behavior
- whether the endpoint needs a more specific path than just `https://ai.sumopod.com`
- whether the backend supports the exact `/v1/messages` format Claude Code expects during `/init`
- whether the model name is listed in the dashboard but still unavailable to this specific API route or account scope
- whether Claude Code reads these environment variables correctly inside the `Cursor` + `WSL` context, or whether the subprocess environment differs from the shell session where I exported them

## Why This Was A Real Debugging Issue

I think this is worth documenting because it shows a more technical kind of troubleshooting than a basic install error.

The hard part was not getting the CLI to launch. The harder part was diagnosing a compatibility problem between:

- `Cursor IDE`
- `WSL`
- `Claude Code`
- custom `ANTHROPIC_*` environment variables
- a third-party provider endpoint instead of the default Claude login flow

In other words, the setup looked correct at the shell level, but the actual application workflow still failed at model initialization. That made it a useful example of API-provider debugging, environment verification, and tool-integration troubleshooting rather than just a one-step installation problem.
