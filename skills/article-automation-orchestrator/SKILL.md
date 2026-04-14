---
name: article-automation-orchestrator
description: Run or adapt an article automation workflow that collects requirements first, then generates title plans, article content, and publishing-ready outputs. Use when the user wants AI-assisted article production, workflow setup, batch article generation, or ongoing content automation in Codex or Claude Code.
---

# Article Automation Orchestrator

## Purpose

Use this skill to operate or adapt a long-form article generation workflow.

This skill is designed to work in both Codex and Claude Code because it relies on plain workflow instructions plus local project files, not product-specific APIs.

## First-Run Intake

On the first invocation in a thread, or whenever the article brief is still ambiguous, do not start generating immediately.

Collect and confirm these items first:

- theme or content domain
- target audience
- article goal
- desired article length
- output format
- batch size
- tone and style constraints
- factual or legal constraints
- CTA or conversion goal
- whether titles, outlines, full articles, or publishing files are needed

If the user gave only a vague request, ask a compact intake in Japanese by default. Use the template in `./references/intake-template.md`.

After the user answers, restate the agreed brief in one short block before making changes or running generation.

## Workflow

1. Read the confirmed brief and identify which stage is requested: planning, title generation, article generation, workflow editing, or publishing preparation.
2. Inspect the repository files that actually implement the automation before changing anything.
3. If generation scripts already exist, prefer updating or running them over rebuilding the flow from scratch.
4. If model or API configuration is involved, make the model configurable through environment variables.
5. Generate or update outputs in a reproducible way.
6. Validate syntax, file paths, and workflow assumptions.
7. Report what changed, what ran, and what still needs manual confirmation.

## Rules

- Default to Japanese when the repository and user context are Japanese.
- Treat article requirements as unstable until the intake is confirmed.
- If legal, medical, tax, or financial claims appear, prefer safer wording and surface review risk explicitly.
- Do not claim a key is invalid unless the API or provider returned an authentication-specific error.
- If a specific model is unavailable, try configured fallbacks before failing the run.
- Keep workflow edits minimal and reversible.

## Repository Adaptation

When this skill is used inside an existing project, inspect the current automation entrypoints first.

For this repository, start with:

- `generate_titles.py`
- `generate_articles.py`
- `.github/workflows/generate-titles-hourly.yml`

Use `./references/repo-workflow-template.md` as the default execution pattern.

## Output

Return:

- the confirmed brief
- what stage was executed
- changed files or commands run
- validation result
- remaining risks or follow-up

