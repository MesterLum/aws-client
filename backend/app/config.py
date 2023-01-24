from pydantic import BaseSettings

class Settings(BaseSettings):
    debug: bool = True

    # database
    db_host: str
    db_user: str
    db_pass: str
    db_name: str
    db_port: int = 5432

    # Security
    secret_key: str = "14a4c2cac279071f9adf3f80c0817f587d49a9f206df3d33bf06de20fff6ede9"
    secret_key_refresh: str = "5b25afa03115fcc3cab0784995ac99bb629877b461ca9b7b93c7b46f6d4008f4"

    @property
    def connection_url(self) -> str:
        return "postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}".format(
                    db_user=self.db_user,
                    db_pass=self.db_pass,
                    db_host=self.db_host,
                    db_port=self.db_port,
                    db_name=self.db_name
                )


settings = Settings()
