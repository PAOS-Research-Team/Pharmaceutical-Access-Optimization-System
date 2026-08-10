"""
API routes (controllers)
-------------------------
Thin HTTP layer only: parse/validate the request, call into services/,
and return a response. No business logic should live here — that
belongs in 1_core/domain or 2_backend/services.
"""

from fastapi import APIRouter, HTTPException

from 2_backend.schemas.validation import RecordCreateSchema, RecordResponseSchema
from 2_backend.services.core_service import create_record, get_record

router = APIRouter(tags=["records"])


@router.post("/records", response_model=RecordResponseSchema)
async def create_record_endpoint(payload: RecordCreateSchema):
    """Create a new record after validation. Delegates to the service layer."""
    record = await create_record(payload.dict())
    return record


@router.get("/records/{record_id}", response_model=RecordResponseSchema)
async def get_record_endpoint(record_id: str):
    """Fetch a single record by id, or 404 if it doesn't exist."""
    record = await get_record(record_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return record
