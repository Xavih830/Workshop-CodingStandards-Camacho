# Student Grade Management System - Coding Standards Lab

This repository contains the practical assignment for the Software Engineering II Coding Standards lab at ESPOL (Section A - Python).

The project starts from an intentionally flawed base program (`test.py`) that exhibits poor naming conventions, syntax/runtime errors, and missing functionality. The objective is to identify violations using static analysis tools (Flake8 and Pylint), refactor the code according to PEP 8 standards and project requirements, and collect initial and final quality reports.

## Project Structure

- `test.py`: Student grade management source code.
- `run_flake8.ps1`: Script to run Flake8 and produce console, text, and HTML reports.
- `run_pylint.ps1`: Script to run Pylint and generate text and HTML reports.
- `requirements.txt`: Pinned Python dependencies.
- `reports/`:
  - `initial/`: Initial reports generated from the base code.
  - `final/`: Final reports generated after refactoring.
- `evidencias/`: Folder for screenshots to be included in the report.
- `.github/workflows/coding-standards.yml`: CI workflow running linter checks on pull requests.

## Setup and Usage

1. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. Run linters:
   ```powershell
   # Initial baseline run
   .\run_flake8.ps1 test.py initial
   .\run_pylint.ps1 test.py initial

   # Final verification run
   .\run_flake8.ps1 test.py final
   .\run_pylint.ps1 test.py final
   ```

Interactive HTML reports are saved to `reports/initial/flake8_html/index.html` (or `reports/final/flake8_html/index.html`).
