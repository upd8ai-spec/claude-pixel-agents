# System Architecture

```mermaid
flowchart LR
  A[ERP/CSV/API Sources] --> B[Ingestion Service]
  B --> C[Validation + Mapping]
  C --> D[(PostgreSQL/PostGIS)]
  C --> E[(Object Storage)]
  D --> F[Reconciliation Engine]
  D --> G[Anomaly Engine]
  G --> H[AI Explainability Service]
  F --> I[Audit/Lineage Service]
  G --> I
  D --> J[GIS Analytics Service]
  J --> K[Executive API]
  F --> K
  H --> K
  K --> L[Next.js Frontend]
  K --> M[Public Transparency API]
  M --> N[Citizen Portal]
  O[(Redis)] --> B
  O --> F
  O --> G
```

## Security & Governance
- JWT auth, RBAC, SSO-ready OIDC adapter
- Immutable audit event ledger table + hash chain
- Row-level security by jurisdiction scope
- KMS-backed encryption at rest and TLS in transit

## Observability
- OpenTelemetry tracing
- Structured JSON logs
- Prometheus metrics + Grafana dashboards
- Health probes: liveness/readiness/startup
