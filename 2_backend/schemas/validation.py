"""
Pydantic schemas (input/output validation)
---------------------------------------------
Acts as the guardrail between the outside world and the API: every
request body and response is validated/shaped here before touching
business logic.
"""

from pydantic import BaseModel, Field


class RecordCreateSchema(BaseModel):
    """Shape required to create a new record via POST /api/records."""
    id: str = Field(..., min_length=1, description="Client-supplied unique id")
    payload: dict = Field(..., description="Arbitrary JSON payload for the record")


class RecordResponseSchema(BaseModel):
    """Shape returned to clients after create/fetch operations."""
    id: str
    payload: dict
