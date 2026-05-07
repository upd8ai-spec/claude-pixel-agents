# GeoFiscal AI MVP

Production-grade MVP blueprint and starter implementation for an AI-powered geographic financial reconciliation and public transparency platform.

## Stack
- Frontend: Next.js + TypeScript + Tailwind + Recharts + Leaflet
- Backend: FastAPI + SQLAlchemy + Redis queue hooks
- Data: PostgreSQL (+ PostGIS), Redis, optional ClickHouse
- AI: OpenAI-compatible abstraction with local-model-ready provider interface

## Modules (MECE)
1. Data Ingestion Layer
2. Reconciliation Engine
3. Geographic Financial Intelligence
4. Public Transparency Dashboard
5. AI Anomaly Detection Engine
6. Executive Command Center
7. Audit & Compliance
8. RBAC
9. Reporting & Exports
10. Demo Data Generation

## Quick Start
```bash
cd geofiscal-ai-mvp
cp .env.example .env
docker compose up --build
```

- Backend: http://localhost:8000/docs
- Frontend: http://localhost:3000

## Included Artifacts
- System architecture diagram: `docs/architecture.md`
- Database ERD + schema: `docs/database-schema.md`
- API contracts: `docs/api.md`
- Deployment guide: `docs/deployment.md`
- Technical debt log and roadmap: `docs/roadmap-techdebt.md`

## Demo Data
Generate 100K+ realistic records with anomalies:
```bash
python data-generator/generate_demo_data.py --records 120000 --output ./data-generator/out
```
