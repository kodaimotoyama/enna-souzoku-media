# Repository Workflow Template

Use this pattern when the repository already contains article automation scripts.

## Discovery

1. Find title generation, article generation, and publishing-related files.
2. Find environment variables and model configuration points.
3. Find workflow files that schedule or dispatch generation jobs.

## Execution Order

1. Confirm the article brief with the user.
2. Update configuration or prompts only where required.
3. Run title generation first if article inputs depend on it.
4. Run article generation second.
5. Validate outputs and generated files.
6. If GitHub Actions is part of the system, update action versions and model env vars when needed.

## Failure Handling

- If a model returns `not_found_error`, treat it as a model availability issue, not an API key issue.
- If authentication fails, stop and report the exact authentication failure.
- If a workflow step fails in CI, inspect the exact step before changing unrelated files.

## Current Repository Notes

- `generate_titles.py` creates title and heading source data.
- `generate_articles.py` turns source rows into full article HTML.
- `.github/workflows/generate-titles-hourly.yml` schedules and runs the automation.
- `CLAUDE_MODEL` should be configurable in the workflow and respected by the Python generator.

