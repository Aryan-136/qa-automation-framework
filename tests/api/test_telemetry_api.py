"""
API Contract & Health Check Automation Tests
"""
import pytest
import requests

BASE_URL = "https://aryan-136.github.io/cyber-snake-arcade"


@pytest.mark.api
@pytest.mark.smoke
class TestTelemetryAPI:

    def test_health_endpoint_status(self):
        """Verify web application returns HTTP 200 OK."""
        response = requests.get(BASE_URL, timeout=5)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    def test_security_headers_present(self):
        """Verify response contains essential security headers."""
        response = requests.head(BASE_URL, timeout=5)
        headers = response.headers
        assert "Content-Type" in headers
        assert "text/html" in headers["Content-Type"].lower()

    def test_latency_performance_sla(self):
        """Verify endpoint responds within SRE SLA limit (<500ms)."""
        response = requests.get(BASE_URL, timeout=5)
        elapsed_ms = response.elapsed.total_seconds() * 1000
        assert elapsed_ms < 500, f"Latency SLA violation: {elapsed_ms}ms > 500ms"