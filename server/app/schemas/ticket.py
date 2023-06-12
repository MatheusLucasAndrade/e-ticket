from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from app.models.enums.enums_base import PreferenceCategory, UrgencyProtocol


class TicketBase(BaseModel):
    hash_Id: str
    protocol_id: str
    urgency: UrgencyProtocol
    preference: PreferenceCategory
    entry_date: datetime
    observation: Optional[str]

    class Config:
        orm_mode: True

class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    observation: Optional[str]
