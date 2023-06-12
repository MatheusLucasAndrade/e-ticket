from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

class Database:
    def __init__(self, connection_string: str) -> None:
        conn_string = self.__connection_string(connection_string)

        self.engine = create_async_engine(
            url=conn_string,
            echo=True
        )

        self.session = async_sessionmaker(bind=self.engine, autoflush=False)

    def __connection_string(self, connection_string: str) -> str:
        return connection_string