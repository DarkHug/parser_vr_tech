import json
import logging.config

from pythonjsonlogger.json import JsonFormatter

import saver
from parser import parse

MESSAGE_FORMAT = '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s'


def get_config(debug: bool = False) -> dict:
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'json': {
                '()': JsonFormatter,
                'format': MESSAGE_FORMAT,
            },
        },
        'handlers': {
            'stream': {
                'level': 'DEBUG' if debug else 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'json',
            },
        },
        'loggers': {
            '': {
                'level': 'DEBUG' if debug else 'INFO',
                'handlers': ['stream'],
            },
        },
    }


if __name__ == '__main__':
    logging.config.dictConfig(get_config(debug=False))
    with open("seed.json", 'r') as file:
        data = json.load(file)
        print(data)
    url = data["product_url"]

    product = parse(url)
    saver.save_to_db(product)
    saver.save_to_json(product)
