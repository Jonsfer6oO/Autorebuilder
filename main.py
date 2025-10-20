from fastapi import FastAPI
import uvicorn 

import logging

import API
from configurations import config
import log 

logging.config.dictConfig(log.config)

main_logger = logging.getLogger(__name__)

app = FastAPI()
main_logger.info('App created')

app.include_router(API.gitea_router)
main_logger.info('Routers are connected')

if __name__ == "__main__":
    ip = config.host.ip
    port = config.host.port
    main_logger.info(f'strart server: ip: {ip} port: {port}')
    uvicorn.run(
        app, 
        host=ip, 
        port=int(port)
    )