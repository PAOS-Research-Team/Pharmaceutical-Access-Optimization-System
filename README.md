# P-A-O-S

A six-pillar platform separating algorithmic core logic, backend
API/persistence, frontend UI, operational tooling, machine learning,
and wearable hardware integration.

## Structure

- **1_core/** — Custom probabilistic data structures (Bloom filter,
  HyperLogLog, Cuckoo filter), pure domain logic, and math/hash utils.
  No framework dependencies; fully unit-testable in isolation.
- **2_backend/** — FastAPI application: routes, DB layer, Pydantic
  validation schemas, and the service layer that wires everything
  together (api -> services -> core/db).
- **3_frontend/** — Next.js client app: reusable components, data-fetching
  hooks, and page routes.
- **4_ops/** — Tests, DB seed scripts, Docker/Compose setup for local
  dev, and an `.env.example` template.
- **5_ml/** — Machine learning models: quality prediction (regression),
  material substitution classifier, manufacturing anomaly detection,
  supply forecasting, and bootstrap uncertainty quantification. Plus
  shared preprocessing utilities and a model save/load registry.
- **6_hardware/** — Wearable device integration: BLE connector, reading
  data model, and an ingestion poller that streams validated sensor
  readings toward the backend.

## Getting started

```bash
pip install -r requirements.txt
cp 4_ops/.env.example .env
uvicorn 2_backend.main:app --reload
```

```bash
cd 3_frontend
npm install
npm run dev
```

## Tests

```bash
pytest 4_ops/tests
```
