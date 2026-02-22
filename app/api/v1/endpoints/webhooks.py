from fastapi import APIRouter, Depends, HTTPException, Header, Request
from sqlalchemy.orm import Session
from typing import List
import json

from app.api import deps
from app.models.webhook import WebhookEvent
from app.schemas.webhook import Webhook, WebhookCreate, WebhookResponse
from app.core.config import settings

router = APIRouter()

@router.get("/all", response_model=List[Webhook])
def get_all_webhooks(db: Session = Depends(deps.get_db)):
    """
    Retrieve all processed webhook events.
    """
    return db.query(WebhookEvent).all()

@router.post("/webhook", response_model=WebhookResponse)
async def receive_webhook(
    request: Request, 
    db: Session = Depends(deps.get_db),
    x_signature: str = Header(None)
):
    """
    Receive and store a webhook event.
    Verifies the signature before processing.
    """
    if x_signature != settings.SHARED_SECRET:
        raise HTTPException(status_code=401, detail="Invalid signature")

    payload = await request.json()

    event_id = payload.get("event_id")
    if not event_id:
        raise HTTPException(status_code=400, detail="Missing event_id")

    existing = db.query(WebhookEvent).filter_by(event_id=event_id).first()
    if existing:
        return {"status": "duplicate", "message": "Event already processed"}

    event = WebhookEvent(
        event_id=event_id,
        payload=json.dumps(payload)
    )

    db.add(event)
    db.commit()

    return {"status": "success", "message": "Event stored"}
