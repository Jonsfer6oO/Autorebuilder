import subprocess
import logging
import os

from configurations import config
repo_logger = logging.getLogger(__name__)

def git_pull(repo_path: str):

    if not os.path.isdir(repo_path):
        repo_logger.info('Directory not found')
        raise FileNotFoundError(f"Каталог '{repo_path}' не найден")
    try:
        result = subprocess.run(
            ["git", "pull", config.webhooks.remote, config.webhooks.main_branch],
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=True
        )
        repo_logger.info('changes received')
        return result.stdout
    except subprocess.CalledProcessError as e:
        repo_logger.error('Error while receiving changes', exc_info=True)
        raise RuntimeError(e.stderr)
