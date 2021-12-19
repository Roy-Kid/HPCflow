# author: Roy Kid
# contact: lijichen365@126.com
# date: 2021-12-19
# version: 0.0.1

from abc import ABCMeta, abstractmethod
from typing import Union

from pssh.clients import SSHClient
from pydantic import BaseModel

from hpcflow import config


class AbstractSession(metaclass=ABCMeta):
    @abstractmethod
    def connect():
        pass

    @abstractmethod
    def disconnect():
        pass

    @abstractmethod
    def put():
        pass
    
    @abstractmethod
    def get():
        pass
    
    @abstractmethod
    def run():
        pass

class Session(SSHClient, AbstractSession, BaseModel):

    host: str
    user: str = None
    password: str = None
    port: int = None
    pkey: Union[str, bytes] = None
    num_retries: int = config.DEFAULT_RETRIES
    retry_delay: int = config.RETRY_DELAY
    allow_agent: bool = True
    timeout: int = None
    forward_ssh_agent: bool = False
    proxy_host: str = None
    proxy_port: int = None
    proxy_pkey: Union[str, bytes] = None
    proxy_user: str = None
    proxy_password: str = None
    _auth_thread_pool: bool = True
    keepalive_seconds: int = 60
    identity_auth: bool = True
    ipv6_only: bool = False

    def connect(self):
        super().__init__(
            self.host,
            self.user,
            self.password,
            self.port,
            self.pkey,
            self.num_retries,
            self.retry_delay,
            self.allow_agent,
            self.timeout,
            self.forward_ssh_agent,
            self.proxy_host,
            self.proxy_port,
            self.proxy_pkey,
            self.proxy_user,
            self.proxy_password,
            self._auth_thread_pool,
            self.keepalive_seconds,
            self.identity_auth,
            self.ipv6_only,
        )
        
    def disconnect(self):
        return super().disconnect()
