import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello kumar from Lambda!....... (Modified v0.2')
    }
