import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


@dataclass(eq=False)
class BaseConfig(object):
    SECRET_KEY: str = os.urandom(20)
    DEBUG: bool = False
    TESTING: bool = False

    @staticmethod
    def init_app(app):
        pass


@dataclass
class DevelopmentConfig(BaseConfig):
    DEBUG: bool = True
    DATABASE_URL: str = os.environ.get("DATABASE_URL")


@dataclass
class ProductionConfig(BaseConfig):
    DATABASE_URL: str = os.environ.get("DATABASE_URL")


@dataclass
class TestingConfig(BaseConfig):
    DATABASE_URL: str = os.environ.get("DATABASE_URL")
    TESTING: bool = True


config_dict = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
