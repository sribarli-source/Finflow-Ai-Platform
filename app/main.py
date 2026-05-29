from fastapi import FastAPI, Response
from pydantic import BaseModel
from prometheus_client import Counter, Histogram, generate_latest
from datetime import datetime
import time, random, json

app = FastAPI(title="FinFlow Transaction API", version="1.0.0")

REQ_COUNT   = Counter('finflow_requests_total', 'Total requests', ['endpoint', 'status'])
REQ_LATENCY = Histogram('finflow_request_duration_seconds', 'Latency', ['endpoint'])
FRAUD_FLAGS = Counter('finflow_fraud_flags_total', 'Fraud flags')

class Transaction(BaseModel):
    transaction_id: str
    amount: float
    currency: str
    merchant: str
    user_id: str

class FraudScore(BaseModel):
    transaction_id: str
    risk_score: float
    is_flagged: bool
    reason: str
    scored_at: str

@app.get("/health")
def health():
    return {"status": "healthy", "service": "finflow-api", "ts": datetime.utcnow().isoformat()}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")

@app.get("/api/v1/stats")
def stats():
    return {"service": "finflow-api", "version": "1.0.0", "status": "operational"}

@app.post("/api/v1/transactions/score")
def score(tx: Transaction):
    t = time.time()

    risk = 0.0
    reason = "normal"

    if tx.amount > 5000:
        risk += 0.35
        reason = "high_value"

    if tx.currency not in ["USD", "EUR", "GBP", "AED"]:
        risk += 0.25
        reason = "unusual_currency"

    if tx.amount > 10000:
        risk += 0.20
        reason = "very_high_value"

    risk = min(risk + random.uniform(0, 0.15), 1.0)

    flagged = risk > 0.65

    if flagged:
        FRAUD_FLAGS.inc()

    REQ_COUNT.labels("/score", "200").inc()
    REQ_LATENCY.labels("/score").observe(time.time() - t)

    print(json.dumps({
        "event": "transaction_scored",
        "id": tx.transaction_id,
        "amount": tx.amount,
        "risk": round(risk, 3),
        "flagged": flagged
    }))

    return FraudScore(
        transaction_id=tx.transaction_id,
        risk_score=round(risk, 3),
        is_flagged=flagged,
        reason=reason,
        scored_at=datetime.utcnow().isoformat()
    )
