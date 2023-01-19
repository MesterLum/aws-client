from pydantic import BaseSettings

class Settings(BaseSettings):
    db_host: str
    db_user: str
    db_pass: str
    db_name: str
    db_port: int = 5432

    @property
    def connection_url(self) -> str:
        return f"postgresql+psycopg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}".format(
                    db_user=self.db_user,
                    db_pass=db_pass,
                    db_host=db_host,
                    db_port=db_port,
                    db_name=db_name
                )
