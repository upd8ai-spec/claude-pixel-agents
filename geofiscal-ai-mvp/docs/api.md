# API Surface

## Auth
- `POST /api/v1/auth/login`
- `POST /api/v1/auth/refresh`

## Ingestion
- `POST /api/v1/ingestion/upload`
- `POST /api/v1/ingestion/run`
- `GET /api/v1/ingestion/jobs/{id}`

## Reconciliation
- `POST /api/v1/reconciliation/run`
- `GET /api/v1/reconciliation/results`

## GIS/Transparency
- `GET /api/v1/geo/heatmap`
- `GET /api/v1/transparency/district/{district_code}`

## AI Risk
- `GET /api/v1/risk/anomalies`
- `POST /api/v1/risk/summarize`

## Audit
- `GET /api/v1/audit/events`
