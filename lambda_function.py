import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello kumar chowdary from Lambda!....... (Modified v0.2')
    }
