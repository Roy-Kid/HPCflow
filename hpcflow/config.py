# author: Roy Kid
# contact: lijichen365@126.com
# date: 2021-12-19
# version: 0.0.1

from pydantic.main import BaseModel


class Config(BaseModel):
    
    DEFAULT_RETRIES: int = 3
    RETRY_DELAY: int = 5