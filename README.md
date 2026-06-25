# AI Developer Portfolio Analyzer

A Flask web app that analyzes a student's resume (PDF) and GitHub profile to
generate scores, a skill-gap analysis, career-path matches, and a personalized
learning roadmap toward internship readiness.

## Tech Stack
- Python 3 + Flask
- SQLite (raw `sqlite3`, no ORM)
- HTML + CSS + Bootstrap 5
- GitHub REST API
- pdfplumber (PDF text extraction)

## Folder Structure
```
ai_portfolio_analyzer/
├── app.py                  # Flask app factory / entry point
├── config.py                # App configuration
├── utils.py                  # login_required decorator
├── requirements.txt
├── database/
│   └── schema.sql            # SQLite table definitions
├── models/
│   └── db.py                  # DB connection helpers
├── modules/
│   ├── resume_analyzer.py     # PDF parsing, skill/project extraction, scoring
│   ├── github_analyzer.py     # GitHub API calls, stats, scoring
│   └── career_engine.py       # Skill gap, career matching, roadmap logic
├── routes/
│   ├── auth.py                 # Register / Login / Logout
│   ├── dashboard.py            # Main dashboard route
│   ├── resume.py                 # Resume upload route
│   └── github.py                 # GitHub analysis route
├── templates/                  # Jinja2 + Bootstrap 5 templates
├── static/
│   ├── css/style.css
│   └── js/script.js
├── uploads/                    # Uploaded resume PDFs (gitignored)
└── instance/                    # portfolio.db SQLite file (auto-created)
```

## Setup & Run (VS Code / Terminal)

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```
   Activate it:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   python app.py
   ```

4. Open your browser at **http://127.0.0.1:5000**

The SQLite database (`instance/portfolio.db`) and its tables are created
automatically on first run — no manual migration step needed.

## How It Works

1. **Register / Login** — session-based auth, passwords hashed with Werkzeug.
2. **Upload Resume** — text is extracted with `PyPDF2` for PDF resumes and
   built-in parsers for DOCX/DOC/TXT/RTF files. Scanned PDFs and images can
   also be processed with OCR if `Tesseract` is installed.
   The resume is then matched against a ~100-keyword skill dictionary and
   scanned for a "Projects" section.
   A 0-100 score is computed from content length, skills found,
   projects found, section coverage, and contact-info presence.
3. **Analyze GitHub** — enter a GitHub username; the app calls the public
   GitHub REST API (`/users/{username}` and `/users/{username}/repos`) to get
   total repos, most-used languages, total stars/forks, and computes a 0-100
   GitHub score.
4. **Skill Gap Analysis** — resume skills + GitHub language-derived skills are
   combined and compared against a master industry skill list to show
   existing / missing / recommended skills.
5. **Career Recommendation Engine** — combined skills are matched against 5
   career profiles (Software Engineer, Full Stack Developer, Data Scientist,
   AI Engineer, Cyber Security Analyst), each showing a match %, required
   skills, and missing skills.
6. **Learning Roadmap** — missing skills are grouped into 2-week phases with a
   suggested mini-project goal for each phase.
7. **Dashboard** — single page bringing all of the above together.

## Notes & Limitations (by design, for a student project)

- Resume parsing uses keyword + heuristic matching rather than a full NLP
  pipeline — works best with standard, text-based (not scanned) PDF resumes.
- GitHub API calls are unauthenticated, so they're subject to GitHub's public
  rate limit (60 requests/hour per IP). For heavier use, add a personal access
  token to the `headers` dict in `modules/github_analyzer.py`.
- Career skill profiles and the master skill dictionary are easy to extend —
  just edit the lists in `modules/career_engine.py` and
  `modules/resume_analyzer.py`.

## Database Tables
- `users` — id, username, email, password_hash, created_at
- `resume_analysis` — user_id, filename, extracted_skills (JSON), extracted_projects (JSON), resume_score, created_at
- `github_analysis` — user_id, github_username, total_repos, languages (JSON), total_stars, github_score, created_at
