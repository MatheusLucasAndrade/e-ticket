from app.database import Database
from sqlalchemy import select, update, delete
from typing import Optional, Type

from app.models.base import Base

class CRUDBase:
    def __init__(self, db: Database, model: Type[Base]) -> None:
        self.db = db
        self.model = model

    async def get_all(self):
        async with self.db.session() as session:
            stmt = select(self.model)
            result = session.execute(stmt)
            return result.scalars().all()
        
    async def get_by_id(self, id: int) -> Optional[Base]:
        async with self.db.session() as session:
            stmt = select(self.model).where(self.model.id == id)
            result = await session.execute(stmt)
            return result.scalar()
    
    async def add(self, model, auto_commit: bool = True):
        async with self.db.session() as session:
            with session.begin():
                session.add(model)
                if auto_commit:
                    self.commit()
        
    async def update(self, id: int, values: dict, auto_commit: bool = True):
        async with self.db.session() as session:
            with session.begin():
                stmt = update(self.model).where(self.model.id == id).values(values.dict())
                session.execute(stmt)
                if auto_commit:
                    self.commit()
            
    async def delete(self, id: int, auto_commit: bool = True):
        async with self.db.session() as session:
            with session.begin():
                stmt = delete(self.model).where(self.model.id == id)
                session.execute(stmt)
                if auto_commit:
                    self.commit()

    async def commit(self):
        async with self.db.session() as session:
            session.commit()
