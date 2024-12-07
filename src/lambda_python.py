import json

def lambda_handler(event, context):
    # TODO implement
    # a first trivial example
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
