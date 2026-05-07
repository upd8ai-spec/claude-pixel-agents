from fastapi import APIRouter
from app.schemas import ReconciliationRequest, ReconciliationResponse
from app.services.reconciliation import reconcile_amounts

router = APIRouter()

@router.post('/reconciliation/run', response_model=ReconciliationResponse)
async def run_reconciliation(payload: ReconciliationRequest):
    return reconcile_amounts(payload.budget, payload.actual, payload.tolerance_pct)

@router.get('/risk/anomalies')
async def get_anomalies():
    return {"items": [{"district":"DIST-045","signal":"spend_spike","severity":"high"}]}

@router.get('/geo/heatmap')
async def geo_heatmap():
    return {
        "type": "FeatureCollection",
        "features": [],
        "meta": {"metric": "utilization_ratio", "geo_level": "district"},
    }
