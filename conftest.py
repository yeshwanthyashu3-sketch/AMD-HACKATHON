"""
Pytest conftest.py for ROCm Navigator Security & Reporting Suite.
Provides shared session-level fixtures for database path isolation during testing.
"""
import os
import sys
import pytest

# Ensure project root is on the Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


def pytest_configure(config):
    """Register custom markers to suppress unknown-marker warnings."""
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test requiring running server"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow (excluded from quick runs)"
    )
