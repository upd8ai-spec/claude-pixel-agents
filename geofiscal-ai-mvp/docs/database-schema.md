# Database Schema (Core)

## Primary Tables
- users, roles, user_roles
- geographies (country/state/district/ward hierarchy)
- projects
- budgets, allocations, expenditures
- tenders, procurements, invoices, payments
- vendors
- reconciliations, reconciliation_items
- anomalies
- ingestion_jobs, ingestion_records
- audit_events

## Example DDL Snippet
```sql
create table geographies (
  id bigserial primary key,
  geo_code text unique not null,
  name text not null,
  level text not null check (level in ('country','state','district','ward')),
  parent_id bigint references geographies(id),
  geom geometry(multipolygon, 4326)
);

create table reconciliations (
  id bigserial primary key,
  reconciliation_type text not null,
  run_at timestamptz not null default now(),
  status text not null,
  confidence_score numeric(5,2),
  risk_score numeric(5,2),
  explanation text
);
```

## Indexing & Partitioning
- Partition large fact tables by month (`expenditures`, `payments`, `invoices`)
- Composite indexes:
  - `(geo_id, fiscal_year)` for budgets/expenditures
  - `(vendor_id, invoice_number)` for duplicate checks
  - `(project_id, status)` for project risk views
