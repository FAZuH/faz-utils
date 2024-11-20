from abc import ABC

from faz.utils.database.base_database import BaseDatabase


class BaseMySQLDatabase(BaseDatabase, ABC):

    def __init__(
        self,
        user: str,
        password: str,
        host: str,
        port: int,
        database: str,
    ) -> None:
        super().__init__(
            sync_driver="mysql+pymysql",
            async_driver="mysql+aiomysql",
            user=user,
            password=password,
            host=host,
            port=port,
            database=database,
        )
