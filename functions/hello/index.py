# functions/hello/index.py 

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "hello from lambda"
    }