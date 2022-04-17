import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
def handler(event, context):
    logger.info(event)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello there!'
    }