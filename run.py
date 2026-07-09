#!/usr/bin/env python3
"""
ROCm Navigator — Quick Launch Script
Starts the Security & Reporting Gateway and opens the browser dashboard.
Owner: Yashwant (Member 5 — Security & Reporting Lead)
"""

import os
import sys
import subprocess
import time
import threading

# Ensure proper working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

BANNER = """
╔══════════════════════════════════════════════════════════════════════╗
║        ROCm Navigator — Security & Reporting Gateway                 ║
║        Member 5: Yashwant | AMD Instinct™ Hackathon 2026             ║
╠══════════════════════════════════════════════════════════════════════╣
║  Dashboard:    http://localhost:8000/dashboard                        ║
║  Swagger UI:   http://localhost:8000/docs                             ║
║  ReDoc:        http://localhost:8000/redoc                            ║
║  Security:     http://localhost:8000/security                         ║
║  Reports:      http://localhost:8000/reports                          ║
║  Compliance:   http://localhost:8000/compliance                       ║
╚══════════════════════════════════════════════════════════════════════╝
"""

def run_quick_audit():
    """Run a quick audit and print the safety score."""
    try:
        from agents.security.security_agent import SecurityAgent
        from agents.reports.reports_agent import ReportsAgent

        print("\n[*] Running quick security audit...\n")
        agent = SecurityAgent(workspace_path=".")
        results = agent.perform_full_audit()

        print(f"  Safety Score   : {results['safety_score']}/100")
        print(f"  Secrets Found  : {len(results['secrets_findings'])}")
        print(f"  Vulnerabilities: {len(results['vulnerabilities'])}")
        print(f"  Container Issues: {len(results['container_findings'])}")

        print("\n[*] Generating report bundle...\n")
        reporter = ReportsAgent(workspace_path=".")
        bundle = reporter.compile_report_bundle(results, session_id="launch_demo")
        for fmt, path in bundle.items():
            print(f"  {fmt}: {path}")

        print("\n[✓] Quick audit complete!\n")
    except Exception as e:
        print(f"[!] Quick audit error: {e}")


def start_server():
    """Start the FastAPI server via uvicorn."""
    try:
        import uvicorn
        import services.security_audit.app as app_module  # noqa: F401
        uvicorn.run(
            "services.security-audit.app:app",
            host="127.0.0.1",
            port=8000,
            reload=False,
            log_level="info"
        )
    except ModuleNotFoundError:
        # Try alternate import path
        subprocess.run([
            sys.executable, "-m", "uvicorn",
            "services.security-audit.app:app",
            "--host", "127.0.0.1",
            "--port", "8000",
            "--reload"
        ])


if __name__ == "__main__":
    print(BANNER)

    mode = sys.argv[1] if len(sys.argv) > 1 else "server"

    if mode == "audit":
        run_quick_audit()
    elif mode == "test":
        subprocess.run([sys.executable, "-m", "pytest", "tests/", "-v", "--tb=short"])
    elif mode == "server":
        # Run a quick audit first to warm up the database
        run_quick_audit()
        print("[*] Starting FastAPI server at http://127.0.0.1:8000 ...\n")
        start_server()
    else:
        print(f"Usage: python run.py [server|audit|test]")
        print(f"  server  — Start the FastAPI gateway (default)")
        print(f"  audit   — Run a quick security audit and print results")
        print(f"  test    — Run the full pytest test suite")
