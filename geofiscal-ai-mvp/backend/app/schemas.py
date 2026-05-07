from pydantic import BaseModel, Field
from typing import Literal

class ReconciliationRequest(BaseModel):
    budget: float = Field(gt=0)
    actual: float = Field(ge=0)
    tolerance_pct: float = Field(default=5, ge=0, le=100)

class ReconciliationResponse(BaseModel):
    status: Literal['matched','partially_matched','unmatched','suspicious']
    variance: float
    variance_pct: float
    confidence_score: float
    risk_score: float
    explanation: str
