from app import crud

class TicketService():
    def __init__(self) -> None:
        self.ticket_crud = crud.ticket_crud

    async def get(self, id: int):
        if await self.ticket_crud.get_by_id(id):
            return await self.ticket_crud.get_by_id(id)
