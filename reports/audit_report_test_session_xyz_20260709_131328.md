# ROCm Navigator: System Audit & Security Report
**Session ID:** `test_session_xyz`
**Generated At:** 2026-07-09T13:13:26.317491
**Overall Safety Rating Score:** 68/100

---

## 1. Executive Summary
ROCm Navigator has completed an autonomous scan and compliance verification of the workspace assets. Below is the rating profile for the current state:

| Assessment Dimension | Rating Contribution |
|:---|:---|
| **Dependency Pinning & Version Integrity** | 18/20 |
| **Secrets & Credential Exposure** | 0/30 |
| **Authentication Flow & Access Rules** | 20/20 |
| **Execution Container Sandboxing** | 15/15 |
| **Memory Boundaries & Static Checking** | 15/15 |
| **Combined System Safety Rating** | **68/100** |

---

## 2. Secrets & Credentials Scan Result
Detected 18 potential api credentials or configuration secrets in the workspace.

| File Path | Line | Secret Type | Disclosed Pattern (Scrubbed) | Severity |
|:---|:---|:---|:---|:---|
| `.env` | 2 | JWT Token | `eyJh***M1Cs` | **HIGH** |
| `.env` | 3 | Database Connection String | `post***CH5@` | **HIGH** |
| `.github/workflows/security_ci.yml` | 340 | High-Entropy String | `'fir***026'` | **HIGH** |
| `.github/workflows/security_ci.yml` | 378 | High-Entropy String | `"===***==="` | **HIGH** |
| `.github/workflows/security_ci.yml` | 380 | High-Entropy String | `"===***==="` | **HIGH** |
| `.github/workflows/security_ci.yml` | 388 | High-Entropy String | `"===***==="` | **HIGH** |
| `reports/audit_report_test_session_xyz_20260709_105607.json` | 153 | High-Entropy String | `"aud***607"` | **HIGH** |
| `reports/audit_report_test_session_xyz_20260709_105634.json` | 160 | High-Entropy String | `"aud***634"` | **HIGH** |
| `reports/audit_report_test_session_xyz_20260709_110925.json` | 167 | High-Entropy String | `"aud***925"` | **HIGH** |
| `reports/audit_report_test_session_xyz_20260709_113615.json` | 174 | High-Entropy String | `"aud***615"` | **HIGH** |
| `reports/audit_report_test_session_xyz_20260709_125835.json` | 195 | High-Entropy String | `"aud***835"` | **HIGH** |
| `reports/audit_report_test_session_xyz_20260709_125847.json` | 202 | High-Entropy String | `"aud***847"` | **HIGH** |
| `tests/test_security_reporting.py` | 64 | OpenAI API Key | `sk-a***z111` | **CRITICAL** |
| `tests/test_security_reporting.py` | 64 | Generic Token/Key | `API_***111"` | **HIGH** |
| `tests/test_security_reporting.py` | 65 | AWS Access Key ID | `AKIA***1234` | **CRITICAL** |
| `tests/test_security_reporting.py` | 243 | High-Entropy String | `"sk-***ear"` | **HIGH** |
| `tests/test_security_reporting.py` | 922 | Database Connection String | `post***ass@` | **HIGH** |
| `tests/test_security_reporting.py` | 934 | Database Connection String | `post***ass@` | **HIGH** |

---

## 3. Static Code Memory & Safety Analysis
Detected 0 vulnerabilities or unsafe thread concurrency patterns.

> [!NOTE]
> **Excellent:** Static parsing indicates memory copy size parameters are bound properly, and kernel execution structures verify safely.

---

## 4. Container Sandbox Security Scan Result
Detected 0 container security vulnerabilities.

> [!NOTE]
> **Excellent:** Container build configurations comply with secure container execution standards (running as non-root user, minimal privileges).

---

## 5. Software Bill of Materials (SBOM) & Licenses
Total Direct Dependencies Identified: 10

| Dependency Name | Declared Version | Installation Source | Resolved Licensing |
|:---|:---|:---|:---|
| `fastapi` | `0.111.0` | pip | MIT |
| `uvicorn` | `0.30.1` | pip | MIT / Apache-2.0 |
| `pydantic` | `2.7.0` | pip | MIT / Apache-2.0 |
| `cryptography` | `42.0.8` | pip | MIT / Apache-2.0 |
| `reportlab` | `4.2.2` | pip | BSD |
| `requests` | `2.32.3` | pip | MIT / Apache-2.0 |
| `pytest` | `8.2.2` | pip | MIT / Apache-2.0 |
| `pytest-asyncio` | `0.23.7` | pip | MIT / Apache-2.0 |
| `httpx` | `0.27.0                # Required by FastAPI TestClient` | pip | MIT / Apache-2.0 |
| `flake8` | `7.1.0` | pip | MIT / Apache-2.0 |

---

## 6. Sequential Audit Log Timeline
Historical records fetched from the database logging system:

| Timestamp | Executing Agent | Step Action | Status | Summary Message |
|:---|:---|:---|:---|:---|
| 2026-07-09T13:10:09 | TestAgent | live_neon_test | SUCCESS | Neon cloud connection verified from local test |
| 2026-07-09T13:11:46 | TestAgent | test_step_db_write | SUCCESS | Pytest audit step log entry — database write test. |
| 2026-07-09T13:11:58 | TestAgent | test_failure_log | FAILED | Simulated failure condition for test purposes. |
| 2026-07-09T13:12:39 | ReportAgent | compile_report_bundle | SUCCESS | Successfully generated Markdown, PDF, and JSON report file bundle under reports/. |
| 2026-07-09T13:12:51 | ReportAgent | compile_report_bundle | SUCCESS | Successfully generated Markdown, PDF, and JSON report file bundle under reports/. |
| 2026-07-09T13:13:02 | ReportAgent | compile_report_bundle | SUCCESS | Successfully generated Markdown, PDF, and JSON report file bundle under reports/. |
| 2026-07-09T13:13:14 | ReportAgent | compile_report_bundle | SUCCESS | Successfully generated Markdown, PDF, and JSON report file bundle under reports/. |
| 2026-07-09T13:13:16 | TestAgent | test_step_db_write | SUCCESS | Pytest audit step log entry — database write test. |
| 2026-07-09T13:13:17 | SecurityAgent | scan_execution | SUCCESS | Invoked GET /security endpoint. Commencing static analysis and secrets sweep. |
| 2026-07-09T13:13:24 | SystemGateway | audit_pipeline_init | SUCCESS | Starting full system audit pipeline run for session: test_session_xyz |

---
*Document cryptographically compiled and verified inside ROCm Navigator System Gateways.*