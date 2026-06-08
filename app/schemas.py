from pydantic import BaseModel
from typing import List, Dict, Any

class TravelPlanRequest(BaseModel):
    query: str
    user_id: str

class TravelPlanResponse(BaseModel):
    status: str
    messages: List[Dict[str, Any]]