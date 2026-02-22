from pydantic import BaseModel, Field, field_validator
from typing import Dict, Any, Optional
import json

class WebhookBase(BaseModel):
    event_id: str = Field(..., description="Unique identifier for the webhook event")
    payload: Dict[str, Any] = Field(..., description="The event data payload")

class WebhookCreate(WebhookBase):
    pass

class Webhook(BaseModel):
    id: int
    event_id: str
    payload: Any

    @field_validator('payload', mode='before')
    @classmethod
    def parse_payload(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                return v
        return v

    class Config:
        from_attributes = True

class WebhookResponse(BaseModel):
    status: str
    message: str
