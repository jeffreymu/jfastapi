import io
import logging
import os
from contextlib import contextmanager
from functools import lru_cache
from io import StringIO
from typing import Optional

from dotenv.main import DotEnv
from pydantic import BaseSettings, Field

logger = logging.getLogger(__name__)

def my_get_stream(self):
    if isinstance(self.dotenv_path, StringIO):
        yield self.dotenv_path
    elif os.path.isfile(self.dotenv_path):
        with io.open(self.dotenv_path, encoding='utf-8') as stream:
            yield stream
    else:
        if self.verbose:
            logger.warning("File doesn't exist %s", self.dotenv_path)
        yield StringIO('')


DotEnv._get_stream = contextmanager(my_get_stream)


class Settings(BaseSettings):
    ENVIRONMENT: Optional[str] = Field(None, env="ENVIRONMENT")
    SECRET_KEY = 'ZEuk2U9svM2WRJql4Fs2lEvD05ZDQXZdKboim__SQqsUUqJwStZJq6u0e30bIL4Qe80PB48X1dcIZHjxqLzUiA'
    API_V1_STR = "/api/v1"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8
    ALGORITHM = "HS256"

    SECRET_KEY: str
    ALGORITHM: str

    class Config:
        env_file = ".env"
        case_sensitive = True


class DevConfig(Settings):
    # redis
    REDIS_HOST: Optional[str] = Field(None, env="DEV_REDIS_HOST")
    REDIS_PORT: Optional[int] = Field(None, env="DEV_REDIS_PORT")
    REDIS_USERNAME: Optional[str] = Field(None, env="DEV_REDIS_USERNAME")
    REDIS_PASSWORD: Optional[str] = Field(None, env="DEV_REDIS_PASSWORD")
    REDIS_DB: Optional[int] = Field(None, env="DEV_REDIS_DB")

    # Mysql
    MYSQL_SERVER: Optional[str] = Field(None, env="DEV_MYSQL_SERVER")
    MYSQL_USER: Optional[str] = Field(None, env="DEV_MYSQL_USER")
    MYSQL_PASSWORD: Optional[str] = Field(None, env="DEV_MYSQL_PASSWORD")
    MYSQL_DB_NAME: Optional[str] = Field(None, env="DEV_MYSQL_DB_NAME")
    MYSQL_PORT: Optional[int] = Field(None, env="DEV_MYSQL_PORT")

class ProdConfig(Settings):
    REDIS_HOST: Optional[str] = Field(None, env="PROD_REDIS_HOST")
    REDIS_PORT: Optional[int] = Field(None, env="PROD_REDIS_PORT")
    REDIS_USERNAME: Optional[str] = Field(None, env="PROD_REDIS_USERNAME")
    REDIS_PASSWORD: Optional[str] = Field(None, env="PROD_REDIS_PASSWORD")
    REDIS_DB: Optional[int] = Field(None, env="PROD_REDIS_DB")

    MYSQL_SERVER: Optional[str] = Field(None, env="PROD_MYSQL_SERVER")
    MYSQL_USER: Optional[str] = Field(None, env="PROD_MYSQL_USER")
    MYSQL_PASSWORD: Optional[str] = Field(None, env="PROD_MYSQL_PASSWORD")
    MYSQL_DB_NAME: Optional[str] = Field(None, env="PROD_MYSQL_DB_NAME")
    MYSQL_PORT: Optional[int] = Field(None, env="PROD_MYSQL_PORT")


class FactoryConfig:
    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):

        if self.env_state == "development":
            return DevConfig()

        elif self.env_state == "production":
            return ProdConfig()

        elif self.env_state == "testing":
            return TestConfig()


@lru_cache()
def get_configs():
    from dotenv import load_dotenv
    load_dotenv(encoding='utf-8')
    return FactoryConfig(Settings().ENVIRONMENT)()


configs = get_configs()
settings = Settings()