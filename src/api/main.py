from fastapi import FastAPI, Depends, Header, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid

app = FastAPI(
    title="Darya Genie API",
    description="Central nervous system for Darya Genie platform: safety certification, field data validation, and micro-incentive payouts.",
    version="0.1.0"
)

# ---------------------------------------------------------------------------
# Schemas
# ---------------------------------------------------------------------------

class RestorationSchema(BaseModel):
    coordinates: tuple[float, float] = Field(..., description="(lat, lng) of planting site")
    species: str = Field(..., max_length=100)
    quantity: int = Field(..., gt=0, le=1000)
    photo_url: Optional[str] = None
    bounty: float = Field(..., gt=0, description="Micro-incentive amount in local currency")

class WasteSchema(BaseModel):
    gps_coordinates: tuple[float, float]
    photo_url: str
    waste_type: str
    estimated_volume: float = Field(..., gt=0)

class PaymentResult(BaseModel):
    status: str
    tx_id: str
    amount: float
    timestamp: datetime

class User(BaseModel):
    id: str
    name: str
    is_certified: bool

# ---------------------------------------------------------------------------
# Mock services (to be replaced with real implementations)
# ---------------------------------------------------------------------------

class UserRegistry:
    """Mock user registry – in production this would query a database."""
    _users = {
        "token-abc-123": User(id="u1", name="Alice", is_certified=True),
        "token-def-456": User(id="u2", name="Bob", is_certified=False),
    }

    @classmethod
    async def get_user(cls, token: str) -> Optional[User]:
        return cls._users.get(token)

class GISService:
    """Mock GIS suitability check – in production this would query a spatial layer."""
    _suitable_sites = {(25.0, 55.0), (25.1, 55.1)}

    @classmethod
    async def is_site_ready(cls, coordinates: tuple[float, float]) -> bool:
        # Round to 1 decimal for mock
        rounded = (round(coordinates[0], 1), round(coordinates[1], 1))
        return rounded in cls._suitable_sites

class AntiGamingService:
    """Mock anti-gaming checks – in production this would validate photo metadata, GPS trails, etc."""
    @classmethod
    async def validate_waste_submission(cls, data: WasteSchema) -> bool:
        # Simple mock: reject if photo_url is suspicious
        if "fake" in data.photo_url.lower():
            return False
        return True

class PaymentGateway:
    """Mock payment gateway – in production this would call a real payment provider."""
    @classmethod
    async def process_payout(cls, user_id: str, amount: float) -> PaymentResult:
        return PaymentResult(
            status="success",
            tx_id=str(uuid.uuid4()),
            amount=amount,
            timestamp=datetime.utcnow()
        )

class GlobalLedger:
    """Mock ledger – in production this would write to a blockchain or database."""
    _entries = []

    @classmethod
    async def commit(cls, user_id: str, action: str, tx_id: str) -> None:
        cls._entries.append({
            "user_id": user_id,
            "action": action,
            "tx_id": tx_id,
            "timestamp": datetime.utcnow()
        })

# ---------------------------------------------------------------------------
# Middleware / Dependency
# ---------------------------------------------------------------------------

async def get_current_user(token: str = Header(...)) -> User:
    user = await UserRegistry.get_user(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    if not user.is_certified:
        raise HTTPException(status_code=403, detail="Certification Required")
    return user

# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "darya-genie-api"}

@app.post("/api/v1/submit_restoration", response_model=PaymentResult)
async def submit_planting(data: RestorationSchema, user: User = Depends(get_current_user)):
    """
    Submit a mangrove restoration planting record.

    Steps:
    1. Validate that the planting site is suitable according to the GIS layer.
    2. Process the micro-incentive payout.
    3. Commit the transaction to the global ledger.
    """
    if not await GISService.is_site_ready(data.coordinates):
        raise HTTPException(status_code=400, detail="Invalid Planting Site")

    payment = await PaymentGateway.process_payout(user.id, amount=data.bounty)
    await GlobalLedger.commit(user.id, "restoration", payment.tx_id)

    return payment

@app.post("/api/v1/submit_waste_collection", response_model=PaymentResult)
async def submit_waste(data: WasteSchema, user: User = Depends(get_current_user)):
    """
    Submit a waste collection record.

    Steps:
    1. Run anti-gaming checks on the submission.
    2. Process the micro-incentive payout.
    3. Commit the transaction to the global ledger.
    """
    if not await AntiGamingService.validate_waste_submission(data):
        raise HTTPException(status_code=400, detail="Suspicious submission – anti-gaming check failed")

    # Example bounty calculation: fixed rate per volume
    bounty = data.estimated_volume * 0.5
    payment = await PaymentGateway.process_payout(user.id, amount=bounty)
    await GlobalLedger.commit(user.id, "waste_collection", payment.tx_id)

    return payment
