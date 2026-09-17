# Bootstrap Guide

Run these commands from the repository root.

## 1. Add supplied books

Put any book PDFs under `books/`:

```bash
mkdir -p books
cp /path/to/books/*.pdf books/
```

`books/` is gitignored. `/bootstrap` discovers `books/**/*.pdf` automatically, so you do not need to pass filenames or paths in the command.

## 2. Install Firecrawl once

Optional retrieval fallback:

```bash
npm install -g firecrawl-cli
firecrawl login --browser
```

Claude's native web search/fetch remains the default research path.

## 3. Start Claude Code

```bash
claude
```

## 4. Run the bootstrap

```text
/bootstrap
```

The command reconstructs progress from repository state, discovers local books, executes the next incomplete stage, verifies and repairs it, commits and pushes it, then continues automatically.

It stops only when a genuine user decision is required, such as approving a supplied-book substitution or exclusion.

## Resume later

Start Claude Code again from the repository root and run:

```text
/bootstrap
```

The bootstrap resumes from the next incomplete stage; no stage number, stage range, book paths, or repeated execution prompt is required.
