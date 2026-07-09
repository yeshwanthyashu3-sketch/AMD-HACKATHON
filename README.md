# 🔒 ROCm Navigator — Security & Reporting Suite
### Member 5 Module | Yashwant | Security & Reporting Lead

> **AMD Instinct™ Hackathon 2026** — Enterprise Security, Compliance, and Autonomous Report Generation for the ROCm Navigator CUDA→HIP Migration Platform

---

## 📋 Module Overview

This module implements the **Security & Reporting Layer** of ROCm Navigator — the enterprise-grade safety gate ensuring that all autonomously migrated GPU code is cryptographically secured, compliance-verified, and accompanied by professional audit documentation.

```text
┌─────────────────────────────────────────────────────────────────────┐
│              ROCm Navigator — Security & Reporting Gate             │
│                                                                     │
│  ┌─────────────┐  ┌─────────────┐  ┌────────────┐  ┌──────────┐   │
│  │   Secret    │  │   Memory    │  │    TEE     │  │  Report  │   │
│  │  Scanner    │  │   Safety    │  │   Vault    │  │ Compiler │   │
│  │ (Regex/TH)  │  │ (CUDA/HIP) │  │ (Fernet)   │  │ (MD/PDF) │   │
│  └──────┬──────┘  └──────┬──────┘  └─────┬──────┘  └─────┬────┘   │
│         └────────────────┴───────────────┴───────────────┘        │
│                              │                                      │
│                    FastAPI Gateway :8000                            │
│             Swagger · ReDoc · Dashboard · GitHub PR                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Architecture & Folder Structure

```
rocm-navigator/
├── agents/
│   ├── security/
│   │   ├── __init__.py
│   │   └── security_agent.py      ← Secret Scanner, TEE, SBOM, Memory Safety
│   └── reports/
│       ├── __init__.py
│       └── reports_agent.py       ← Markdown / PDF / JSON report compiler
│
├── shared/
│   └── database/
│       ├── __init__.py
│       ├── db.py                  ← SQLite audit log & scan result storage
│       ├── models.py              ← Dataclass schemas for all entities
│       ├── navigator.db           ← SQLite database (auto-created)
│       └── tee_vault.json         ← Encrypted TEE key store (auto-created)
│
├── services/
│   └── security-audit/
│       └── app.py                 ← FastAPI gateway with all API routes
│
├── tests/
│   └── test_security_reporting.py ← 50+ unit & integration tests (14 groups)
│
├── reports/                       ← Generated audit reports (auto-created)
│   ├── *.md                       ← Markdown reports
│   ├── *.pdf                      ← PDF reports (if reportlab installed)
│   ├── *.json                     ← JSON structured reports
│   ├── openapi.json               ← OpenAPI spec (auto-generated on startup)
│   └── postman_collection.json    ← Postman collection (auto-generated on startup)
│
├── .github/
│   └── workflows/
│       └── security_ci.yml        ← 7-job GitHub Actions CI/CD pipeline
│
├── Dockerfile                     ← Production container (Python 3.11-slim, non-root)
├── docker-compose.yml             ← Stack: gateway + test-runner services
├── requirements.txt               ← Python dependencies
├── pytest.ini                     ← Test configuration
└── conftest.py                    ← Shared pytest fixtures
```

---

## 🔑 APIs Owned

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/security` | Run full workspace security audit (secrets + memory + containers) |
| `POST` | `/audit` | Complete pipeline: scan → compile all report formats |
| `GET` | `/reports` | List all generated report artifacts from database |
| `GET` | `/compliance` | SBOM + OWASP API Security Top 10 checklist |
| `POST` | `/github/pr` | Automated Git branch → commit → Pull Request |
| `GET` | `/docs` | Custom dark-mode Swagger UI |
| `GET` | `/redoc` | ReDoc API documentation |
| `GET` | `/dashboard` | Live security telemetry dashboard panel |
| `GET` | `/download/{filename}` | Download generated report files |

---

## ⚡ Quickstart

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the API Gateway

```bash
# From the project root
python services/security-audit/app.py
```

