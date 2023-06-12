from typing import Type, TypeVar
from app.database import Database
from app.crud.base import CRUDBase
from app.models.ticket import Ticket

from app.database import db
from app.models.base import Base

ModelType = TypeVar("ModelType", bound=Base)

class CRUDTicket(CRUDBase):
    def __init__(self, db: Database, model: Type[ModelType]) -> None:
        super().__init__(db, model)

ticket_crud = CRUDTicket(db, Ticket)