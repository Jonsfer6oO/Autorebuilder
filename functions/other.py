from configurations import config

def compare_secret_key(hook_secret_key: str) -> bool:
    return config.webhooks.secret_key == hook_secret_key