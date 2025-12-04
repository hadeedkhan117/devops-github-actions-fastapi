# DevOps GitHub Actions FastAPI Demo

Complete DevOps project with FastAPI, Docker, and GitHub Actions CI/CD.

## Quick Start

### Local Development
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Docker
```bash
docker compose up --build
```

## Endpoints
- `GET /` - API status
- `POST /echo` - Echo message
- `GET /frontend` - Interactive demo page

## Testing
```bash
pytest -v
ruff check .
```# Demo change