Or with uvicorn:
```bash
uvicorn services.security-audit.app:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Open the Dashboard

```
http://localhost:8000/         ← Landing page
http://localhost:8000/dashboard ← Security telemetry dashboard
http://localhost:8000/docs     ← Swagger UI (dark mode)
http://localhost:8000/redoc    ← ReDoc documentation
```

### 4. Run a Security Audit

```bash
curl http://localhost:8000/security
```

### 5. Generate Full Report Bundle

```bash
curl -X POST http://localhost:8000/audit \
  -H "Content-Type: application/json" \
  -d '{"session_id": "hackathon_demo_001"}'
```

---

## 🐳 Docker

### Build & Run

```bash
# Build image
docker build -t rocm-navigator-security:latest .

# Run gateway
docker compose up security-gateway

# Run tests
docker compose --profile test run test-runner
```

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `GITHUB_TOKEN` | *(empty)* | GitHub Personal Access Token for real PR creation |
| `NAVIGATOR_ENV` | `production` | Environment mode (`production` / `test`) |
| `PYTHONUNBUFFERED` | `1` | Force unbuffered stdout for container logs |

---

## 🧪 Running Tests

```bash
# Full test suite (50+ tests across 14 test groups)
pytest tests/ -v

# Quick smoke test
pytest tests/test_security_reporting.py::TestTEEVault -v

# Specific group
pytest tests/test_security_reporting.py::TestFullAudit -v

