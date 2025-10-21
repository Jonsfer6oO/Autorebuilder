from environs import Env

from . import config_model as cm
from . import config_env as ce

env = ce.ENVConfig.read()

config = cm.Config(
    cm.Host(
        ip=env('HOST_IP'),
        port=env('PORT')
    ),
    cm.WebHooks(
        path_server=env('PATH_VOLUMES'),
        main_branch=env('MAIN_BRANCH'),
        remote=env('REMOTE'),
        services_list=env('SERVICES_LIST')
    )
)