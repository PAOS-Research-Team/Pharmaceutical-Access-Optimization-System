# my-platform

A four-pillar platform separating algorithmic core logic, backend
API/persistence, frontend UI, and operational tooling.

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