# With coverage
pip install pytest-cov
pytest tests/ --cov=agents --cov=shared --cov-report=term-missing
```

### Test Coverage Matrix

| Test Group | Coverage Area | Tests |
|------------|--------------|-------|
| `TestDatabase` | SQLite CRUD operations | 5 |
| `TestDataModels` | Dataclass serialization | 5 |
| `TestTEEVault` | Encrypt/Decrypt/Store | 6 |
| `TestSecretScanning` | Regex secret detection | 5 |
| `TestMemorySafetyAnalysis` | CUDA/HIP static analysis | 4 |
| `TestContainerScanning` | Dockerfile misconfigs | 3 |
| `TestSBOMGeneration` | Dependency inventory | 4 |
| `TestFullAudit` | End-to-end audit pipeline | 6 |
| `TestMarkdownReports` | .md file generation | 4 |
| `TestJSONReports` | .json file generation | 4 |
| `TestReportBundle` | Multi-format bundle | 4 |
| `TestFastAPIGateway` | API endpoint integration | 8 |
| `TestTEEVaultSecurity` | Edge cases & security | 4 |
| `TestCompliance` | OWASP/scoring verification | 3 |

---

## 🛡️ Security Features

### 1. Secret Scanner
Detects exposed credentials using 15+ regex patterns:
- API Keys (OpenAI, Anthropic, Fireworks, AWS, GCP, Azure, GitHub)
- JWT Tokens
- Private SSH Keys
- Database connection strings with passwords
- Generic high-entropy token strings

### 2. Memory Safety Analyzer (CUDA/HIP)
Static analysis rules detecting:
- `CUDA-MEM-001`: Unchecked `cudaMemcpy` return codes
- `CUDA-MEM-002`: Unvalidated `cudaMalloc` result pointers
- `CUDA-SYNC-001`: Missing `cudaGetLastError()` post-kernel checks
- `HIP-MEM-001`: Unchecked `hipMemcpy` return codes
- `HIP-MEM-002`: Unvalidated `hipMalloc` result pointers

### 3. TEE (Trusted Execution Environment) Simulation
- **Primary mode**: PBKDF2+Fernet AES-256-CBC encryption via `cryptography` library
- **Fallback mode**: XOR+Base64 cipher when `cryptography` is unavailable
- Encrypted JSON vault at `shared/database/tee_vault.json`
- 100,000-iteration PBKDF2 key derivation

### 4. Container Security Scanning
Checks Dockerfiles for:
- `USER root` privilege escalation
- Port `22` (SSH) exposure
- Missing `HEALTHCHECK` directives
- Multi-stage build optimization opportunities
- Privileged execution flags

### 5. SBOM (Software Bill of Materials)
Auto-generates from `requirements.txt`:
- Full dependency inventory with versions
- License classification (MIT, Apache-2.0, BSD, etc.)
- Risk level assessment per package

### 6. OWASP API Security Top 10 Compliance
All 10 categories verified:
- Broken Object Level Authorization → ✅ FastAPI Depends hooks
- Broken Authentication → ✅ JWT with expiry
- Broken Object Property Level Auth → ✅ Schema filtering
- Unrestricted Resource Consumption → ✅ cgroups limits
- Broken Function Level Authorization → ✅ RACI validation
- Unrestricted Business Flow Access → ✅ LLM rate gates
- SSRF → ✅ Container network isolation
- Security Misconfiguration → ✅ TEE key derivation
- Improper Assets Management → ✅ Versioned API paths
- Unsafe API Consumption → ✅ Input type validation

---

## 📊 Report Formats

### Markdown Report (`.md`)
- Executive summary with safety score gauge
- Secrets scan results (scrubbed, never raw)
- Memory safety vulnerability table
- Container security findings
- SBOM dependency inventory
- OWASP compliance checklist
- Audit timeline from database logs

### PDF Report (`.pdf`)
- Generated via `reportlab` if installed
- Falls back to HTML → `.pdf` filename if not installed
- Includes all sections from Markdown report

### JSON Report (`.json`)
```json
{
  "session_id": "hackathon_demo_001",
  "generated_at": "2026-07-07T10:30:00Z",
  "safety_score": 87.5,
  "ratings_breakdown": {...},
  "secrets_findings": [...],
  "vulnerabilities": [...],
  "sbom": {...},
  "tee_status": {...},
  "audit_logs": [...]
}
```

### OpenAPI Specification (`openapi.json`)
Auto-generated on gateway startup, saved to `reports/openapi.json`.

### Postman Collection (`postman_collection.json`)
Auto-generated on gateway startup with all endpoint configurations.

---

## 🔄 GitHub PR Automation

The `POST /github/pr` endpoint automates:
1. `git init` (if not already initialized)
2. `git checkout -b <head_branch>`
3. `git add .` → `git commit -m <title>`
4. If `GITHUB_TOKEN` set: `git push` + GitHub API PR creation
5. If no token: simulated PR response with metadata

---

## 🚀 CI/CD Pipeline (GitHub Actions)

7-stage pipeline defined in `.github/workflows/security_ci.yml`:

```
Lint → Secret Scan → Tests → Report Gen → Compliance → API Validate → TEE → Gate
```

Triggers on every push and pull request to all branches.

---

## 🏆 Hackathon Deliverables Checklist

- [x] **Security Agent** — `agents/security/security_agent.py`
- [x] **Secret Scanning** — Regex-based with 15+ patterns, scrubbed output
- [x] **TEE Simulation** — Fernet AES encryption vault with PBKDF2 key derivation
- [x] **Reports Agent** — `agents/reports/reports_agent.py` (MD + PDF + JSON)
- [x] **Swagger/OpenAPI** — Custom dark-mode UI + auto-exported JSON
- [x] **GitHub PR Automation** — `POST /github/pr` with real/simulated modes
- [x] **OWASP Compliance** — Full API Security Top 10 verification
- [x] **Audit Logs** — SQLite-backed timeline with per-step agent tracking
- [x] **SBOM** — Auto-generated Software Bill of Materials
- [x] **Dashboard** — Live dark-mode telemetry panel at `/dashboard`
- [x] **Tests** — 50+ tests across 14 groups in `tests/`
- [x] **CI/CD** — 7-job GitHub Actions pipeline
- [x] **Docker** — Production Dockerfile + docker-compose.yml
- [x] **Data Models** — Type-safe dataclass schemas in `shared/database/models.py`

---

## 👤 Owner

**Yashwant** — Member 5, Security & Reporting Lead  
AMD Instinct™ Hackathon 2026 | ROCm Navigator Team

*Workload: 8% of total system (28 estimated hours)*
