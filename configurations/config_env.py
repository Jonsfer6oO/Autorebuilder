from environs import Env

from dataclasses import dataclass


@dataclass 
class ENVConfig:
    def read():
        env = Env()
        env.read_env()

        return env