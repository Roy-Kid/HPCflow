# author: Roy Kid
# contact: lijichen365@126.com
# date: 2021-12-19
# version: 0.0.1

from typing import Sequence
from pydantic import BaseModel

class Resource(BaseModel):
    
    nndoes: int
    ncore: int
    ngpu: int = 0
    queueName: str
    modules: Sequence = []
    envVariables: Sequence = []
    