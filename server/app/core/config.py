from pydantic import BaseSettings, validator

class SettingsDatabase(BaseSettings):
    @validator("SQLALCHEMY_DATABASE_URI", pre=True, check_fields=False)
    def __init__(self) -> None:
        self.db_connection_string = "postgresql+asyncpg://postgres:admin@localhost:5432/eticket"

settings = SettingsDatabase()