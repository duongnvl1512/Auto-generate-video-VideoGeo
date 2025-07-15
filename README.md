# Auto-Generate Video Project

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [Notes](#notes)

---

## Introduction

This project automates web tasks using Playwright, including login, scraping, and other web interactions. It is designed to simplify repetitive tasks and enhance productivity by leveraging browser automation.

### Key Features:

- **Login Automation**: Automatically logs in using credentials stored in an Excel file.
- **OTP Handling**: Waits for user input to complete OTP-based authentication.
- **Modular Design**: Tasks and utilities are organized into separate modules for better maintainability.
- **Retry Mechanism**: Includes helper functions for retrying failed operations.
- **Logging**: Provides detailed logs for debugging and monitoring.

## Project Structure

```bash
├── main.py                    # Entry point of the application
├── config/
│   └── settings.py            # General configuration: URL, headless mode, timeout...
├── core/
│   ├── browser.py             # Creates and manages Playwright browser instances
│   └── navigator.py           # Logic for navigating URLs and interacting with web pages
├── tasks/
│   └── task_sample.py         # Example task: login, scrape, etc.
├── utils/
│   └── helpers.py             # Common utility functions (logging, retry, etc.)
├── modules/
│   └── login.py               # Sample login module
├── requirements.txt           # Required Python libraries
└── README.md                  # Project documentation
```

## System Requirements

- Python 3.8 or higher
- pip (Python package manager)
- Google Chrome or Chromium (if running Playwright in non-headless mode)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/duongnvl1512/Auto-generate-video-VideoGeo.git
   cd Pw-auto-gen-vid
   ```
2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

## Configuration

- Update settings in `config/settings.py` (URL, timeout, headless mode, etc.)
- Add account details to `data/accounts.xlsx` (if using login functionality)

## Running the Project

Run the main script:

```bash
python main.py
```

Or execute specific tasks/modules:

```bash
python tasks/task_sample.py
python modules/login.py
```

## Notes

- Ensure browsers are installed for Playwright using the command `playwright install`.
- If you encounter browser-related errors, rerun the above command.
- You may need to modify configuration files, account details, or task logic to suit your use case.

---

For any questions, feel free to contact the project owner for support.
