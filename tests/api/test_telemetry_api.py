"""
API Contract & Health Check Automation Tests.
Validates status codes, headers, response integrity, and latency SLAs.
"""
import os
import pytest
import requests

BASE_URL = os.getenv("API_BASE_URL", "https://aryan-136.github.io/cyber-snake-arcade")
SLA_MAX_MS = int(os.getenv("SLA_MAX_LATENCY_MS", "2500"))


@pytest.mark.api
class TestTelemetryAPI:

    @pytest.mark.smoke
    def test_health_endpoint_status(self):
        """Verify endpoint returns HTTP 200 OK."""
        response = requests.get(BASE_URL, timeout=10)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    @pytest.mark.smoke
    def test_security_and_content_headers(self):
        """Verify response contains standard content headers."""
        response = requests.head(BASE_URL, timeout=10)
        assert response.status_code == 200
        content_type = response.headers.get("Content-Type", "")
        assert "text/html" in content_type.lower(), f"Unexpected Content-Type: {content_type}"

    @pytest.mark.regression
    def test_response_body_integrity(self):
        """Verify response contains expected HTML content markers."""
        response = requests.get(BASE_URL, timeout=10)
        assert "<!doctype html>" in response.text.lower() or "<html" in response.text.lower()
        assert len(response.text) > 100, "Response body unexpectedly empty"

    @pytest.mark.regression
    def test_latency_performance_sla(self):
        """Verify endpoint latency adheres to SLA threshold."""
        # Warm-up request to establish TLS/TCP connection
        session = requests.Session()
        session.head(BASE_URL, timeout=10)

        response = session.get(BASE_URL, timeout=10)
        elapsed_ms = response.elapsed.total_seconds() * 1000
        assert elapsed_ms < SLA_MAX_MS, f"Latency SLA violation: {elapsed_ms:.1f}ms exceeds {SLA_MAX_MS}ms"
