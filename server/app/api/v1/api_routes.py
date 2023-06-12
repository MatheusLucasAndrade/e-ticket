from fastapi import APIRouter

from app.api.v1.routes import (
    ticket
)

api_router = APIRouter()
api_router.include_router(ticket.router, prefix="/ticket", tags=["tickets"])