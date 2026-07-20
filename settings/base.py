from pathlib import Path
from pydantic import BaseSettings

BASE_DIR = Path(__file__).absolute().parent.parent.parent


class AdvancedBaseSettings(BaseSettings):
    # Родительский объект с общими настройками

    class Config:
        allow_mutation = False
