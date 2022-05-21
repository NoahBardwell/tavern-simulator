import logging

from inventory import Inventory
from item import Item

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info(event)

    item = Item.parse_obj(get_input_dict())
    logger.info(item.dict())
    inventory = Inventory.parse_obj({"items": [item.dict()]})
    logger.info(inventory)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello there!'
    }


def get_input_dict():
    return {"name": "Aged Cheese", "quality": 5, "sell_in": 3}
