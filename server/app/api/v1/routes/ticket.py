from fastapi import APIRouter
from fastapi.params import Depends

from app.services.ticket import TicketService

router = APIRouter()

@router.get("/{id}")
async def read_values_by_id(
    *,
    ticket_service: TicketService = Depends(),
    id: int
    ):
    return await ticket_service.get(id=id)
