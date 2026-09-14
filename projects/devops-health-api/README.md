# ⚡ DevOps Health API

<p align="center">
  <strong>A production-style mini DevOps project demonstrating containerization, automated testing, CI/CD quality gates and container security.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-3.1-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions"/>
  <img src="https://img.shields.io/badge/Trivy-Security-1904DA?style=for-the-badge&logo=aqua&logoColor=white" alt="Trivy"/>
</p>

## 🎯 Project Overview

`devops-health-api` is a small cloud-ready HTTP service designed to showcase a practical DevOps delivery workflow without unnecessary application complexity.

The project demonstrates:

- Application health and readiness-style endpoints
- Automated unit testing with `pytest`
- Reproducible Docker image builds
- Non-root container execution
- Docker Compose for local operations
- GitHub Actions CI pipeline
- Container vulnerability scanning with Trivy
- Path-based workflow execution to keep CI efficient

## 🏗️ Architecture

```mermaid
graph LR
    Dev[Developer] --> Git[GitHub]
    Git --> CI[GitHub Actions]
    CI --> Test[Pytest]
    Test --> Build[Docker Build]
    Build --> Scan[Trivy Scan]
    Scan --> Ready[Validated Image]
    Ready --> Run[Container / Compose]
    Run --> Health[/health]
```

## 📁 Repository Structure

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🚀 Run Locally

### Option 1 — Python

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open:

- `http://localhost:8080/`
- `http://localhost:8080/health`

### Option 2 — Docker Compose

```bash
docker compose up --build
```

Stop it with:

```bash
docker compose down
```

## 🧪 Testing

```bash
pytest -q
```

## 🔄 CI/CD Workflow

Every push or pull request affecting this project triggers:

```text
Checkout
   ↓
Python 3.12 setup
   ↓
Dependency installation
   ↓
Pytest
   ↓
Docker image build
   ↓
Trivy HIGH/CRITICAL vulnerability scan
   ↓
Pipeline result
```

The workflow uses least-privilege GitHub Actions permissions and only runs when files under this project change.

## 🔐 Security Practices

This project intentionally includes a few production-minded controls:

| Control | Implementation |
|---|---|
| Non-root container | Dedicated UID `10001` |
| Dependency pinning | `requirements.txt` versions are pinned |
| Image scanning | Trivy scans HIGH/CRITICAL vulnerabilities |
| CI permissions | Read-only contents by default |
| Automated tests | Pytest quality gate |
| Health check | Docker Compose healthcheck |

## 📊 Endpoints

| Endpoint | Purpose |
|---|---|
| `GET /` | Service information |
| `GET /health` | Health status + UTC timestamp |

Example response:

```json
{
  "status": "healthy",
  "timestamp": "2026-01-01T12:00:00+00:00"
}
```

## 💼 DevOps Skills Demonstrated

**CI/CD** · GitHub Actions · Docker · Docker Compose · Python · Linux containers · Automated testing · Security scanning · Health checks · Git workflows · Infrastructure-ready application design

## 🛣️ Next Improvements

This starter can be extended into a larger portfolio project with:

- Terraform deployment to Azure Container Apps
- Azure Container Registry
- OIDC-based GitHub → Azure authentication
- Azure Monitor / Application Insights
- Prometheus metrics
- Environment promotion: Dev → QA → Prod
- Deployment approvals and rollback strategy
- SBOM generation and artifact signing

---

<p align="center">
  <strong>Built as a compact DevOps portfolio project by Yesh Pal.</strong><br/>
  <sub>Build → Test → Scan → Ship</sub>
</p>
