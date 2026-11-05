# :test_tube: Production QA Test Automation Framework

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Selenium WebDriver](https://img.shields.io/badge/Browser%20Automation-Selenium%204-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://selenium.dev)
[![PyTest](https://img.shields.io/badge/Test%20Runner-PyTest%207-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org)
[![CI/CD](https://img.shields.io/badge/Continuous%20Integration-GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](.github/workflows/test.yml)

An enterprise-grade, maintainable QA test automation framework built on Python, Selenium WebDriver 4, and PyTest. Implements the **Page Object Model (POM)** architectural pattern, multi-browser parallel test execution, API contract validation, and automated GitHub Actions CI/CD test reporting.

---

## :triangular_ruler: Framework Architecture

```mermaid
flowchart TD
    subgraph Test Execution Layer
        CLI[PyTest CLI Runner<br/>pytest -m smoke -n auto]
        CI[GitHub Actions CI Pipeline<br/>Multi-OS Matrix]
    end

    subgraph Configuration & Fixtures
        Conf[conftest.py<br/>WebDriver Factory]
        Ini[pytest.ini<br/>Markers & Rules]
    end

    subgraph Page Object Model POM
        Base[BasePage<br/>Explicit Waits & Safe Actions]
        LoginPage[LoginPage POM]
        DashPage[DashboardPage POM]
    end

    subgraph Target Applications & APIs
        Web[Web Applications / SaaS Portals]
        API[Backend REST Endpoints / SLAs]
    end

    CLI --> Conf
    CI --> Conf
    Conf --> Base
    Base --> LoginPage
    Base --> DashPage
    LoginPage --> Web
    DashPage --> Web
    CLI --> API
```

---

## :sparkles: Key Framework Features

- **Page Object Model (POM)**: Strict separation of test assertions from UI locators, eliminating brittle selectors and test maintenance overhead.
- **Explicit Dynamic Waits**: Zero hardcoded `sleep` calls. All interactions rely on `WebDriverWait` and `expected_conditions`.
- **Parallel Cross-Browser Execution**: Native support for running regressions across Chrome and Firefox concurrently (`pytest-xdist`).
- **Full-Stack Validation**: Seamlessly tests both UI frontend flows and backend REST API latency SLAs within a single unified runner.
- **CI/CD Integration**: Executes headless regressions automatically on every pull request, outputting JUnit XML test reports and failure screenshots.

---

## :rocket: Getting Started

### 1. Installation
```bash
git clone https://github.com/Aryan-136/qa-automation-framework.git
cd qa-automation-framework

python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Running Test Suites
```bash
# Run critical smoke tests
pytest -m smoke

# Run full regression suite in parallel (4 workers)
pytest -m regression -n 4

# Run API SLA validation tests
pytest tests/api/

# Run with HTML test report generation
pytest --html=report.html --self-contained-html
```

---

## :file_folder: Repository Layout
```text
.
â”œâ”€â”€ .github/
â”‚   â””â”€â”€ workflows/
â”‚       â””â”€â”€ test.yml              # Automated CI matrix execution
â”œâ”€â”€ pages/
â”‚   â”œâ”€â”€ base_page.py              # Foundational Page Object with explicit waits
â”‚   â””â”€â”€ login_page.py             # Authentication portal POM
â”œâ”€â”€ tests/
â”‚   â”œâ”€â”€ api/
â”‚   â”‚   â””â”€â”€ test_telemetry_api.py # REST API contract & latency tests
â”‚   â””â”€â”€ e2e/
â”‚       â””â”€â”€ test_auth.py          # End-to-end browser authentication flows
â”œâ”€â”€ conftest.py                   # PyTest browser fixtures & CLI parameters
â”œâ”€â”€ pytest.ini                    # Test execution rules and custom markers
â”œâ”€â”€ requirements.txt              # Framework dependencies
â””â”€â”€ README.md                     # Architectural documentation
```