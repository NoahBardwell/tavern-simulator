import logging
import simplejson as json

from inventory import Inventory
from item import Item

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info(event)
    event_body = json.loads(event.get("body"))
    logger.info(event_body)

    item = Item.parse_obj(event_body)
    logger.info(item.dict())
    inventory = Inventory.parse_obj({"items": [item.dict()]})
    inventory.update()
    logger.info(inventory)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': inventory.json()
    }
