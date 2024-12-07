from src.lambda_function import lambda_handler
from src.utils import get_extra_utils
import json


def test_lambda_function():
    assert {
        "statusCode":200,
        "body": json.dumps(get_extra_utils())
    } == lambda_handler({},{})
    

def test_lambda_function_2():
    assert lambda_handler({},{})["statusCode"]==200