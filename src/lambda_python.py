import json
from src.utils import get_extra_utils

def lambda_handler(event, context):
    # TODO implement
    # a first trivial example
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
