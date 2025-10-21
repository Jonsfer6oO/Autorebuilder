from dataclasses import dataclass


@dataclass
class Host:
    ip: str
    port: int


@dataclass
class WebHooks:
    path_server: str
    main_branch: str
    remote: str
    services_list: str
    secret_key: str


@dataclass
class Config:
    host: Host
    webhooks: WebHooks