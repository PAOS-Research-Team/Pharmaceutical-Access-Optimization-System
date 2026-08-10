# Dockerfile for the backend API service.
# Multi-stage-ready base; keep dependencies pinned via requirements.txt.

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Run the FastAPI app defined in 2_backend/main.py
CMD ["uvicorn", "2_backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
