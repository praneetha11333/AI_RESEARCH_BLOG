# AI Research Blog

A fully autonomous daily AI news blog for students. Every morning, a LangChain agent searches for recent AI news, picks 3–5 stories from different domains, writes cited summaries, and publishes them as a static MkDocs site via GitHub Pages.

## How it works

1. `agent.py` — runs the research agent. It calls DuckDuckGo (3–5 searches), validates the results, and writes a dated post to `docs/posts/`.
2. `build_index.py` — rebuilds `docs/index.md` with links to all posts.
3. GitHub Actions (`.github/workflows/daily-blog.yml`) — runs both scripts every day at 07:00 IST, commits the new post, and deploys the site to GitHub Pages.

## Project structure

```
agent.py              # Research agent
build_index.py        # Homepage builder
docs/posts/           # Generated daily digests
memory/               # Agent memory (editorial goals, past runs)
logs/runs.jsonl       # Run logs (published / skipped / failed)
mkdocs.yml            # MkDocs site config
requirements.txt      # Python dependencies
```

## Setup

### 1. Clone and install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set environment variables

Create a `.env` file:

```
OPENAI_API_KEY=<your_api_key>
MODEL=<model_name>          # optional, defaults to gpt-5.6-luna
```

The agent uses [aipipe.org](https://aipipe.org) as the OpenAI-compatible base URL.

### 3. Run locally

```bash
python agent.py        # generate today's post
python build_index.py  # rebuild the homepage
mkdocs serve           # preview the site
```

Set `FORCE=1` to regenerate a post that already exists:

```bash
FORCE=1 python agent.py
```

## GitHub Actions setup

1. Go to **Settings → Secrets and variables → Actions** in your repo.
2. Add a secret: `OPENAI_API_KEY`
3. Optionally add a variable: `MODEL`
4. Enable **GitHub Pages** from the `gh-pages` environment (Actions will configure it automatically).

The workflow runs on every push to `main`, on manual trigger (`workflow_dispatch`), and on a daily schedule.

## Tech stack

- [LangChain](https://github.com/langchain-ai/langchain) — agent framework
- [DuckDuckGo Search (ddgs)](https://github.com/deedy5/duckduckgo_search) — news search
- [MkDocs](https://www.mkdocs.org/) — static site generator
- [Pydantic](https://docs.pydantic.dev/) — structured output validation
- GitHub Actions + GitHub Pages — CI/CD and hosting
