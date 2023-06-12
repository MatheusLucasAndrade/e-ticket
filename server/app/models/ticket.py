from .base import Base
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.orm import Mapped, mapped_column

class Ticket(Base):
    __tablename__ = 'ticket'
    id: Mapped[int] = mapped_column(primary_key=True)
    test: Mapped[str] = mapped_column(String, nullable=True)