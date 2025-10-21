from fastapi import APIRouter, Request
from fastapi import HTTPException, status

import os
import logging

from configurations import config as cf
from functions import git_pull

gitea_logger = logging.getLogger(__name__)

gitea_router = APIRouter(
    prefix='/gitea',
    tags=['Gitea']
)

@gitea_router.post(path='/webhooks')
async def handle_gitea_hook(request: Request):
    try:
        json = await request.json()
        for service in cf.webhooks.services_list.split():
            if json['repository']['name'] == service:
                pull = git_pull(os.path.join(cf.webhooks.path_server, service))
                break
        else:
            raise  HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        gitea_logger.info(pull)
        gitea_logger.info('Changes received')
        return {'detail': 'OK'}
    
    except HTTPException:
        gitea_logger.error('Not repo')
        raise
    except:
        gitea_logger.error('Error processing webhooks', exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)