# ðŸ§ª Enterprise QA Automation Framework (Python, PyTest, Selenium & Requests)

[![Testing](https://img.shields.io/badge/Test%20Framework-PyTest-blue?style=flat-square&logo=pytest)](https://pytest.org/)
[![UI Automation](https://img.shields.io/badge/UI%20Testing-Selenium%20WebDriver-green?style=flat-square&logo=selenium)](https://www.selenium.dev/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=flat-square&logo=githubactions)](./.github/workflows/test.yml)
[![Reports](https://img.shields.io/badge/Reports-Allure%20%2F%20HTML-yellowgreen?style=flat-square)](https://github.com/aryanpandya)

A production-ready test automation framework adhering to the **Page Object Model (POM)** design pattern. Capable of driving parallel cross-browser regression suites (Chrome, Firefox, Headless) and automated REST API validation.

---

## ðŸ—ï¸ Framework Architecture
- **Page Object Model (POM)**: Decouples UI locators from test logic for maximum maintainability.
- **Data-Driven Testing**: Externalized JSON and CSV test fixtures for parameterized verification.
- **API Test Layer**: Validates HTTP status codes, JSON payload schemas, headers, and authentication tokens via `requests`.
- **Continuous Integration**: Runs headless regression tests automatically on every GitHub Pull Request.

---

## âš¡ Running Tests Locally

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run all tests with HTML report
pytest --html=reports/report.html --self-contained-html

# 3. Run in parallel (4 threads)
pytest -n 4
```
