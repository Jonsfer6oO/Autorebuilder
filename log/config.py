import os 

config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standart': {
            'format': '%(levelname)s: %(message)s'
        },
        'debug': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standart',
            'level': 'INFO',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers':{
        '': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False
        },
    }
}