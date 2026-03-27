from pydantic import BaseModel
from typing import Dict, List

class Action(BaseModel):
    action_type: str
    target: str

class Observation(BaseModel):
    logs: str
    metrics: Dict[str, float]
    alerts: List[str]
    service_status: str

class Reward(BaseModel):
    value: float
