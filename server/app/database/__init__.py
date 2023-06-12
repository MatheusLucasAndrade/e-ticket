from app.database.database import Database
from app.core.config import settings

db = Database(connection_string=settings.db_connection_string)