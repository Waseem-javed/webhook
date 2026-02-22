from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base

class WebhookEvent(Base):
    __tablename__ = "webhook_events"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(String, unique=True, index=True)
    payload = Column(Text)
