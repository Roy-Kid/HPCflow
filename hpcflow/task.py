# author: Roy Kid
# contact: lijichen365@126.com
# date: 2021-12-19
# version: 0.0.1

from typing import Sequence
from pydantic import BaseModel

class Task(BaseModel):

    """Task class, which represents a job submitted to queue system.
    
    Args:
        baseDir (str): remote directory which store upload_files.
        upload_files (Sequence[str]): data files needed to upload to remote HPC
        download_files (Sequence[str]):
        result files needed to retrieve back to local after task finish

    """

    baseDir: str = ''
    upload_files: Sequence[str] = []
    download_files: Sequence[str] = []
    out: str = None
    err: str = None
    before_run: Sequence[str] = []
    after_run: Sequence[str] = []

    