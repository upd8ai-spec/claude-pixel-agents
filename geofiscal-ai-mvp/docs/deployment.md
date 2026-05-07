# Deployment Guide

## Local
- `docker compose up --build`

## Cloud (Kubernetes-ready)
- Containerize frontend/backend
- Use managed PostgreSQL + Redis
- Enable HPA for backend workers and APIs
- Add ingress with WAF and TLS termination

## CI/CD
- Lint/test/build on PR
- SBOM + image scan
- Progressive deployment (staging -> prod)
