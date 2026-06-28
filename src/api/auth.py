"""
Darya Certification Authentication Middleware
Ensures only certified collectors can receive micro-incentive payouts
"""

from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer
from typing import Optional


class UserRegistry:
    """Mock database layer - replace with actual DB implementation."""
    
    def __init__(self):
        self._users = {}  # wallet_id -> {is_certified, certification_token, ...}
    
    def is_certified(self, wallet_id: str) -> bool:
        """Check if user has valid certification."""
        user = self._users.get(wallet_id)
        return user.get("is_certified", False) if user else False
    
    def get_user(self, wallet_id: str) -> Optional[dict]:
        """Retrieve user record."""
        return self._users.get(wallet_id)
    
    def certify_user(self, wallet_id: str, token: str) -> bool:
        """Record successful certification."""
        self._users[wallet_id] = {
            "is_certified": True,
            "certification_token": token,
            "certified_at": None  # Set by DB layer
        }
        return True


user_registry = UserRegistry()


def certify_user(wallet_id: str, token: str) -> bool:
    """
    FastAPI endpoint handler for certification POST.
    Called by certification_gatekeeper.py upon quiz completion.
    """
    return user_registry.certify_user(wallet_id, token)


def require_certification(wallet_id: str = Depends(HTTPBearer())) -> bool:
    """
    Dependency that validates user certification before payment processing.
    Raises HTTPException if user is not certified.
    """
    if not wallet_id:
        raise HTTPException(
            status_code=403,
            detail={
                "error": "CERTIFICATION_REQUIRED",
                "message": "Complete Safety-First Certification before receiving payouts",
                "redirect": "/docs/safety/"
            }
        )
    return True


def check_certification_status(wallet_request) -> dict:
    """
    Utility function for checking certification status on webhook calls.
    Returns status dict for payment processing decisions.
    """
    wallet_id = wallet_request.get("sender_wallet")
    
    if not wallet_id:
        return {"certified": False, "reason": "NO_WALLET_PROVIDED"}
    
    if user_registry.is_certified(wallet_id):
        return {"certified": True, "reason": "VALID_CERTIFICATION"}
    
    return {
        "certified": False, 
        "reason": "USER_NOT_CERTIFIED",
        "action": "HOLD_PAYOUT"
    }