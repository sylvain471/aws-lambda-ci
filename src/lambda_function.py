import json
from utils import get_extra_utils

def lambda_handler(event, context):
    # TODO implement
    # a first trivial example
    print(get_extra_utils())
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

if __name__=="__main__":
    print(lambda_handler({},{}))