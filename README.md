# AI-Portfolio-Analyzer

An AI-powered portfolio analysis platform that evaluates resumes and GitHub repositories, generates skill assessments, highlights missing technologies, and recommends career paths and learning roadmaps.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [CLI](#cli)
  - [API / Web UI](#api--web-ui)
- [Architecture](#architecture)
- [Configuration](#configuration)
- [Development](#development)
  - [Testing](#testing)
  - [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)
- [Contact](#contact)

---

## Overview

AI-Portfolio-Analyzer helps job-seekers, hiring managers, and developers understand strengths and gaps in technical portfolios. It analyzes resumes and GitHub repositories using AI-driven NLP and static code analysis to produce:

- Skill assessments mapped to industry frameworks
- Highlighted missing or underrepresented technologies
- Suggested career paths and role-fit recommendations
- Personalized learning roadmaps and curated resources

This repository contains the backend, analysis pipelines, model interfaces, and (optionally) frontend code used to deliver these capabilities.

## Features

- Resume parsing and skill/entity extraction (PDF/DOCX)
- GitHub repository analysis (language detection, activity, tests, docs)
- Gap detection and prioritized learning roadmap generation
- Role and career-path recommendation engine using LLMs
- Exportable reports (JSON/HTML/PDF)
- REST API for automation and integrations

## Quick Start

Prerequisites

- Python 3.9+
- Node.js 16+ (if frontend is included)
- Docker (recommended)
- An LLM provider API key (OpenAI or compatible)

Local (development) example

1. Clone the repository

   git clone https://github.com/Shehryar-coder/AI-Portfolio-Analyzer.git
   cd AI-Portfolio-Analyzer

2. Create and activate a virtual environment

   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   .\.venv\Scripts\activate  # Windows (PowerShell/CMD)

3. Install Python dependencies

   pip install -r requirements.txt

4. Copy the example env and set secrets

   cp .env.example .env
   # Edit .env and add MODEL_API_KEY, GITHUB_TOKEN, DATABASE_URL, etc.

5. Run the service

   flask run --host 0.0.0.0 --port 8000

Or using Docker

   docker build -t ai-portfolio-analyzer .
   docker run --env-file .env -p 8000:8000 ai-portfolio-analyzer

## Usage

CLI

Analyze a resume and a GitHub repo from the command line:

   python cli/analyze.py --resume path/to/resume.pdf --repo https://github.com/owner/repo

Output: JSON report written to ./reports or printed to stdout.

API / Web UI

POST /api/v1/analyze
- Body: multipart form with `resume` file and `repo_url` field
- Response: { "report_id": "...", "summary": { ... } }

Open http://localhost:8000 to access the web dashboard (if included).

## Architecture

- Ingest: Resume parser and GitHub connector
- Analysis: NLP extractors + static code analysis for repo signals
- Intelligence: LLM-driven scoring, gap detection, and recommendation generation
- Presentation: HTTP API and optional frontend dashboard

Main folders

- backend/ — API, orchestration, and model interfaces
- analysis/ — pipelines and feature extractors
- models/ — prompt templates and model wrappers
- cli/ — command-line utilities
- frontend/ — (optional) web UI
- docs/ — documentation and examples

## Configuration

Required environment variables (example):

- MODEL_API_KEY — API key for your LLM provider
- MODEL_PROVIDER — e.g. openai
- GITHUB_TOKEN — (optional) GitHub token for higher rate limits
- DATABASE_URL — e.g. sqlite:///data/db.sqlite or Postgres DSN
- STORAGE_DIR — path to store uploaded artifacts

Do not commit secrets to the repository.

## Development

- Use pre-commit hooks for linting and formatting
- Follow typing and coding standards used in the repo

Testing

Run unit tests:

   pytest tests/

Run linters / formatters:

   pre-commit run --all-files

Contributing

Contributions are welcome. Typical workflow:
1. Fork the repository
2. Create a feature branch (git checkout -b feat/short-description)
3. Commit and push your changes
4. Open a Pull Request describing the change

See CONTRIBUTING.md (if present) for more details.

## Roadmap

Planned improvements:

- Deeper static analysis (dependency graphs, security checks)
- Personalized interactive learning plans and progress tracking
- Team-level benchmarking and comparisons
- Additional model providers and on-premise deployment options

## License

This project is available under the MIT License. See LICENSE for details.

## Contact

Created and maintained by Shehryar-coder.
For questions, bugs, or feature requests, please open an issue in this repository.
