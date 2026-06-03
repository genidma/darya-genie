#!/usr/bin/env python3
"""
Darya Certification Gatekeeper
Validates assessment quiz and updates User_Registry via FastAPI endpoint
"""

import hashlib
import json
import requests
from datetime import datetime
from typing import Dict, List, Tuple

ANSWER_KEY = {
    "1": "D", "2": "C", "3": "B", "4": "B", "5": "C",
    "6": "B", "7": "B", "8": "C", "9": "C", "10": "B",
    "11": "B", "12": "C", "13": "C", "14": "C", "15": "D"
}
PASSING_SCORE = 12  # 80%
API_ENDPOINT = "http://localhost:8000/api/certify"


def validate_answers(user_answers: Dict[str, str]) -> Tuple[bool, int, List[str]]:
    """
    Validate user answers against answer key.
    
    Returns:
        Tuple of (passed, score, incorrect_questions)
    """
    correct = 0
    incorrect = []
    
    for qid, correct_answer in ANSWER_KEY.items():
        user_answer = user_answers.get(qid, "").upper()
        if user_answer == correct_answer:
            correct += 1
        else:
            incorrect.append(qid)
    
    passed = correct >= PASSING_SCORE
    return passed, correct, incorrect


def generate_certification_token(wallet_id: str, score: int) -> str:
    """Generate SHA-256 token for certification."""
    data = f"{wallet_id}:{score}:{datetime.utcnow().isoformat()}"
    return hashlib.sha256(data.encode()).hexdigest()[:16]


def update_user_registry(wallet_id: str, token: str, passed: bool) -> Dict:
    """
    Update user registry via POST request to FastAPI endpoint.
    
    Returns:
        Response JSON from server
    """
    payload = {
        "wallet_id": wallet_id,
        "certification_token": token,
        "timestamp": datetime.utcnow().isoformat(),
        "status": "CERTIFIED" if passed else "FAILED"
    }
    
    try:
        response = requests.post(API_ENDPOINT, json=payload, timeout=5)
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e), "status": "FAILED"}


def process_certification(user_answers: Dict[str, str], wallet_id: str) -> Dict:
    """
    Main certification processing pipeline.
    
    Args:
        user_answers: Dictionary of question_id -> answer
        wallet_id: Mobile wallet identifier
        
    Returns:
        Complete certification result
    """
    passed, score, incorrect = validate_answers(user_answers)
    token = generate_certification_token(wallet_id, score)
    
    result = {
        "wallet_id": wallet_id,
        "passed": passed,
        "score": score,
        "total_questions": len(ANSWER_KEY),
        "incorrect_questions": incorrect,
        "certification_token": token if passed else None,
        "timestamp": datetime.utcnow().isoformat()
    }
    
    if passed:
        api_response = update_user_registry(wallet_id, token, passed)
        result["api_response"] = api_response
        
    return result


if __name__ == "__main__":
    # Example usage
    sample_answers = {str(i): "B" for i in range(1, 16)}  # Mock answers
    sample_wallet = "03001234567"
    
    result = process_certification(sample_answers, sample_wallet)
    print(json.dumps(result, indent=2))