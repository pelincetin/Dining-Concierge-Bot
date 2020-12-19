import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('lex-runtime')
    response = client.post_text(
        botName='DiningConcierge',
        botAlias='$LATEST',
        userId='LF0',
        sessionAttributes={},
        requestAttributes={},
        inputText=event['text']
    )
    print(event['text'])
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': response
    }